/* ============================================================
   AeroLLM Portal — lớp đồng bộ tùy chọn (Google Sheets / Apps Script)
   ------------------------------------------------------------
   Dùng chung cho: index.html, danh-gia.html, admin.html,
                   portal.html, ket-qua.html, ket-noi.html

   • Ghi (POST): fetch text/plain → không kích hoạt preflight CORS.
     Nếu mạng lỗi → xếp hàng trong localStorage, tự gửi lại sau.
   • Đọc (GET) : JSONP → luôn chạy được từ GitHub Pages.
   • Không có URL Web App → mọi hàm trả về "tắt", trang vẫn chạy
     bình thường bằng localStorage như trước.
   ============================================================ */
(function (global) {
  'use strict';

  /* Không gửi dữ liệu tới backend mặc định. Giáo viên chủ động cấu hình
     Apps Script của mình trên trang Kết nối dữ liệu. */
  var DEFAULT_URL = '';

  var URL_KEY   = 'stem_api_url';
  var QUEUE_KEY = 'stem_sync_queue';
  var META_KEY  = 'stem_sync_meta';
  var MAX_QUEUE = 500;

  /* ── tiện ích lưu trữ ── */
  function readJSON(key, fallback) {
    try { return JSON.parse(localStorage.getItem(key)) ?? fallback; }
    catch (e) { return fallback; }
  }
  function writeJSON(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {}
  }

  /* ── cấu hình URL ── */
  function normalizeUrl(u) {
    u = String(u || '').trim();
    if (!u) return '';
    if (!/^https:\/\/script\.google\.com\//.test(u)) return u; // vẫn cho phép, cảnh báo ở UI
    return u.replace(/\/+$/, '');
  }
  function getUrl() {
    var q = new URLSearchParams(location.search).get('api');
    if (q) { setUrl(q); }
    return localStorage.getItem(URL_KEY) || global.STEM_API_URL || DEFAULT_URL;
  }
  function setUrl(u) {
    u = normalizeUrl(u);
    if (u) localStorage.setItem(URL_KEY, u);
    else   localStorage.removeItem(URL_KEY);
    return u;
  }
  function enabled() { return !!getUrl(); }

  /* ── hàng đợi ── */
  function queue() { return readJSON(QUEUE_KEY, []); }
  function queueSize() { return queue().length; }
  function enqueue(item) {
    var q = queue();
    // chống trùng: cùng type + cùng uid thì ghi đè
    var i = q.findIndex(function (x) { return x.type === item.type && x.uid && x.uid === item.uid; });
    if (i >= 0) q[i] = item; else q.push(item);
    if (q.length > MAX_QUEUE) q = q.slice(q.length - MAX_QUEUE);
    writeJSON(QUEUE_KEY, q);
    paint();
  }
  function clearQueue() { writeJSON(QUEUE_KEY, []); paint(); }

  /* ── gửi 1 gói tới Web App ── */
  function rawPost(body) {
    var url = getUrl();
    if (!url) return Promise.reject(new Error('Chưa cấu hình URL Web App'));
    return fetch(url, {
      method: 'POST',
      // text/plain = "simple request" → trình duyệt không gửi OPTIONS preflight
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(body),
      redirect: 'follow'
    }).then(function (res) {
      return res.text().then(function (txt) {
        var data;
        try { data = JSON.parse(txt); } catch (e) { data = { ok: res.ok, raw: txt }; }
        if (!res.ok || data.ok === false) throw new Error(data.error || ('HTTP ' + res.status));
        return data;
      });
    });
  }

  /* ── đọc dữ liệu bằng JSONP ── */
  var jsonpSeq = 0;
  function get(action, params, timeoutMs) {
    var url = getUrl();
    if (!url) return Promise.reject(new Error('Chưa cấu hình URL Web App'));
    params = params || {};
    return new Promise(function (resolve, reject) {
      var cb = '__stemcb' + (++jsonpSeq) + '_' + Date.now();
      var qs = new URLSearchParams(Object.assign({ action: action, callback: cb }, params));
      var s = document.createElement('script');
      var done = false;
      // Apps Script khởi động nguội có thể mất >20s cho lần gọi đầu
      var timer = setTimeout(function () { finish(new Error('Hết thời gian chờ máy chủ')); }, timeoutMs || 45000);

      function finish(err, data) {
        if (done) return; done = true;
        clearTimeout(timer);
        // giữ callback dạng no-op thay vì xoá hẳn — nếu Apps Script trả lời muộn (sau khi
        // đã hết giờ), script <script src> vẫn gọi được tên hàm này mà không văng lỗi console
        global[cb] = function () {};
        setTimeout(function () { try { delete global[cb]; } catch (e) {} }, 60000);
        if (s.parentNode) s.parentNode.removeChild(s);
        err ? reject(err) : resolve(data);
      }
      global[cb] = function (data) {
        if (data && data.ok === false) finish(new Error(data.error || 'Lỗi máy chủ'));
        else finish(null, data);
      };
      s.onerror = function () { finish(new Error('Không gọi được Web App (kiểm tra quyền truy cập)')); };
      s.src = url + (url.indexOf('?') >= 0 ? '&' : '?') + qs.toString();
      document.head.appendChild(s);
    });
  }

  /* ── ghi dữ liệu (có hàng đợi dự phòng) ── */
  function push(type, payload, opts) {
    opts = opts || {};
    var item = {
      type: type,
      uid: opts.uid || payload.uid || '',
      payload: payload,
      queuedAt: new Date().toISOString(),
      device: deviceId()
    };
    if (!enabled()) { enqueue(item); return Promise.resolve({ ok: false, queued: true, reason: 'offline-config' }); }

    return rawPost({ type: type, uid: item.uid, device: item.device, payload: payload })
      .then(function (r) { touchMeta({ lastPushAt: new Date().toISOString() }); paint(); return r; })
      .catch(function (err) {
        enqueue(item);
        return { ok: false, queued: true, error: err.message };
      });
  }

  /* ── đẩy toàn bộ hàng đợi ── */
  function flush() {
    var q = queue();
    if (!q.length || !enabled()) return Promise.resolve({ sent: 0, left: q.length });
    return rawPost({ type: 'batch', items: q })
      .then(function (r) {
        clearQueue();
        touchMeta({ lastPushAt: new Date().toISOString() });
        return { sent: q.length, left: 0, server: r };
      })
      .catch(function (err) { paint(); return { sent: 0, left: q.length, error: err.message }; });
  }

  /* ── siêu dữ liệu / thiết bị ── */
  function meta() { return readJSON(META_KEY, {}); }
  function touchMeta(patch) { writeJSON(META_KEY, Object.assign(meta(), patch)); }
  function deviceId() {
    var m = meta();
    if (!m.deviceId) { m.deviceId = 'dev_' + Math.random().toString(36).slice(2, 8); writeJSON(META_KEY, m); }
    return m.deviceId;
  }

  /* ── kiểm tra kết nối ── */
  function ping() {
    return get('ping', {}, 45000).then(function (r) {
      touchMeta({ lastPingAt: new Date().toISOString(), config: r.config || null });
      paint();
      return r;
    });
  }

  /* ── huy hiệu trạng thái nổi ── */
  var badgeEl = null;
  function paint() {
    if (!badgeEl) return;
    var n = queueSize();
    if (!enabled()) {
      badgeEl.className = 'stem-cloud-badge off';
      badgeEl.innerHTML = '☁️ Chưa kết nối Sheets';
      badgeEl.title = 'Bấm để mở trang kết nối';
    } else if (n) {
      badgeEl.className = 'stem-cloud-badge wait';
      badgeEl.innerHTML = '⏳ ' + n + ' bản ghi chờ gửi';
      badgeEl.title = 'Bấm để gửi lại ngay';
    } else {
      badgeEl.className = 'stem-cloud-badge ok';
      badgeEl.innerHTML = '☁️ Đã đồng bộ';
      badgeEl.title = 'Dữ liệu đã lưu lên Google Sheets';
    }
  }
  function mountBadge() {
    if (global.STEM_NO_BADGE || badgeEl) return;
    var css = document.createElement('style');
    css.textContent = '.stem-cloud-badge{position:fixed;right:12px;bottom:12px;z-index:9999;font:600 12px/1 Inter,system-ui,sans-serif;' +
      'padding:9px 13px;border-radius:99px;cursor:pointer;border:1px solid rgba(0, 0, 0, .08);' +
      'box-shadow:0 6px 18px rgba(0, 0, 0, .14);user-select:none;transition:.2s}' +
      '.stem-cloud-badge:hover{transform:translateY(-2px)}' +
      '.stem-cloud-badge.ok{background:#dcfce7;color:#166534}' +
      '.stem-cloud-badge.wait{background:#fef3c7;color:#92400e}' +
      '.stem-cloud-badge.off{background:#e5e7eb;color:#374151}' +
      '@media print{.stem-cloud-badge{display:none}}';
    document.head.appendChild(css);
    badgeEl = document.createElement('div');
    badgeEl.onclick = function () {
      if (!enabled()) { location.href = 'ket-noi.html'; return; }
      badgeEl.innerHTML = '⏳ Đang gửi…';
      flush().then(function (r) {
        if (r.error) alert('Chưa gửi được: ' + r.error);
        paint();
      });
    };
    document.body.appendChild(badgeEl);
    paint();
  }

  /* ── khởi động ── */
  function boot() {
    mountBadge();
    if (enabled() && queueSize()) flush();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
  global.addEventListener('online', function () { if (enabled()) flush(); });

  global.STEMCloud = {
    getUrl: getUrl, setUrl: setUrl, enabled: enabled,
    push: push, get: get, flush: flush, ping: ping,
    queue: queue, queueSize: queueSize, clearQueue: clearQueue,
    meta: meta, deviceId: deviceId, repaint: paint
  };
})(window);

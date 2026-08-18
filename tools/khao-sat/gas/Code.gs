/* =====================================================================
   AEROLLM PORTAL — BACKEND GOOGLE APPS SCRIPT
   ---------------------------------------------------------------------
   Hỗ trợ 12 khoá học, chia 3 nhóm tiêu chí đánh giá:
     • stem     — STEM & Kỹ thuật        (micro:bit, CFD, tên lửa)
     • khtn     — Khoa học tự nhiên & Toán (Lí 10/11/12, Toán 4/7, Lượng tử)
     • ngonngu  — Ngôn ngữ & Xã hội       (Tiếng Anh 7, Ngữ văn 7, Tiếng Việt 4)

   Chức năng:
     1. taoToanBo()      → tạo Spreadsheet (14 sheet) + 7 Google Form,
                           liên kết Form → Sheet, cài trigger.
     2. napDuLieuTuWeb() → nạp khoá học / buổi học / lớp / học sinh từ GitHub Pages.
     3. doPost(e)        → nhận dữ liệu JSON từ các trang HTML.
     4. doGet(e)         → trả dữ liệu JSON/JSONP cho dashboard.
     5. xuLyFormSubmit   → chuẩn hoá phản hồi Google Form vào bảng tổng.
     6. capNhatTongHop() → dựng lại sheet "Tổng hợp" (theo học sinh × khoá).
     7. nangCapV2()      → migrate từ bản 1 khoá (xoá sheet/form cũ rồi tạo mới).

   HƯỚNG DẪN: xem HUONG-DAN.md cùng thư mục.
   ===================================================================== */

/* ───────────────────────── CẤU HÌNH ───────────────────────── */
var CONFIG = {
  OWNER_EMAIL   : '',           // email tài khoản triển khai
  FOLDER_ID     : '',           // để trống để script tự tạo thư mục
  FOLDER_NAME   : 'AeroLLM — Khảo sát & Đánh giá',
  SPREADSHEET   : 'AeroLLM — CSDL Khảo sát & Đánh giá',
  TIMEZONE      : 'Asia/Ho_Chi_Minh',
  TOKEN         : '',           // điền chuỗi bí mật nếu muốn bắt buộc token
  // Email giáo viên nhận báo cáo tổng hợp (có thể đổi lúc khởi tạo hoặc trong trang ket-noi.html)
  TEACHER_EMAIL : '',
  BASE_URL      : 'https://aerovfx.github.io/AeroLLM/tools/khao-sat/',
  ROSTER_URL    : 'https://aerovfx.github.io/AeroLLM/tools/khao-sat/data/students.json',
  COURSES_URL   : 'https://aerovfx.github.io/AeroLLM/tools/khao-sat/data/courses.json'
};

/* ───────────── NHÓM TIÊU CHÍ (khớp data/courses.json) ───────────── */
var GROUPS = [
  { id: 'stem', name: 'STEM & Kỹ thuật', criteria: [
    { id:'teamwork',    label:'Hợp tác nhóm',      icon:'🤝', desc:'Phối hợp và hỗ trợ thành viên' },
    { id:'creativity',  label:'Sáng tạo',          icon:'💡', desc:'Đề xuất ý tưởng, giải pháp mới' },
    { id:'coding',      label:'Kỹ năng lập trình', icon:'💻', desc:'Viết code chính xác, hiệu quả' },
    { id:'problem',     label:'Giải quyết vấn đề', icon:'🧩', desc:'Xử lý lỗi và tìm giải pháp' },
    { id:'presentation',label:'Thuyết trình',      icon:'🎤', desc:'Trình bày rõ ràng, tự tin' },
    { id:'attitude',    label:'Thái độ học tập',   icon:'⭐', desc:'Chăm chỉ, tích cực, đúng giờ' }]},
  { id: 'khtn', name: 'Khoa học tự nhiên & Toán', criteria: [
    { id:'reasoning',   label:'Lập luận khoa học',   icon:'🧠', desc:'Suy luận chặt chẽ, dùng đúng khái niệm' },
    { id:'calculation', label:'Tính toán chính xác', icon:'🔢', desc:'Biến đổi, tính đúng, đúng đơn vị' },
    { id:'experiment',  label:'Thực hành & mô phỏng',icon:'🔬', desc:'Làm thí nghiệm, đo đạc, mô phỏng' },
    { id:'problem',     label:'Giải quyết vấn đề',   icon:'🧩', desc:'Vận dụng vào bài toán/thực tiễn' },
    { id:'presentation',label:'Trình bày & lý giải', icon:'🎤', desc:'Diễn đạt lời giải mạch lạc' },
    { id:'attitude',    label:'Thái độ học tập',     icon:'⭐', desc:'Chăm chỉ, tích cực, đúng giờ' }]},
  { id: 'ngonngu', name: 'Ngôn ngữ & Xã hội', criteria: [
    { id:'listening',   label:'Nghe – Nói',         icon:'🗣️', desc:'Nghe hiểu và diễn đạt bằng lời' },
    { id:'reading',     label:'Đọc hiểu',           icon:'📖', desc:'Nắm ý chính, phân tích văn bản' },
    { id:'writing',     label:'Viết',               icon:'✍️', desc:'Bố cục, diễn đạt, chính tả' },
    { id:'language',    label:'Từ vựng – Ngữ pháp', icon:'🔤', desc:'Dùng từ và cấu trúc chính xác' },
    { id:'creativity',  label:'Sáng tạo & hợp tác', icon:'💡', desc:'Ý tưởng riêng, làm việc nhóm' },
    { id:'attitude',    label:'Thái độ học tập',    icon:'⭐', desc:'Chăm chỉ, tích cực, đúng giờ' }]}
];
function nhom_(id) {
  for (var i = 0; i < GROUPS.length; i++) if (GROUPS[i].id === id) return GROUPS[i];
  return GROUPS[0];
}
function labels_(gid) { return nhom_(gid).criteria.map(function (c) { return c.label; }); }
function ids_(gid)    { return nhom_(gid).criteria.map(function (c) { return c.id; }); }

/* ───────────────────────── TÊN SHEET ───────────────────────── */
var SH = {
  SURVEY  : 'Khảo sát',
  PEER    : { stem: 'ĐG đồng đẳng — STEM', khtn: 'ĐG đồng đẳng — KHTN', ngonngu: 'ĐG đồng đẳng — Ngôn ngữ' },
  TEACHER : { stem: 'Điểm GV — STEM',      khtn: 'Điểm GV — KHTN',      ngonngu: 'Điểm GV — Ngôn ngữ' },
  COURSE  : 'Khoá học',
  STUDENT : 'Học sinh',
  CLASS   : 'Lớp',
  SESSION : 'Buổi học',
  CRIT    : 'Tiêu chí',
  DASH    : 'Tổng hợp',
  LOG     : 'Nhật ký'
};
/* Sheet của bản v1 — sẽ được dọn khi chạy nangCapV2() */
var SHEET_CU = ['Đánh giá đồng đẳng', 'Điểm giáo viên'];

var HEADERS = {};
HEADERS[SH.SURVEY]  = ['Thời gian', 'Mã bản ghi', 'Mã khoá', 'Tên khoá', 'Mã HS', 'Họ tên', 'Trường', 'Khối/Lớp',
                       'Buổi số', 'Tên buổi', 'Số buổi đã học', 'Phần thích nhất', 'Đánh giá (1-5)', 'Độ khó',
                       'Sẽ giới thiệu', 'Mức cải thiện (%)', 'Kỹ năng nổi bật', 'Điều thích nhất', 'Cần cải thiện',
                       'Muốn học thêm', 'Nguồn', 'Thiết bị'];
HEADERS[SH.COURSE]  = ['Mã khoá', 'Tên khoá', 'Biểu tượng', 'Nhóm tiêu chí', 'Số buổi', 'Tài liệu'];
HEADERS[SH.STUDENT] = ['Mã HS', 'Họ tên', 'Lớp', 'Biểu tượng', 'Cập nhật'];
HEADERS[SH.CLASS]   = ['Mã lớp', 'Tên lớp', 'Giáo viên', 'Phòng', 'Lịch học'];
HEADERS[SH.SESSION] = ['Mã khoá', 'Buổi số', 'Tên buổi', 'Giai đoạn'];
HEADERS[SH.CRIT]    = ['Nhóm', 'Mã tiêu chí', 'Tên tiêu chí', 'Biểu tượng', 'Mô tả'];
HEADERS[SH.DASH]    = ['Mã khoá', 'Tên khoá', 'Mã HS', 'Họ tên', 'Lớp', 'Số lượt bạn ĐG', 'TB bạn đánh giá',
                       'TB giáo viên', 'Điểm tổng hợp', 'Số khảo sát', 'Sao khảo sát TB', 'Cập nhật'];
HEADERS[SH.LOG]     = ['Thời gian', 'Hành động', 'Khoá', 'Kết quả', 'Chi tiết'];
GROUPS.forEach(function (g) {
  HEADERS[SH.PEER[g.id]]    = ['Thời gian', 'Khoá', 'Mã khoá', 'Tên khoá', 'Buổi số', 'Tên buổi', 'Lớp',
                               'Mã người đánh giá', 'Người đánh giá', 'Mã bạn được ĐG', 'Bạn được đánh giá']
                               .concat(labels_(g.id), ['Trung bình', 'Nhận xét', 'Nguồn', 'Thiết bị']);
  HEADERS[SH.TEACHER[g.id]] = ['Thời gian', 'Khoá', 'Mã khoá', 'Tên khoá', 'Mã HS', 'Họ tên', 'Lớp', 'Giáo viên']
                               .concat(labels_(g.id), ['Trung bình', 'Nhận xét', 'Nguồn', 'Thiết bị']);
});

/* Tiêu đề câu hỏi Google Form */
var Q = {
  KHOA       : 'Khoá học',
  MA_HS      : 'Mã học sinh (nếu có)',
  HO_TEN     : 'Họ và tên',
  TRUONG     : 'Trường',
  LOP        : 'Lớp',
  BUOI       : 'Buổi học (số thứ tự)',
  SO_BUOI    : 'Số buổi đã học',
  THICH_NHAT : 'Phần em thích nhất',
  TONG_THE   : 'Đánh giá tổng thể khoá học',
  DO_KHO     : 'Độ khó của khoá học',
  GIOI_THIEU : 'Em sẽ giới thiệu khoá học cho bạn khác?',
  CAI_THIEN  : 'Mức cải thiện kỹ năng của em (0–100 %)',
  KY_NANG    : 'Kỹ năng em thấy tiến bộ nhất',
  DIEU_THICH : 'Điều em thích nhất',
  CAN_CAI    : 'Điều cần cải thiện',
  HOC_THEM   : 'Chủ đề em muốn học thêm',
  MA_NGUOI   : 'Mã của em (người đánh giá)',
  TEN_NGUOI  : 'Họ tên của em (người đánh giá)',
  MA_BAN     : 'Mã của bạn được đánh giá',
  TEN_BAN    : 'Họ tên bạn được đánh giá',
  NHAN_XET   : 'Nhận xét',
  GIAO_VIEN  : 'Giáo viên đánh giá',
  NX_GV      : 'Nhận xét của giáo viên'
};

/* ═════════════════ 1. TẠO / NÂNG CẤP HỆ THỐNG ═════════════════ */
function taoToanBo() {
  var folder = layHoacTaoThuMuc_();
  var ss = layHoacTaoBang_(folder);
  var out = ['📊 Bảng tính: ' + ss.getUrl()];

  napDuLieuTuWeb_(ss);                      // khoá học + buổi học + lớp + học sinh
  var forms = taoCacForm_(ss, folder);
  forms.forEach(function (f) { out.push('📝 ' + f.name + ': ' + f.publishedUrl); });

  caiTrigger_();
  capNhatTongHop();
  batBaoCaoHangTuan();                      // báo cáo tự động sáng thứ Hai
  out.push('📧 Báo cáo gửi về: ' + emailGiaoVien_());
  ghiLog_('taoToanBo', '', 'OK', out.join(' | '));

  var msg = ['✅ ĐÃ TẠO XONG HỆ THỐNG ĐA KHOÁ', '', 'Bảng tính:', '  ' + ss.getUrl(), '', 'Biểu mẫu:']
    .concat(forms.map(function (f) { return '  • ' + f.name + '\n    Điền: ' + f.publishedUrl; }))
    .concat(['', 'Nhớ: Triển khai > Quản lý triển khai > ✏️ > Phiên bản mới, để Web App dùng mã mới nhất.'])
    .join('\n');
  Logger.log(msg);
  try { SpreadsheetApp.getUi().alert(msg); } catch (e) {}
  return msg;
}

/** Migrate từ bản 1 khoá: dọn sheet/form cũ rồi dựng lại toàn bộ */
function nangCapV2() {
  var props = PropertiesService.getScriptProperties();
  var ss = bang_();
  SHEET_CU.forEach(function (n) {
    var sh = ss.getSheetByName(n);
    if (sh && sh.getLastRow() <= 1) ss.deleteSheet(sh);
  });
  // 3 form của bản v1 (thiếu câu hỏi "Khoá học") → bỏ vào thùng rác, tạo lại bản mới
  ['FORM_SURVEY', 'FORM_PEER', 'FORM_TEACHER'].forEach(function (k) {
    var id = props.getProperty(k);
    if (!id) return;
    try { DriveApp.getFileById(id).setTrashed(true); } catch (e) {}
    props.deleteProperty(k);
  });
  ghiLog_('nangCapV2', '', 'OK', 'Đã dọn bản v1');
  return taoToanBo();
}

function layHoacTaoThuMuc_() {
  if (CONFIG.FOLDER_ID) {
    try { return DriveApp.getFolderById(CONFIG.FOLDER_ID); }
    catch (e) { Logger.log('Không mở được FOLDER_ID: ' + e.message); }
  }
  var it = DriveApp.getFoldersByName(CONFIG.FOLDER_NAME);
  return it.hasNext() ? it.next() : DriveApp.createFolder(CONFIG.FOLDER_NAME);
}

function chuyenVaoThuMuc_(fileId, folder) {
  try {
    var f = DriveApp.getFileById(fileId);
    if (f.moveTo) { f.moveTo(folder); return; }
    folder.addFile(f); DriveApp.getRootFolder().removeFile(f);
  } catch (e) { Logger.log('Không chuyển được file ' + fileId + ': ' + e.message); }
}

function layHoacTaoBang_(folder) {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty('SS_ID'), ss = null;
  if (id) { try { ss = SpreadsheetApp.openById(id); } catch (e) { ss = null; } }
  if (!ss) {
    ss = SpreadsheetApp.create(CONFIG.SPREADSHEET);
    props.setProperty('SS_ID', ss.getId());
    chuyenVaoThuMuc_(ss.getId(), folder);
  }
  ss.setSpreadsheetTimeZone(CONFIG.TIMEZONE);
  Object.keys(HEADERS).forEach(function (name) { taoSheet_(ss, name, HEADERS[name]); });
  napTieuChi_(ss);
  return ss;
}

function taoSheet_(ss, name, headers) {
  var sh = ss.getSheetByName(name) || ss.insertSheet(name);
  var cur = sh.getRange(1, 1, 1, Math.max(sh.getLastColumn(), 1)).getValues()[0];
  if (cur.join('|') !== headers.join('|')) sh.getRange(1, 1, 1, headers.length).setValues([headers]);
  sh.getRange(1, 1, 1, headers.length)
    .setFontWeight('bold').setBackground('#245c46').setFontColor('#ffffff')
    .setVerticalAlignment('middle').setWrap(true);
  sh.setFrozenRows(1);
  sh.setRowHeight(1, 40);
  if (sh.getMaxColumns() > headers.length) sh.deleteColumns(headers.length + 1, sh.getMaxColumns() - headers.length);
  return sh;
}

function napTieuChi_(ss) {
  var rows = [];
  GROUPS.forEach(function (g) {
    g.criteria.forEach(function (c) { rows.push([g.name, c.id, c.label, c.icon, c.desc]); });
  });
  ghiDe_(ss.getSheetByName(SH.CRIT), rows);
}

/* ═════════════════ 2. NẠP DỮ LIỆU NỀN ═════════════════ */
function napDuLieuTuWeb() { return napDuLieuTuWeb_(bang_()); }

function napDuLieuTuWeb_(ss) {
  var dem = { courses: 0, sessions: 0, classes: 0, students: 0 };
  var kc = taiJson_(CONFIG.COURSES_URL);
  if (kc && kc.courses) dem = luuKhoaHoc_(ss, kc.courses);
  var rs = taiJson_(CONFIG.ROSTER_URL);
  if (rs) {
    var d2 = luuDanhSach_(ss, rs);
    dem.classes = d2.classes; dem.students = d2.students;
  }
  ghiLog_('napDuLieuTuWeb', '', 'OK', JSON.stringify(dem));
  Logger.log('Đã nạp: ' + JSON.stringify(dem));
  return dem;
}

function taiJson_(url) {
  var res = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  if (res.getResponseCode() !== 200) { Logger.log('Không tải được ' + url); return null; }
  try { return JSON.parse(res.getContentText()); } catch (e) { return null; }
}

function luuKhoaHoc_(ss, courses) {
  var rowsC = [], rowsS = [];
  courses.forEach(function (c) {
    rowsC.push([c.id, c.title, c.icon || '', c.group || 'stem', (c.sessions || []).length, c.docPath || '']);
    (c.sessions || []).forEach(function (s) { rowsS.push([c.id, s.id, s.title, s.phase || 1]); });
  });
  ghiDe_(ss.getSheetByName(SH.COURSE), rowsC);
  ghiDe_(ss.getSheetByName(SH.SESSION), rowsS);
  return { courses: rowsC.length, sessions: rowsS.length };
}

function luuDanhSach_(ss, db) {
  var dem = { classes: 0, students: 0 };
  if (db.classes && db.classes.length) {
    ghiDe_(ss.getSheetByName(SH.CLASS), db.classes.map(function (c) {
      return [c.id, c.name, c.teacher || '', c.room || '', c.schedule || ''];
    }));
    dem.classes = db.classes.length;
  }
  if (db.students && db.students.length) {
    var now = new Date();
    ghiDe_(ss.getSheetByName(SH.STUDENT), db.students.map(function (s) {
      return [s.id, s.name, s.classId, s.avatar || '🧑', now];
    }));
    dem.students = db.students.length;
  }
  if (db.courses && db.courses.length) luuKhoaHoc_(ss, db.courses);
  return dem;
}

function ghiDe_(sh, rows) {
  if (!sh) return;
  if (sh.getLastRow() > 1) sh.getRange(2, 1, sh.getLastRow() - 1, sh.getLastColumn()).clearContent();
  if (rows.length) sh.getRange(2, 1, rows.length, rows[0].length).setValues(rows);
}

/* ═════════════════ 3. TẠO 7 GOOGLE FORM ═════════════════ */
function taoCacForm_(ss, folder) {
  var props = PropertiesService.getScriptProperties();
  var khoa = docCot_(ss, SH.COURSE, 1, 4);          // [mã, tên, icon, nhóm]
  var lop  = docCot_(ss, SH.CLASS, 1, 2);
  var tenLop = lop.length ? lop.map(function (r) { return r[0] + ' — ' + r[1]; }) : ['8A', '8B', '9A', '10A'];
  var ket = [];

  var moiKhoa = khoa.length ? khoa.map(function (r) { return r[0] + ' — ' + r[2] + ' ' + r[1]; })
                            : ['stem-microbit — 🤖 STEM micro:bit'];
  ket.push(dungForm_('FORM_SURVEY', '🧪 Khảo sát học viên — Tất cả khoá học',
    'Ý kiến của em giúp thầy cô cải thiện khoá học. Chọn đúng khoá em đang học.',
    function (f) {
      f.addListItem().setTitle(Q.KHOA).setChoiceValues(moiKhoa).setRequired(true);
      f.addTextItem().setTitle(Q.MA_HS).setHelpText('Ví dụ: s001 — bỏ trống nếu không nhớ');
      f.addTextItem().setTitle(Q.HO_TEN).setRequired(true);
      f.addTextItem().setTitle(Q.TRUONG);
      f.addListItem().setTitle(Q.LOP).setChoiceValues(tenLop).setRequired(true);
      f.addTextItem().setTitle(Q.BUOI).setHelpText('Nhập số buổi/tuần, ví dụ 5')
        .setValidation(FormApp.createTextValidation().requireNumberBetween(0, 60).build());
      f.addTextItem().setTitle(Q.SO_BUOI)
        .setValidation(FormApp.createTextValidation().requireNumberBetween(0, 60).build());
      f.addCheckboxItem().setTitle(Q.THICH_NHAT)
        .setChoiceValues(['Lý thuyết trên lớp', 'Thực hành / thí nghiệm', 'Bài tập & luyện đề',
                          'Làm việc nhóm', 'Dự án cuối khoá', 'Ứng dụng máy tính / lập trình']);
      f.addScaleItem().setTitle(Q.TONG_THE).setBounds(1, 5).setLabels('Rất kém', 'Xuất sắc').setRequired(true);
      f.addMultipleChoiceItem().setTitle(Q.DO_KHO).setChoiceValues(['Quá dễ', 'Vừa phải', 'Hơi khó', 'Quá khó']);
      f.addMultipleChoiceItem().setTitle(Q.GIOI_THIEU).setChoiceValues(['Chắc chắn', 'Có thể', 'Không']);
      f.addTextItem().setTitle(Q.CAI_THIEN)
        .setValidation(FormApp.createTextValidation().requireNumberBetween(0, 100).build());
      f.addCheckboxItem().setTitle(Q.KY_NANG)
        .setChoiceValues(['Tư duy giải quyết vấn đề', 'Kiến thức chuyên môn', 'Làm việc nhóm',
                          'Sáng tạo', 'Thực hành', 'Thuyết trình']);
      f.addParagraphTextItem().setTitle(Q.DIEU_THICH);
      f.addParagraphTextItem().setTitle(Q.CAN_CAI);
      f.addTextItem().setTitle(Q.HOC_THEM);
    }, ss, folder, props));

  GROUPS.forEach(function (g) {
    var moiKhoaNhom = khoa.filter(function (r) { return r[3] === g.id; })
                          .map(function (r) { return r[0] + ' — ' + r[2] + ' ' + r[1]; });
    if (!moiKhoaNhom.length) moiKhoaNhom = ['(chưa có khoá)'];

    ket.push(dungForm_('FORM_PEER_' + g.id.toUpperCase(), '🔄 Đánh giá đồng đẳng — ' + g.name,
      'Chấm trung thực và tôn trọng. Mỗi phiếu dành cho MỘT bạn trong một buổi học.',
      function (f) {
        f.addListItem().setTitle(Q.KHOA).setChoiceValues(moiKhoaNhom).setRequired(true);
        f.addTextItem().setTitle(Q.BUOI)
          .setValidation(FormApp.createTextValidation().requireNumberBetween(1, 60).build()).setRequired(true);
        f.addListItem().setTitle(Q.LOP).setChoiceValues(tenLop).setRequired(true);
        f.addTextItem().setTitle(Q.MA_NGUOI);
        f.addTextItem().setTitle(Q.TEN_NGUOI).setRequired(true);
        f.addTextItem().setTitle(Q.MA_BAN);
        f.addTextItem().setTitle(Q.TEN_BAN).setRequired(true);
        g.criteria.forEach(function (c) {
          f.addScaleItem().setTitle(c.icon + ' ' + c.label).setHelpText(c.desc)
            .setBounds(1, 5).setLabels('Cần cố gắng', 'Xuất sắc').setRequired(true);
        });
        f.addParagraphTextItem().setTitle(Q.NHAN_XET).setHelpText('Một điểm mạnh + một góp ý cho bạn');
      }, ss, folder, props));

    ket.push(dungForm_('FORM_TEACHER_' + g.id.toUpperCase(), '👩‍🏫 Phiếu đánh giá của giáo viên — ' + g.name,
      'Giáo viên chấm từng học sinh theo 6 tiêu chí của nhóm môn.',
      function (f) {
        f.addListItem().setTitle(Q.KHOA).setChoiceValues(moiKhoaNhom).setRequired(true);
        f.addTextItem().setTitle(Q.GIAO_VIEN).setRequired(true);
        f.addListItem().setTitle(Q.LOP).setChoiceValues(tenLop).setRequired(true);
        f.addTextItem().setTitle(Q.MA_HS);
        f.addTextItem().setTitle(Q.HO_TEN).setRequired(true);
        g.criteria.forEach(function (c) {
          f.addScaleItem().setTitle(c.icon + ' ' + c.label).setHelpText(c.desc)
            .setBounds(1, 5).setLabels('Cần cố gắng', 'Xuất sắc').setRequired(true);
        });
        f.addParagraphTextItem().setTitle(Q.NX_GV);
      }, ss, folder, props));
  });

  return ket;
}

function dungForm_(propKey, title, desc, build, ss, folder, props) {
  var id = props.getProperty(propKey), form = null;
  if (id) { try { form = FormApp.openById(id); } catch (e) { form = null; } }
  if (!form) {
    form = FormApp.create(title);
    props.setProperty(propKey, form.getId());
    build(form);
    chuyenVaoThuMuc_(form.getId(), folder);
  }
  form.setTitle(title).setDescription(desc)
      .setCollectEmail(false).setAllowResponseEdits(false)
      .setConfirmationMessage('✅ Đã ghi nhận. Cảm ơn em! — STEM Portal');
  try {
    if (form.getDestinationId() !== ss.getId()) form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
  } catch (e) {
    try { form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId()); } catch (e2) {}
  }
  return { key: propKey, name: title, id: form.getId(),
           publishedUrl: form.getPublishedUrl(), editUrl: form.getEditUrl() };
}

function docCot_(ss, sheetName, from, to) {
  var sh = ss.getSheetByName(sheetName);
  if (!sh || sh.getLastRow() < 2) return [];
  return sh.getRange(2, from, sh.getLastRow() - 1, to - from + 1).getValues()
           .filter(function (r) { return String(r[0]).trim() !== ''; });
}

/* ═════════════════ 4. TRIGGER & FORM SUBMIT ═════════════════ */
function danhSachPropForm_() {
  var ks = ['FORM_SURVEY'];
  GROUPS.forEach(function (g) {
    ks.push('FORM_PEER_' + g.id.toUpperCase());
    ks.push('FORM_TEACHER_' + g.id.toUpperCase());
  });
  return ks;
}

function caiTrigger_() {
  var props = PropertiesService.getScriptProperties();
  var có = ScriptApp.getProjectTriggers().map(function (t) {
    return t.getHandlerFunction() + '|' + t.getTriggerSourceId();
  });
  danhSachPropForm_().forEach(function (k) {
    var id = props.getProperty(k);
    if (!id || có.indexOf('xuLyFormSubmit|' + id) >= 0) return;
    ScriptApp.newTrigger('xuLyFormSubmit').forForm(FormApp.openById(id)).onFormSubmit().create();
  });
  if (!có.filter(function (x) { return x.indexOf('capNhatTongHop') === 0; }).length) {
    ScriptApp.newTrigger('capNhatTongHop').timeBased().everyHours(6).create();
  }
}

function xuLyFormSubmit(e) {
  try {
    var props = PropertiesService.getScriptProperties();
    var formId = e.source.getId(), ans = {};
    e.response.getItemResponses().forEach(function (ir) { ans[ir.getItem().getTitle()] = ir.getResponse(); });
    var tg = e.response.getTimestamp() || new Date();
    var kh = tachKhoa_(ans[Q.KHOA]);

    if (formId === props.getProperty('FORM_SURVEY')) {
      luuKhaoSat_({
        id: 'form_' + e.response.getId(), courseId: kh.id, courseTitle: kh.title,
        studentId: ans[Q.MA_HS] || '', studentName: ans[Q.HO_TEN] || '',
        school: ans[Q.TRUONG] || '', classId: tachMa_(ans[Q.LOP]),
        sessionId: ans[Q.BUOI] || '', sessions: ans[Q.SO_BUOI] || '',
        fav: ans[Q.THICH_NHAT] || [], overall: ans[Q.TONG_THE] || '',
        difficulty: ans[Q.DO_KHO] || '', recommend: ans[Q.GIOI_THIEU] || '',
        skill: ans[Q.CAI_THIEN] || '', skill_gained: ans[Q.KY_NANG] || [],
        best: ans[Q.DIEU_THICH] || '', improve: ans[Q.CAN_CAI] || '',
        topic: ans[Q.HOC_THEM] || '', submittedAt: tg
      }, 'Google Form', '');
      ghiLog_('formSubmit', 'survey', 'OK', kh.id);
      return;
    }
    for (var i = 0; i < GROUPS.length; i++) {
      var g = GROUPS[i], G = g.id.toUpperCase();
      if (formId === props.getProperty('FORM_PEER_' + G)) {
        luuDanhGiaDongDang_({
          courseId: kh.id, courseTitle: kh.title, sessionId: ans[Q.BUOI] || '',
          classId: tachMa_(ans[Q.LOP]), raterId: ans[Q.MA_NGUOI] || '', raterName: ans[Q.TEN_NGUOI] || '',
          targetId: ans[Q.MA_BAN] || '', targetName: ans[Q.TEN_BAN] || '',
          scores: layDiem_(ans, g), note: ans[Q.NHAN_XET] || '', savedAt: tg
        }, 'Google Form', '');
        ghiLog_('formSubmit', 'peer:' + g.id, 'OK', kh.id);
        return;
      }
      if (formId === props.getProperty('FORM_TEACHER_' + G)) {
        luuDiemGiaoVien_({
          courseId: kh.id, courseTitle: kh.title, studentId: ans[Q.MA_HS] || '',
          studentName: ans[Q.HO_TEN] || '', classId: tachMa_(ans[Q.LOP]),
          teacher: ans[Q.GIAO_VIEN] || '', scores: layDiem_(ans, g),
          note: ans[Q.NX_GV] || '', updatedAt: tg
        }, 'Google Form', '');
        ghiLog_('formSubmit', 'teacher:' + g.id, 'OK', kh.id);
        return;
      }
    }
  } catch (err) {
    ghiLog_('formSubmit', '', 'LỖI', err.message);
  }
}

function layDiem_(ans, g) {
  var s = {};
  g.criteria.forEach(function (c) {
    var v = ans[c.icon + ' ' + c.label];
    if (v !== undefined && v !== '') s[c.id] = Number(v);
  });
  return s;
}
function tachMa_(v) { return String(v || '').split('—')[0].trim(); }
function tachKhoa_(v) {
  var t = String(v || ''), p = t.split('—');
  return { id: (p[0] || '').trim(), title: (p[1] || '').trim() };
}

/* ═════════════════ 5. GHI DỮ LIỆU ═════════════════ */
function bang_() {
  var id = PropertiesService.getScriptProperties().getProperty('SS_ID');
  if (!id) throw new Error('Chưa chạy taoToanBo() — bảng tính chưa tồn tại.');
  return SpreadsheetApp.openById(id);
}

/** Nhóm tiêu chí của một khoá (đọc sheet Khoá học, có cache) */
var _cacheNhom = null;
function nhomCuaKhoa_(courseId) {
  if (!_cacheNhom) {
    _cacheNhom = {};
    docCot_(bang_(), SH.COURSE, 1, 4).forEach(function (r) { _cacheNhom[r[0]] = r[3]; });
  }
  return _cacheNhom[courseId] || 'stem';
}
function tenKhoa_(courseId, fallback) {
  if (fallback) return fallback;
  var rows = docCot_(bang_(), SH.COURSE, 1, 2);
  for (var i = 0; i < rows.length; i++) if (rows[i][0] === courseId) return rows[i][1];
  return '';
}

function upsert_(sheetName, khoa, row) {
  var ss = bang_(), sh = ss.getSheetByName(sheetName) || taoSheet_(ss, sheetName, HEADERS[sheetName]);
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var last = sh.getLastRow(), dong = 0;
    if (khoa && last > 1) {
      var keys = sh.getRange(2, 2, last - 1, 1).getValues();
      for (var i = 0; i < keys.length; i++) if (String(keys[i][0]) === String(khoa)) { dong = i + 2; break; }
    }
    if (!dong) dong = last + 1;
    sh.getRange(dong, 1, 1, row.length).setValues([row]);
    return { sheet: sheetName, row: dong, updated: dong <= last };
  } finally { lock.releaseLock(); }
}

function tb_(diem) {
  var so = diem.filter(function (v) { return v !== '' && v !== null; }).map(Number);
  return so.length ? Math.round(so.reduce(function (a, b) { return a + b; }, 0) / so.length * 10) / 10 : '';
}

function luuKhaoSat_(p, nguon, thietBi) {
  var cid = p.courseId || 'stem-microbit';
  var khoa = p.id || ('sv_' + cid + '_' + (p.studentId || p.studentName) + '_' + (p.sessionId || ''));
  var row = [
    p.submittedAt ? new Date(p.submittedAt) : new Date(), khoa,
    cid, tenKhoa_(cid, p.courseTitle),
    p.studentId || '', p.studentName || '', p.school || '', p.classId || p.grade || '',
    p.sessionId || '', p.sessionTitle || '', p.sessions || '',
    gop_(p.fav), p.overall || '', p.difficulty || '', p.recommend || '',
    p.skill || '', gop_(p.skill_gained), p.best || '', p.improve || '', p.topic || '',
    nguon || 'Web', thietBi || ''
  ];
  return upsert_(SH.SURVEY, khoa, row);
}

function luuDanhGiaDongDang_(p, nguon, thietBi) {
  var cid = p.courseId || 'stem-microbit';
  var gid = p.group || nhomCuaKhoa_(cid);
  var khoa = [cid, p.raterId || p.raterName, 'b' + (p.sessionId || 0), p.targetId || p.targetName].join('|');
  var diem = ids_(gid).map(function (id) { return (p.scores && p.scores[id]) || ''; });
  var row = [
    p.savedAt ? new Date(p.savedAt) : new Date(), khoa, cid, tenKhoa_(cid, p.courseTitle),
    p.sessionId || '', p.sessionTitle || '', p.classId || '',
    p.raterId || '', p.raterName || '', p.targetId || '', p.targetName || ''
  ].concat(diem, [tb_(diem), p.note || '', nguon || 'Web', thietBi || '']);
  return upsert_(SH.PEER[gid], khoa, row);
}

function luuDiemGiaoVien_(p, nguon, thietBi) {
  var cid = p.courseId || 'stem-microbit';
  var gid = p.group || nhomCuaKhoa_(cid);
  var khoa = ['gv', cid, p.studentId || p.studentName, p.teacher || ''].join('|');
  var diem = ids_(gid).map(function (id) { return (p.scores && p.scores[id]) || ''; });
  var row = [
    p.updatedAt ? new Date(p.updatedAt) : new Date(), khoa, cid, tenKhoa_(cid, p.courseTitle),
    p.studentId || '', p.studentName || '', p.classId || '', p.teacher || ''
  ].concat(diem, [tb_(diem), p.note || '', nguon || 'Web', thietBi || '']);
  return upsert_(SH.TEACHER[gid], khoa, row);
}

function gop_(v) { return Array.isArray(v) ? v.join(', ') : (v || ''); }

/* ═════════════════ 6. WEB APP: POST ═════════════════ */
function doPost(e) {
  var body = {};
  try { body = JSON.parse(e.postData.contents); }
  catch (err) { return traVe_({ ok: false, error: 'JSON không hợp lệ' }); }
  if (CONFIG.TOKEN && body.token !== CONFIG.TOKEN) return traVe_({ ok: false, error: 'Sai mã bảo mật' });
  try {
    var ket = xuLyGoi_(body);
    ghiLog_('POST:' + body.type, body.uid || '', 'OK', JSON.stringify(ket).slice(0, 400));
    return traVe_({ ok: true, result: ket });
  } catch (err) {
    ghiLog_('POST:' + (body.type || '?'), body.uid || '', 'LỖI', err.message);
    return traVe_({ ok: false, error: err.message });
  }
}

function xuLyGoi_(body) {
  var type = body.type, p = body.payload || {}, dev = body.device || '';
  switch (type) {
    case 'survey':        return luuKhaoSat_(p, 'Web', dev);
    case 'peer_eval':     return luuDanhGiaDongDang_(p, 'Web', dev);
    case 'peer_eval_set':
      return (p.items || []).map(function (x) {
        return luuDanhGiaDongDang_({
          courseId: p.courseId, courseTitle: p.courseTitle, group: p.group,
          sessionId: p.sessionId, sessionTitle: p.sessionTitle, classId: p.classId,
          raterId: p.raterId, raterName: p.raterName,
          targetId: x.targetId, targetName: x.targetName,
          scores: x.scores, note: x.note, savedAt: x.savedAt
        }, 'Web', dev);
      });
    case 'teacher_grade': return luuDiemGiaoVien_(p, 'Web', dev);
    case 'roster':        return luuDanhSach_(bang_(), p);
    case 'courses':       return luuKhoaHoc_(bang_(), p.courses || []);
    case 'batch':
      return (body.items || []).map(function (it) {
        try { return { type: it.type, ok: true, r: xuLyGoi_({ type: it.type, payload: it.payload, device: it.device }) }; }
        catch (err) { return { type: it.type, ok: false, error: err.message }; }
      });
    case 'set_email':     return datEmailGiaoVien(p.email);
    case 'send_report':   return guiBaoCaoTongHop(p.email, p.courseId);
    case 'ping':          return { pong: true };
    default: throw new Error('Loại dữ liệu không hỗ trợ: ' + type);
  }
}

/* ═════════════════ 7. WEB APP: GET ═════════════════ */
function doGet(e) {
  var p = (e && e.parameter) || {}, action = p.action || 'ping', kq;
  try {
    switch (action) {
      case 'ping':      kq = { ok: true, service: 'STEM Portal API v2', time: new Date().toISOString(), config: thongTinCauHinh_() }; break;
      case 'config':    kq = { ok: true, config: thongTinCauHinh_() }; break;
      case 'roster':    kq = { ok: true, data: docDanhSach_(p.course) }; break;
      case 'courses':   kq = { ok: true, data: docKhoaHoc_() }; break;
      case 'surveys':   kq = { ok: true, data: locKhoa_(docSheet_(SH.SURVEY, p.limit), p.course) }; break;
      case 'peer':      kq = { ok: true, data: gopNhom_(SH.PEER, p) }; break;
      case 'teacher':   kq = { ok: true, data: gopNhom_(SH.TEACHER, p) }; break;
      case 'dashboard': kq = { ok: true, data: locKhoa_(docSheet_(SH.DASH, p.limit), p.course) }; break;
      case 'summary':   kq = { ok: true, data: tomTat_() }; break;
      case 'rebuild':   capNhatTongHop(); kq = { ok: true, data: 'Đã cập nhật Tổng hợp' }; break;
      case 'reload':    kq = { ok: true, data: napDuLieuTuWeb_(bang_()) }; break;
      case 'email':     kq = { ok: true, data: { email: emailGiaoVien_(), weekly: lichBaoCao_() } }; break;
      case 'set_email': kq = { ok: true, data: datEmailGiaoVien(p.email) }; break;
      case 'report':    kq = { ok: true, data: guiBaoCaoTongHop(p.email, p.course) }; break;
      case 'weekly':    kq = { ok: true, data: (p.on === '0' ? tatBaoCaoHangTuan() : batBaoCaoHangTuan()) }; break;
      default: kq = { ok: false, error: 'Hành động không hỗ trợ: ' + action };
    }
  } catch (err) { kq = { ok: false, error: err.message }; }
  return traVe_(kq, p.callback);
}

function traVe_(obj, callback) {
  var txt = JSON.stringify(obj);
  if (callback) return ContentService.createTextOutput(callback + '(' + txt + ');')
                                     .setMimeType(ContentService.MimeType.JAVASCRIPT);
  return ContentService.createTextOutput(txt).setMimeType(ContentService.MimeType.JSON);
}

/** Gộp 3 sheet theo nhóm, kèm cột "Nhóm" */
function gopNhom_(map, p) {
  var ra = [];
  Object.keys(map).forEach(function (gid) {
    if (p.group && p.group !== gid) return;
    docSheet_(map[gid], p.limit).forEach(function (r) { r['Nhóm'] = gid; ra.push(r); });
  });
  return locKhoa_(ra, p.course);
}
function locKhoa_(rows, course) {
  if (!course) return rows;
  return rows.filter(function (r) { return r['Mã khoá'] === course; });
}

function thongTinCauHinh_() {
  var props = PropertiesService.getScriptProperties();
  var ra = { spreadsheetId: props.getProperty('SS_ID') || '', forms: {} };
  if (ra.spreadsheetId) ra.spreadsheetUrl = 'https://docs.google.com/spreadsheets/d/' + ra.spreadsheetId + '/edit';
  danhSachPropForm_().forEach(function (k) {
    var id = props.getProperty(k);
    if (!id) return;
    try {
      var f = FormApp.openById(id);
      ra.forms[k] = { title: f.getTitle(), url: f.getPublishedUrl(), editUrl: f.getEditUrl() };
    } catch (e) {}
  });
  return ra;
}

function docSheet_(name, limit) {
  var sh = bang_().getSheetByName(name);
  if (!sh || sh.getLastRow() < 2) return [];
  var head = sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0];
  var n = sh.getLastRow() - 1, lim = Math.min(Number(limit) || n, n);
  return sh.getRange(sh.getLastRow() - lim + 1, 1, lim, sh.getLastColumn()).getValues().map(function (r) {
    var o = {};
    head.forEach(function (h, i) { o[h] = (r[i] instanceof Date) ? r[i].toISOString() : r[i]; });
    return o;
  });
}

function docKhoaHoc_() {
  var ss = bang_();
  var buoi = {};
  docCot_(ss, SH.SESSION, 1, 4).forEach(function (r) {
    (buoi[r[0]] = buoi[r[0]] || []).push({ id: Number(r[1]), title: r[2], phase: Number(r[3]) || 1 });
  });
  return {
    criteriaGroups: GROUPS,
    courses: docCot_(ss, SH.COURSE, 1, 6).map(function (r) {
      return { id: r[0], title: r[1], icon: r[2], group: r[3], docPath: r[5], sessions: buoi[r[0]] || [] };
    })
  };
}

function docDanhSach_(courseId) {
  var ss = bang_(), kh = docKhoaHoc_();
  var ra = {
    classes: docCot_(ss, SH.CLASS, 1, 5).map(function (r) {
      return { id: r[0], name: r[1], teacher: r[2], room: r[3], schedule: r[4] };
    }),
    students: docCot_(ss, SH.STUDENT, 1, 4).map(function (r) {
      return { id: r[0], name: r[1], classId: r[2], avatar: r[3] || '🧑' };
    }),
    courses: kh.courses, criteriaGroups: GROUPS
  };
  var c = courseId && kh.courses.filter(function (x) { return x.id === courseId; })[0];
  ra.sessions = c ? c.sessions : (kh.courses[0] ? kh.courses[0].sessions : []);
  ra.criteria = nhom_(c ? c.group : 'stem').criteria;
  return ra;
}

function tomTat_() {
  var ss = bang_();
  var dem = function (n) { var s = ss.getSheetByName(n); return s ? Math.max(0, s.getLastRow() - 1) : 0; };
  var peer = 0, gv = 0;
  GROUPS.forEach(function (g) { peer += dem(SH.PEER[g.id]); gv += dem(SH.TEACHER[g.id]); });
  return {
    khaoSat: dem(SH.SURVEY), dongDang: peer, giaoVien: gv,
    hocSinh: dem(SH.STUDENT), lop: dem(SH.CLASS), khoaHoc: dem(SH.COURSE), buoiHoc: dem(SH.SESSION),
    capNhat: Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'dd/MM/yyyy HH:mm')
  };
}

/* ═════════════════ 8. SHEET TỔNG HỢP (học sinh × khoá) ═════════════════ */
function capNhatTongHop() {
  var ss = bang_();
  var hs = {}; docCot_(ss, SH.STUDENT, 1, 3).forEach(function (r) { hs[r[0]] = { name: r[1], classId: r[2] }; });
  var ten = {}; docCot_(ss, SH.COURSE, 1, 2).forEach(function (r) { ten[r[0]] = r[1]; });

  var map = {};   // key = courseId|studentKey
  var lay = function (cid, ma, tenHs) {
    var id = ma || tenHs || '?';
    var k = cid + '|' + id;
    if (!map[k]) map[k] = { courseId: cid, id: ma || '', name: tenHs || (hs[ma] ? hs[ma].name : ''),
                            classId: hs[ma] ? hs[ma].classId : '', peer: [], gv: [], sv: [] };
    if (!map[k].name && hs[ma]) map[k].name = hs[ma].name;
    return map[k];
  };

  GROUPS.forEach(function (g) {
    docSheet_(SH.PEER[g.id]).forEach(function (r) {
      var o = lay(r['Mã khoá'], r['Mã bạn được ĐG'], r['Bạn được đánh giá']);
      if (r['Trung bình'] !== '') o.peer.push(Number(r['Trung bình']));
    });
    docSheet_(SH.TEACHER[g.id]).forEach(function (r) {
      var o = lay(r['Mã khoá'], r['Mã HS'], r['Họ tên']);
      if (r['Trung bình'] !== '') o.gv.push(Number(r['Trung bình']));
    });
  });
  docSheet_(SH.SURVEY).forEach(function (r) {
    var o = lay(r['Mã khoá'], r['Mã HS'], r['Họ tên']);
    o.sv.push(Number(r['Đánh giá (1-5)']) || 0);
  });

  var now = new Date();
  var rows = Object.keys(map).map(function (k) {
    var o = map[k], p = tb_(o.peer), g = tb_(o.gv);
    var tong = (p !== '' && g !== '') ? Math.round((p * 0.4 + g * 0.6) * 10) / 10 : (g !== '' ? g : p);
    return [o.courseId, ten[o.courseId] || '', o.id, o.name, o.classId,
            o.peer.length, p, g, tong, o.sv.length, tb_(o.sv.filter(Boolean)), now];
  }).sort(function (a, b) { return String(a[0] + a[4] + a[3]).localeCompare(String(b[0] + b[4] + b[3]), 'vi'); });

  var sh = ss.getSheetByName(SH.DASH) || taoSheet_(ss, SH.DASH, HEADERS[SH.DASH]);
  ghiDe_(sh, rows);
  if (rows.length) {
    sh.getRange(2, 7, rows.length, 3).setNumberFormat('0.0');
    sh.getRange(2, 12, rows.length, 1).setNumberFormat('dd/MM/yyyy HH:mm');
  }
  ghiLog_('capNhatTongHop', '', 'OK', rows.length + ' dòng');
  return rows.length;
}

/* ═════════════════ 9. BÁO CÁO QUA EMAIL ═════════════════ */
function emailGiaoVien_() {
  return PropertiesService.getScriptProperties().getProperty('TEACHER_EMAIL') || CONFIG.TEACHER_EMAIL;
}

/** Đặt email nhận báo cáo (chạy tay hoặc gọi từ trang ket-noi.html) */
function datEmailGiaoVien(email) {
  email = String(email || '').trim();
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) throw new Error('Email không hợp lệ: ' + email);
  PropertiesService.getScriptProperties().setProperty('TEACHER_EMAIL', email);
  ghiLog_('datEmailGiaoVien', '', 'OK', email);
  return { email: email };
}

/** Bật/tắt lịch gửi báo cáo hằng tuần (sáng thứ Hai) */
function batBaoCaoHangTuan() {
  if (!ScriptApp.getProjectTriggers().filter(function (t) {
        return t.getHandlerFunction() === 'guiBaoCaoDinhKy'; }).length) {
    ScriptApp.newTrigger('guiBaoCaoDinhKy').timeBased()
      .onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(7).create();
  }
  return { weekly: true, email: emailGiaoVien_() };
}
function tatBaoCaoHangTuan() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'guiBaoCaoDinhKy') ScriptApp.deleteTrigger(t);
  });
  return { weekly: false };
}
function lichBaoCao_() {
  return ScriptApp.getProjectTriggers().filter(function (t) {
    return t.getHandlerFunction() === 'guiBaoCaoDinhKy'; }).length > 0;
}
function guiBaoCaoDinhKy() { return guiBaoCaoTongHop(); }

/** Gửi báo cáo tổng hợp. email/courseId để trống = dùng mặc định / tất cả khoá */
function guiBaoCaoTongHop(email, courseId) {
  email = email || emailGiaoVien_();
  capNhatTongHop();

  var tt = tomTat_();
  var dash = docSheet_(SH.DASH);
  if (courseId) dash = dash.filter(function (r) { return r['Mã khoá'] === courseId; });

  var theoKhoa = {};
  dash.forEach(function (r) {
    var k = r['Mã khoá'] || '—';
    var o = theoKhoa[k] || (theoKhoa[k] = { ten: r['Tên khoá'] || k, hs: 0, peer: [], gv: [], sv: 0 });
    o.hs++;
    if (r['TB bạn đánh giá'] !== '') o.peer.push(Number(r['TB bạn đánh giá']));
    if (r['TB giáo viên'] !== '')   o.gv.push(Number(r['TB giáo viên']));
    o.sv += Number(r['Số khảo sát']) || 0;
  });

  var xepHang = dash.filter(function (r) { return r['Điểm tổng hợp'] !== ''; })
                    .sort(function (a, b) { return Number(b['Điểm tổng hợp']) - Number(a['Điểm tổng hợp']); });
  var top = xepHang.slice(0, 5);
  var canHoTro = xepHang.slice(-5).reverse().filter(function (r) { return Number(r['Điểm tổng hợp']) < 3.5; });

  var phanHoi = docSheet_(SH.SURVEY, 5).reverse().filter(function (r) {
    return !courseId || r['Mã khoá'] === courseId;
  });

  var ngay = Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'dd/MM/yyyy HH:mm');
  var css = 'style="border:1px solid #dce5df;padding:7px 10px;text-align:left;font-size:13px"';
  var th  = 'style="border:1px solid #dce5df;padding:7px 10px;text-align:left;font-size:12px;' +
            'background:#245c46;color:#fff;font-weight:700"';

  var html = [
    '<div style="font-family:Inter,Arial,sans-serif;color:#18251f;max-width:760px">',
    '<h2 style="margin:0 0 4px">📊 Báo cáo tổng hợp — STEM Portal</h2>',
    '<p style="color:#6a7770;margin:0 0 18px">Cập nhật ' + ngay +
      (courseId ? ' · Khoá: ' + courseId : ' · Tất cả khoá học') + '</p>',
    '<table style="border-collapse:collapse;margin-bottom:20px">',
    '<tr><td ' + css + '>🎓 Khoá học</td><td ' + css + '><b>' + tt.khoaHoc + '</b></td>',
    '<td ' + css + '>📅 Buổi học</td><td ' + css + '><b>' + tt.buoiHoc + '</b></td></tr>',
    '<tr><td ' + css + '>👥 Học sinh</td><td ' + css + '><b>' + tt.hocSinh + '</b></td>',
    '<td ' + css + '>🏫 Lớp</td><td ' + css + '><b>' + tt.lop + '</b></td></tr>',
    '<tr><td ' + css + '>🧪 Phiếu khảo sát</td><td ' + css + '><b>' + tt.khaoSat + '</b></td>',
    '<td ' + css + '>🔄 Phiếu đồng đẳng</td><td ' + css + '><b>' + tt.dongDang + '</b></td></tr>',
    '<tr><td ' + css + '>👩‍🏫 Phiếu giáo viên</td><td ' + css + '><b>' + tt.giaoVien + '</b></td>',
    '<td ' + css + '></td><td ' + css + '></td></tr>',
    '</table>'
  ];

  var kA = Object.keys(theoKhoa);
  if (kA.length) {
    html.push('<h3 style="margin:18px 0 8px">📚 Theo khoá học</h3>',
      '<table style="border-collapse:collapse;width:100%"><tr>',
      '<th ' + th + '>Khoá học</th><th ' + th + '>Học sinh</th><th ' + th + '>TB bạn ĐG</th>',
      '<th ' + th + '>TB giáo viên</th><th ' + th + '>Khảo sát</th></tr>');
    kA.forEach(function (k) {
      var o = theoKhoa[k];
      html.push('<tr><td ' + css + '>' + o.ten + '</td><td ' + css + '>' + o.hs + '</td><td ' + css + '>' +
        (tb_(o.peer) || '—') + '</td><td ' + css + '>' + (tb_(o.gv) || '—') + '</td><td ' + css + '>' + o.sv + '</td></tr>');
    });
    html.push('</table>');
  }

  if (top.length) {
    html.push('<h3 style="margin:18px 0 8px">🏆 Top 5 điểm tổng hợp</h3>',
      '<table style="border-collapse:collapse;width:100%"><tr>',
      '<th ' + th + '>Học sinh</th><th ' + th + '>Lớp</th><th ' + th + '>Khoá</th><th ' + th + '>Điểm</th></tr>');
    top.forEach(function (r) {
      html.push('<tr><td ' + css + '>' + (r['Họ tên'] || r['Mã HS']) + '</td><td ' + css + '>' + r['Lớp'] +
        '</td><td ' + css + '>' + r['Tên khoá'] + '</td><td ' + css + '><b>' + r['Điểm tổng hợp'] + '</b>/5</td></tr>');
    });
    html.push('</table>');
  }

  if (canHoTro.length) {
    html.push('<h3 style="margin:18px 0 8px">🎯 Cần hỗ trợ thêm (dưới 3.5/5)</h3>',
      '<table style="border-collapse:collapse;width:100%"><tr>',
      '<th ' + th + '>Học sinh</th><th ' + th + '>Lớp</th><th ' + th + '>Khoá</th><th ' + th + '>Điểm</th></tr>');
    canHoTro.forEach(function (r) {
      html.push('<tr><td ' + css + '>' + (r['Họ tên'] || r['Mã HS']) + '</td><td ' + css + '>' + r['Lớp'] +
        '</td><td ' + css + '>' + r['Tên khoá'] + '</td><td ' + css + '><b>' + r['Điểm tổng hợp'] + '</b>/5</td></tr>');
    });
    html.push('</table>');
  }

  if (phanHoi.length) {
    html.push('<h3 style="margin:18px 0 8px">💬 Phản hồi gần nhất</h3>');
    phanHoi.forEach(function (r) {
      html.push('<div style="border-left:3px solid #245c46;background:#f7f9f6;padding:9px 12px;margin:6px 0">',
        '<b>' + (r['Họ tên'] || '—') + '</b> <span style="color:#6a7770;font-size:12px">· ' +
        (r['Tên khoá'] || '') + ' · ' + (r['Đánh giá (1-5)'] || '—') + '/5</span><br/>',
        '<span style="font-size:13px">👍 ' + (r['Điều thích nhất'] || '—') + '<br/>🔧 ' +
        (r['Cần cải thiện'] || '—') + '</span></div>');
    });
  }

  var props = PropertiesService.getScriptProperties();
  html.push('<p style="margin-top:22px;font-size:12px;color:#6a7770">',
    '📄 <a href="https://docs.google.com/spreadsheets/d/' + props.getProperty('SS_ID') + '/edit">Mở bảng tính đầy đủ</a> · ',
    '📊 <a href="' + CONFIG.BASE_URL + 'ket-qua.html">Dashboard</a><br/>',
    'Email tự động từ STEM Portal — Apps Script (' + CONFIG.OWNER_EMAIL + ')</p></div>');

  var body = html.join('');
  MailApp.sendEmail({
    to: email,
    subject: '📊 Báo cáo STEM Portal — ' + ngay,
    htmlBody: body,
    name: 'STEM Portal'
  });
  ghiLog_('guiBaoCaoTongHop', courseId || '', 'OK', email);
  return { sent: true, to: email, courses: kA.length, students: dash.length, quotaLeft: MailApp.getRemainingDailyQuota() };
}

/* ═════════════════ 10. NHẬT KÝ & TIỆN ÍCH ═════════════════ */
function ghiLog_(hanhDong, khoa, ketQua, chiTiet) {
  try {
    var ss = bang_();
    var sh = ss.getSheetByName(SH.LOG) || taoSheet_(ss, SH.LOG, HEADERS[SH.LOG]);
    sh.appendRow([new Date(), hanhDong, khoa || '', ketQua || '', String(chiTiet || '').slice(0, 800)]);
    if (sh.getLastRow() > 5000) sh.deleteRows(2, 1000);
  } catch (e) {}
}

function xemThongTin() {
  var t = thongTinCauHinh_();
  Logger.log(JSON.stringify(t, null, 2));
  return t;
}

/** Xoá dữ liệu nghiệp vụ (giữ khoá học / lớp / học sinh). Cẩn thận! */
function xoaDuLieuNghiepVu() {
  var ss = bang_(), ds = [SH.SURVEY, SH.DASH];
  GROUPS.forEach(function (g) { ds.push(SH.PEER[g.id]); ds.push(SH.TEACHER[g.id]); });
  ds.forEach(function (n) {
    var sh = ss.getSheetByName(n);
    if (sh && sh.getLastRow() > 1) sh.getRange(2, 1, sh.getLastRow() - 1, sh.getLastColumn()).clearContent();
  });
  ghiLog_('xoaDuLieuNghiepVu', '', 'OK', '');
}

/* AeroLLM — shared top navigation for classroom tools. */
(function () {
  'use strict';
  var items = [
    { href: '../../index.html', label: 'Kho học liệu', icon: '⌂', external: true },
    { href: 'portal.html', label: 'Portal', icon: '◎' },
    { href: 'index.html', label: 'Khảo sát', icon: '▤' },
    { href: 'danh-gia.html', label: 'Đánh giá', icon: '◇' },
    { href: 'ket-qua.html', label: 'Kết quả', icon: '▥' },
    { href: 'admin.html', label: 'Quản lý', icon: '⚙' },
    { href: 'ket-noi.html', label: 'Kết nối', icon: '↗' }
  ];

  function boot() {
    if (document.querySelector('.science-nav')) return;
    var current = location.pathname.split('/').pop() || 'portal.html';
    var nav = document.createElement('nav');
    nav.className = 'science-nav';
    nav.setAttribute('aria-label', 'Điều hướng khu vực lớp học');
    nav.innerHTML = '<a class="science-nav-brand" href="../../index.html" aria-label="AeroLLM">' +
      '<span>A</span><b>AeroLLM</b></a>' +
      '<div class="science-nav-links">' + items.map(function (item) {
        var active = !item.external && current === item.href;
        return '<a href="' + item.href + '" class="science-nav-link' + (active ? ' active' : '') + '"' +
          (active ? ' aria-current="page"' : '') + '><i>' + item.icon + '</i><span>' + item.label + '</span></a>';
      }).join('') + '</div>';
    document.body.insertBefore(nav, document.body.firstChild);

    var active = nav.querySelector('.science-nav-link.active');
    if (active) setTimeout(function () { active.scrollIntoView({ block: 'nearest', inline: 'center' }); }, 0);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();

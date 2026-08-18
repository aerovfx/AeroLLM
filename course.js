const content = document.querySelector('#lesson-content');
const toc = document.querySelector('#toc');
const headings = [...content.querySelectorAll('h2, h3')];

const sidebarToggle = document.querySelector('#sidebar-toggle');
const sidebarPreferenceKey = 'cyberlearn-sidebar-collapsed';

function setSidebarCollapsed(collapsed) {
  document.body.classList.toggle('sidebar-collapsed', collapsed);
  sidebarToggle.setAttribute('aria-expanded', String(!collapsed));
  sidebarToggle.setAttribute('aria-label', collapsed ? 'Mở rộng thanh bên' : 'Thu gọn thanh bên');
  sidebarToggle.querySelector('span').textContent = collapsed ? '›' : '‹';
}

if (sidebarToggle) {
  setSidebarCollapsed(localStorage.getItem(sidebarPreferenceKey) === 'true');
  sidebarToggle.addEventListener('click', () => {
    const collapsed = !document.body.classList.contains('sidebar-collapsed');
    setSidebarCollapsed(collapsed);
    localStorage.setItem(sidebarPreferenceKey, String(collapsed));
  });
}

const pathParts = location.pathname.split('/').filter(Boolean);
const courseIndex = pathParts.findIndex((part) => part.endsWith('-10weeks'));
if (courseIndex !== -1) {
  const courseRoot = `/${pathParts.slice(0, courseIndex + 1).join('/')}`;
  const isCrypto = courseRoot.includes('/2_Cryptography/');
  const weekMatch = location.pathname.match(/week(\d{2})/i);
  const currentWeek = weekMatch ? Number(weekMatch[1]) : 1;
  const weekSlug = `week${String(currentWeek).padStart(2, '0')}`;
  const resources = [
    ['Lesson', `${courseRoot}/lessons/${weekSlug}.html`, '/lessons/'],
    ['Code', `${courseRoot}/code/${weekSlug}/README.html`, '/code/'],
    ['Exercise', isCrypto ? `${courseRoot}/code/week01/14_bai_tap_thuc_hanh_bai_ve_nha_hands_on_exercises_homewo.py` : `${courseRoot}/exercises/week01/README.html`, '/exercises/'],
    ['Project', `${courseRoot}/projects/final_project.html`, '/projects/']
  ];
  const resourceNav = document.querySelector('#resource-nav');
  resources.forEach(([label, href, matcher], index) => {
    const link = document.createElement('a');
    link.href = href;
    link.innerHTML = `<b>0${index + 1}</b><span>${label}</span><i>↗</i>`;
    const cryptoExercise = label === 'Exercise' && isCrypto && location.pathname.includes('bai_tap');
    if (location.pathname.includes(matcher) || cryptoExercise) link.classList.add('active');
    resourceNav.appendChild(link);
  });

  const weekNav = document.querySelector('#week-nav');
  const weekLabel = document.createElement('span');
  weekLabel.className = 'week-nav-label';
  weekLabel.textContent = '// CHỌN TUẦN';
  weekNav.appendChild(weekLabel);

  const weekLinks = document.createElement('div');
  weekLinks.className = 'week-nav-links';
  for (let week = 1; week <= 10; week += 1) {
    const link = document.createElement('a');
    link.href = `${courseRoot}/lessons/week${String(week).padStart(2, '0')}.html`;
    link.textContent = String(week).padStart(2, '0');
    link.setAttribute('aria-label', `Mở bài học tuần ${week}`);
    if (week === currentWeek) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
    weekLinks.appendChild(link);
  }
  weekNav.appendChild(weekLinks);

  const pagination = document.querySelector('#lesson-pagination');
  const addPaginationLink = (week, direction) => {
    const link = document.createElement('a');
    link.className = `lesson-${direction}`;
    link.href = `${courseRoot}/lessons/week${String(week).padStart(2, '0')}.html`;
    link.innerHTML = direction === 'previous'
      ? `<i>←</i><span><small>BÀI TRƯỚC</small>Tuần ${week}</span>`
      : `<span><small>BÀI TIẾP THEO</small>Tuần ${week}</span><i>→</i>`;
    pagination.appendChild(link);
  };
  if (currentWeek > 1) addPaginationLink(currentWeek - 1, 'previous');
  if (currentWeek < 10) addPaginationLink(currentWeek + 1, 'next');
  if (currentWeek === 1) pagination.classList.add('only-next');
}

function slugify(text, index) {
  const slug = text.toLocaleLowerCase('vi').normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
  return slug || `section-${index + 1}`;
}

headings.forEach((heading, index) => {
  if (!heading.id) heading.id = slugify(heading.textContent, index);
  const link = document.createElement('a');
  link.href = `#${heading.id}`;
  link.textContent = heading.textContent;
  if (heading.tagName === 'H3') link.classList.add('subheading');
  toc.appendChild(link);
});

if (!headings.length) toc.hidden = true;

const directChildren = [...content.children];
const firstSection = directChildren.findIndex((node) => node.tagName === 'H2');
if (firstSection > 0) {
  const intro = document.createElement('header');
  intro.className = 'doc-hero';
  content.insertBefore(intro, directChildren[0]);
  directChildren.slice(0, firstSection).forEach((node) => intro.appendChild(node));
}

[...content.children].forEach((node) => {
  if (node.tagName !== 'H2') return;
  const section = document.createElement('section');
  section.className = 'doc-section';
  content.insertBefore(section, node);
  let current = node;
  while (current && !(current !== node && current.tagName === 'H2')) {
    const next = current.nextElementSibling;
    section.appendChild(current);
    current = next;
  }
});

// Nâng cấp các khối mã nguồn thành khung có tiêu đề, mô tả và nút sao chép.
[...content.querySelectorAll('pre')].forEach((pre, index) => {
  const code = pre.querySelector('code');
  if (!code || pre.closest('.code-frame')) return;

  const heading = [...content.querySelectorAll('h2, h3, h4')]
    .filter((candidate) => candidate.compareDocumentPosition(pre) & Node.DOCUMENT_POSITION_FOLLOWING)
    .pop();
  const description = heading?.nextElementSibling?.tagName === 'P'
    ? heading.nextElementSibling.textContent.replace(/^Chức năng:\s*/i, '')
    : '';
  if (description) heading.nextElementSibling.classList.add('code-description-source');

  const frame = document.createElement('div');
  frame.className = 'code-frame';

  const toolbar = document.createElement('div');
  toolbar.className = 'code-toolbar';

  const windowControls = document.createElement('span');
  windowControls.className = 'code-window-controls';
  windowControls.setAttribute('aria-hidden', 'true');
  windowControls.innerHTML = '<i></i><i></i><i></i>';

  const meta = document.createElement('div');
  meta.className = 'code-meta';
  const titleGroup = document.createElement('div');
  titleGroup.className = 'code-title';
  const title = document.createElement('strong');
  title.textContent = heading?.textContent || `CODE BLOCK ${String(index + 1).padStart(2, '0')}`;
  titleGroup.appendChild(title);
  if (description) {
    const summary = document.createElement('small');
    summary.textContent = description;
    titleGroup.appendChild(summary);
  }
  const language = document.createElement('span');
  language.textContent = [...code.classList].find((name) => name.startsWith('language-'))?.replace('language-', '').toUpperCase() || 'CODE';
  meta.append(titleGroup, language);

  const copyButton = document.createElement('button');
  copyButton.type = 'button';
  copyButton.className = 'code-copy';
  copyButton.innerHTML = 'COPY CODE <span aria-hidden="true">⧉</span>';
  copyButton.setAttribute('aria-label', `Sao chép mã nguồn ${title.textContent}`);
  copyButton.addEventListener('click', async () => {
    await navigator.clipboard.writeText(code.textContent);
    copyButton.classList.add('copied');
    copyButton.innerHTML = 'ĐÃ SAO CHÉP <span aria-hidden="true">✓</span>';
    setTimeout(() => {
      copyButton.classList.remove('copied');
      copyButton.innerHTML = 'COPY CODE <span aria-hidden="true">⧉</span>';
    }, 1600);
  });

  const codeBody = document.createElement('div');
  codeBody.className = 'code-body';
  const lineNumbers = document.createElement('ol');
  lineNumbers.className = 'code-line-numbers';
  lineNumbers.setAttribute('aria-hidden', 'true');
  const lineCount = code.textContent.replace(/\n$/, '').split('\n').length;
  for (let line = 1; line <= lineCount; line += 1) {
    lineNumbers.appendChild(document.createElement('li'));
  }

  toolbar.append(windowControls, meta, copyButton);
  pre.parentNode.insertBefore(frame, pre);
  codeBody.append(lineNumbers, pre);
  frame.append(toolbar, codeBody);
});

document.querySelector('#copy-link').addEventListener('click', async (event) => {
  await navigator.clipboard.writeText(location.href);
  const label = event.currentTarget.firstChild;
  const previous = label.textContent;
  label.textContent = 'COPIED ';
  setTimeout(() => { label.textContent = previous; }, 1400);
});

addEventListener('scroll', () => {
  const max = document.documentElement.scrollHeight - innerHeight;
  document.querySelector('#reading-progress').style.width = `${max ? scrollY / max * 100 : 0}%`;
}, { passive: true });

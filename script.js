const search = document.querySelector('#course-search');
const cards = [...document.querySelectorAll('.course-card')];
const filterButtons = [...document.querySelectorAll('[data-filter]')];
const emptyState = document.querySelector('#empty-state');
let activeFilter = 'all';

function updateCourses() {
  const query = search.value.trim().toLocaleLowerCase('vi');
  let visible = 0;
  cards.forEach((card) => {
    const matchesFilter = activeFilter === 'all' || card.dataset.level === activeFilter;
    const matchesSearch = !query || card.dataset.search.includes(query) || card.textContent.toLocaleLowerCase('vi').includes(query);
    card.hidden = !(matchesFilter && matchesSearch);
    if (!card.hidden) visible += 1;
  });
  emptyState.hidden = visible !== 0;
}

search.addEventListener('input', updateCourses);
filterButtons.forEach((button) => button.addEventListener('click', () => {
  activeFilter = button.dataset.filter;
  filterButtons.forEach((item) => item.classList.toggle('active', item === button));
  updateCourses();
}));

document.querySelector('#year').textContent = new Date().getFullYear();

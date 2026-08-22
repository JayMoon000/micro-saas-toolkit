const themeToggleBtn = document.getElementById('themeToggle');
const currentTheme = localStorage.getItem('theme') || 'dark';

// 초기 테마 적용
if (currentTheme === 'light') {
  document.documentElement.setAttribute('data-theme', 'light');
  themeToggleBtn.querySelector('.icon').textContent = '🌙';
}

// 클릭 이벤트
themeToggleBtn.addEventListener('click', () => {
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  if (isLight) {
    document.documentElement.removeAttribute('data-theme');
    localStorage.setItem('theme', 'dark');
    themeToggleBtn.querySelector('.icon').textContent = '☀️';
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    themeToggleBtn.querySelector('.icon').textContent = '🌙';
  }
});
// Theme toggle functionality
(function () {
  const getTheme = () => localStorage.getItem('theme') ||
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

  const updateIcon = (theme) => {
    const moonIcon = document.querySelector('.moon-icon');
    const sunIcon = document.querySelector('.sun-icon');
    if (moonIcon && sunIcon) {
      if (theme === 'light') {
        moonIcon.style.display = 'block';
        sunIcon.style.display = 'none';
      } else {
        moonIcon.style.display = 'none';
        sunIcon.style.display = 'block';
      }
    }
  };

  const setTheme = (theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    updateIcon(theme);
  };

  // Set theme on load
  setTheme(getTheme());

  // Toggle function
  window.toggleTheme = () => {
    const currentTheme = getTheme();
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
  };
})();

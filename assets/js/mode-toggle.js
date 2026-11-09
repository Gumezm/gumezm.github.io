/* Light/Dark switch: flips on click instead of opening the theme menu.
   The theme's own bundle still expects `#mode-toggle + .dropdown-menu` to exist,
   so sidebar.html keeps that menu hidden — this script never touches it. */
(function () {
  'use strict';

  const root = document.documentElement;
  const btn = document.getElementById('mode-toggle');

  if (!btn || typeof Theme === 'undefined') return;

  const isDark = () => root.getAttribute('data-bs-theme') === 'dark';

  function sync() {
    const label = isDark() ? '切换到浅色模式' : '切换到深色模式';
    btn.setAttribute('aria-label', label);
    btn.setAttribute('title', label);
  }

  btn.addEventListener('click', () => {
    // Theme.update() persists the choice and flips the sidebar icon via CSS.
    Theme.update(isDark() ? 'light' : 'dark');
    sync();
  });

  // another tab may have switched the theme
  window.addEventListener('message', (event) => {
    if (event.data && event.data.id === 'theme-updated') sync();
  });

  sync();
})();

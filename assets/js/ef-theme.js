/* EF theme switch: ORI (original Chirpy) <-> EF, persisted in localStorage.
   The data-ef attribute is applied before first paint by an inline script in head.html. */
(function () {
  'use strict';

  const KEY = 'ef-theme';
  const root = document.documentElement;

  const isEf = () => root.getAttribute('data-ef') === 'ef';

  function sync() {
    const btn = document.getElementById('ef-toggle');
    if (!btn) return;

    const ef = isEf();
    btn.setAttribute('aria-pressed', ef ? 'true' : 'false');
    btn.setAttribute(
      'aria-label',
      ef ? '切换主题风格：当前 EF，点击回到原版' : '切换主题风格：当前原版，点击切换到 EF'
    );
    btn.setAttribute('title', ef ? '主题风格：EF（点击切换回原版）' : '主题风格：原版（点击切换到 EF）');
  }

  function apply(mode, persist) {
    if (mode === 'ef') {
      root.setAttribute('data-ef', 'ef');
    } else {
      root.removeAttribute('data-ef');
    }

    if (persist) {
      try {
        localStorage.setItem(KEY, mode);
      } catch (e) {
        /* storage unavailable: the switch still works for this page */
      }
    }

    sync();
  }

  function init() {
    sync();

    const btn = document.getElementById('ef-toggle');
    if (!btn) return;

    btn.addEventListener('click', () => {
      apply(isEf() ? 'ori' : 'ef', true);
    });

    // keep other tabs in sync
    window.addEventListener('storage', (event) => {
      if (event.key === KEY) apply(event.newValue === 'ef' ? 'ef' : 'ori', false);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

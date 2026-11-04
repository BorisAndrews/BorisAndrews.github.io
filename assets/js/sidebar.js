// Keep the sidebar in view while the page scrolls, but only when the whole of
// it (nav buttons included) fits in the window; otherwise it scrolls as usual.
(function () {
  var header = document.querySelector('.wrapper > header');
  if (!header) return;
  function update() {
    var fits = window.innerWidth > 960 && header.offsetHeight <= window.innerHeight;
    header.classList.toggle('sticky', fits);
  }
  update();
  window.addEventListener('resize', update);
  if (window.ResizeObserver) new ResizeObserver(update).observe(header);
})();

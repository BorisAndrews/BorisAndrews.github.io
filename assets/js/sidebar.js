// Keep the sidebar in view while the page scrolls, but only when all of its
// contents (nav buttons included) fit in the window; otherwise it scrolls as
// usual. Below the buttons there is only sand, so that may run off the screen.
(function () {
  var header = document.querySelector('.wrapper > header');
  if (!header) return;
  function update() {
    var last = header.querySelector('nav') || header.lastElementChild;
    var height = last.getBoundingClientRect().bottom - header.getBoundingClientRect().top;
    var fits = window.innerWidth > 960 && height + 16 <= window.innerHeight;
    header.classList.toggle('sticky', fits);
  }
  update();
  window.addEventListener('resize', update);
  window.addEventListener('load', update);
  if (window.ResizeObserver) new ResizeObserver(update).observe(header);
})();

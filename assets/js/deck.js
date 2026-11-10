// Embedded slide decks (_includes/deck.html): clicking the preview grows it to
// the largest 16:9 box that fits the window; Esc or the close button shrinks it
// back, and a tap or click on the open deck steps it. The close button shows
// for a moment on opening, then only while the pointer is in the window's
// top-right corner (always, on touchscreens).
//
// The frame is given its final, full-window size at once and scaled down to sit
// exactly over the preview, then the scale is animated away. Animating a
// transform rather than the size keeps the motion smooth, and since both boxes
// are 16:9 the scaling is uniform, so the slides never look stretched. The
// iframe itself is never moved in the DOM, which would reload the deck.
(function () {
  var DURATION = 450;
  var EASE = 'cubic-bezier(0.2, 0.7, 0.2, 1)';
  var RADIUS = 8;
  var CLOSE_SHOWN = 2500;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');

  function fit() {
    var w = Math.min(window.innerWidth, window.innerHeight * 16 / 9);
    var h = w * 9 / 16;
    return { left: (window.innerWidth - w) / 2, top: (window.innerHeight - h) / 2, width: w, height: h };
  }

  function place(el, box) {
    el.style.left = box.left + 'px';
    el.style.top = box.top + 'px';
    el.style.width = box.width + 'px';
    el.style.height = box.height + 'px';
  }

  // The transform taking the full-window box `to` onto the preview box `from`.
  function shrinkTo(from, to) {
    return 'translate(' + (from.left - to.left) + 'px, ' + (from.top - to.top) + 'px) scale(' + from.width / to.width + ')';
  }

  function setUp(deck) {
    var frame = deck.querySelector('.deck-frame');
    var iframe = frame.querySelector('iframe');
    var openButton = deck.querySelector('.deck-open');
    var closeButton = deck.querySelector('.deck-close');
    var state = 'closed';
    var hideTimer;

    function animate() {
      return reduce.matches ? 'none' :
        'transform ' + DURATION + 'ms ' + EASE + ', border-radius ' + DURATION + 'ms ' + EASE;
    }

    function open() {
      if (state !== 'closed') return;
      state = 'open';
      var from = deck.getBoundingClientRect();
      var to = fit();
      frame.style.transition = 'none';
      frame.style.position = 'fixed';
      frame.style.transformOrigin = '0 0';
      place(frame, to);
      frame.style.transform = shrinkTo(from, to);
      frame.style.borderRadius = RADIUS * to.width / from.width + 'px';
      deck.classList.add('open');
      deck.classList.add('show-close');
      window.clearTimeout(hideTimer);
      hideTimer = window.setTimeout(function () {
        deck.classList.remove('show-close');
      }, (reduce.matches ? 0 : DURATION) + CLOSE_SHOWN);
      document.documentElement.style.overflow = 'hidden';
      frame.getBoundingClientRect();
      frame.style.transition = animate();
      frame.style.transform = 'none';
      frame.style.borderRadius = '0';
      iframe.tabIndex = 0;
      window.setTimeout(function () {
        iframe.focus();
        try { iframe.contentWindow.focus(); } catch (e) {}
      }, reduce.matches ? 0 : DURATION);
    }

    function close() {
      if (state !== 'open') return;
      state = 'closing';
      document.documentElement.style.overflow = '';
      var from = deck.getBoundingClientRect();
      var to = fit();
      frame.style.transition = animate();
      frame.style.transform = shrinkTo(from, to);
      frame.style.borderRadius = RADIUS * to.width / from.width + 'px';
      window.clearTimeout(hideTimer);
      deck.classList.remove('show-close');
      deck.classList.remove('open');
      deck.classList.add('closing');
      window.setTimeout(function () {
        frame.removeAttribute('style');
        deck.classList.remove('closing');
        iframe.tabIndex = -1;
        state = 'closed';
        openButton.focus({ preventScroll: true });
      }, reduce.matches ? 0 : DURATION);
    }

    // Capture phase, so Esc closes the deck instead of reaching reveal.js
    // (which would toggle its slide overview).
    function onKey(event) {
      if (event.key === 'Escape' && state === 'open') {
        event.preventDefault();
        event.stopImmediatePropagation();
        close();
      }
    }

    // reveal.js moves on only by swiping on a touchscreen, so a tap (or click)
    // on the open deck steps it: back on the left third, forward elsewhere.
    function onTap(event) {
      var reveal = iframe.contentWindow.Reveal;
      if (state !== 'open' || !reveal || event.button !== 0) return;
      if (event.clientX < iframe.contentWindow.innerWidth / 3) reveal.prev();
      else reveal.next();
    }

    function listenInside() {
      try {
        iframe.contentWindow.addEventListener('keydown', onKey, true);
        iframe.contentDocument.addEventListener('click', onTap);
      } catch (e) {}
    }

    openButton.addEventListener('click', open);
    // Clicks on the margins or in the close button's corner would otherwise take
    // focus from the deck, and the arrow keys would stop advancing the slides.
    deck.querySelectorAll('.deck-backdrop, .deck-corner').forEach(function (el) {
      el.addEventListener('mousedown', function (event) { event.preventDefault(); });
    });
    closeButton.addEventListener('click', close);
    document.addEventListener('keydown', onKey, true);
    iframe.addEventListener('load', listenInside);
    try {
      if (iframe.contentDocument && iframe.contentDocument.readyState === 'complete') listenInside();
    } catch (e) {}

    window.addEventListener('resize', function () {
      if (state !== 'open') return;
      frame.style.transition = 'none';
      place(frame, fit());
    });
  }

  document.querySelectorAll('.deck').forEach(setUp);
})();

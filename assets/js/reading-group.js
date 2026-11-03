// The reading-group page keeps its references and past records in collapsed
// <details> sections. A link to an anchor inside one (from a schedule row, or
// an old /reading-group/references/#id URL forwarded here) must open every
// enclosing section first, or the target has no box to scroll to.
(function () {
  function reveal(id, scroll) {
    var target = id && document.getElementById(id);
    if (!target) return;
    for (var el = target; el; el = el.parentElement) {
      if (el.tagName === "DETAILS") el.open = true;
    }
    if (scroll) target.scrollIntoView();
  }

  function hashId() {
    return decodeURIComponent(location.hash.slice(1));
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href*='#']");
    if (!a || a.pathname !== location.pathname) return;
    reveal(decodeURIComponent(a.hash.slice(1)), false);
  });

  window.addEventListener("hashchange", function () { reveal(hashId(), true); });

  document.addEventListener("DOMContentLoaded", function () {
    reveal(hashId(), true);

    // Keep the address bar in step with what is open, so the URL can be shared.
    document.querySelectorAll("details.rg-toggle").forEach(function (d) {
      d.addEventListener("toggle", function () {
        if (d.open) {
          if (!d.contains(document.getElementById(hashId()))) {
            history.replaceState(null, "", "#" + d.id);
          }
        } else if (location.hash && (location.hash === "#" + d.id || d.contains(document.getElementById(hashId())))) {
          var parent = d.parentElement.closest("details.rg-toggle");
          history.replaceState(null, "", parent ? "#" + parent.id : location.pathname);
        }
      });
    });
  });
})();

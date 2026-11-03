// Following any link to the CV page also opens the PDF CV in a new tab, so
// visitors see that it exists. It has to happen inside the click: browsers
// block a tab opened later by the CV page itself as a pop-up. Clicks with a
// modifier key (open in new tab/window) are left alone.
document.addEventListener("click", function (e) {
  if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
  var a = e.target.closest && e.target.closest("a[href]");
  if (!a || a.target === "_blank") return;
  var sameSite = a.origin === location.origin || a.hostname === "borisandrews.github.io";
  if (!sameSite || a.pathname.replace(/\/?$/, "/") !== "/cv/") return;
  if (location.pathname.replace(/\/?$/, "/") === "/cv/") return;
  window.open("/cv/assets/pdf/cv.pdf", "_blank", "noopener");
});

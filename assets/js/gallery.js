// Arrow buttons for the collaborator carousel: each click pans one screenful
// (the visible columns plus the gap after them), and a button is disabled at
// its end of the track.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".gallery").forEach(function (track) {
    var controls = track.nextElementSibling;
    if (!controls || !controls.classList.contains("gallery-controls")) return;
    var prev = controls.querySelector(".gallery-prev");
    var next = controls.querySelector(".gallery-next");
    var gap = function () {
      return parseFloat(getComputedStyle(track).columnGap) || 0;
    };
    var step = function (dir) {
      track.scrollBy({ left: dir * (track.clientWidth + gap()), behavior: "smooth" });
    };
    var update = function () {
      prev.disabled = track.scrollLeft <= 1;
      next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 1;
    };
    prev.addEventListener("click", function () { step(-1); });
    next.addEventListener("click", function () { step(1); });
    track.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  });
});

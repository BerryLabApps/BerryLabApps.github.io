(function () {
  var root = document.documentElement;
  var supported = ["en", "ru"];

  function initialLanguage() {
    var fromUrl = new URLSearchParams(location.search).get("lang");
    if (supported.indexOf(fromUrl) >= 0) return fromUrl;
    try {
      var saved = localStorage.getItem("lang");
      if (supported.indexOf(saved) >= 0) return saved;
    } catch (e) {}
    var browser = (navigator.language || "en").toLowerCase();
    return /^(ru|uk|be|kk)/.test(browser) ? "ru" : "en";
  }

  function syncButtons() {
    document.querySelectorAll("[data-set-lang]").forEach(function (button) {
      button.setAttribute("aria-pressed", String(button.getAttribute("data-set-lang") === root.lang));
    });
    var title = document.querySelector("meta[name='title-" + root.lang + "']");
    if (title) document.title = title.content;
  }

  root.lang = initialLanguage();

  document.addEventListener("DOMContentLoaded", syncButtons);

  document.addEventListener("click", function (event) {
    var button = event.target.closest("[data-set-lang]");
    if (!button) return;
    root.lang = button.getAttribute("data-set-lang");
    syncButtons();
    try { localStorage.setItem("lang", root.lang); } catch (e) {}
  });
})();

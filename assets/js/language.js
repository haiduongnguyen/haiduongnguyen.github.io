(function () {
  "use strict";

  var storageKey = "haiduong-blog-language";
  var supportedLanguages = ["vi", "en"];
  var root = document.documentElement;
  var body = document.body;

  function preferredLanguage() {
    var requested = new URLSearchParams(window.location.search).get("lang");
    if (supportedLanguages.indexOf(requested) !== -1) return requested;

    try {
      var saved = window.localStorage.getItem(storageKey);
      if (supportedLanguages.indexOf(saved) !== -1) return saved;
    } catch (error) {
      // The site remains usable when storage is disabled.
    }

    return "en";
  }

  function setLanguage(language, persist) {
    var nextLanguage = supportedLanguages.indexOf(language) !== -1 ? language : "en";
    root.lang = nextLanguage;
    body.classList.add("language-ready");

    document.querySelectorAll("[data-set-language]").forEach(function (button) {
      button.setAttribute("aria-pressed", String(button.dataset.setLanguage === nextLanguage));
    });

    var title = body.dataset[nextLanguage === "vi" ? "titleVi" : "titleEn"];
    var description = body.dataset[nextLanguage === "vi" ? "descriptionVi" : "descriptionEn"];
    if (title) document.title = title + " | Hai Duong Nguyen";

    var descriptionTag = document.querySelector('meta[name="description"]');
    if (descriptionTag && description) descriptionTag.setAttribute("content", description);

    if (persist) {
      try {
        window.localStorage.setItem(storageKey, nextLanguage);
      } catch (error) {
        // Ignore storage failures without blocking language switching.
      }
    }
  }

  function attachOriginalArchive() {
    var source = document.querySelector('.original-source[data-original-source="true"][data-lang]');
    if (!source) return;

    var sourceLanguage = source.dataset.lang;
    var targetLanguage = sourceLanguage === "en" ? "vi" : "en";
    var translation = document.querySelector(
      '.reading-page[data-lang="' + targetLanguage + '"]:not(.original-source)'
    );
    if (!translation || translation.querySelector(".original-archive")) return;

    var archive = document.createElement("details");
    archive.className = "original-archive";

    var summary = document.createElement("summary");
    summary.textContent = targetLanguage === "vi"
      ? "Nội dung và code nguyên bản (English)"
      : "Original content and code (Vietnamese)";

    var content = document.createElement("div");
    content.lang = sourceLanguage;
    content.innerHTML = source.innerHTML;
    content.querySelectorAll(".original-source__note").forEach(function (note) {
      note.remove();
    });
    content.querySelectorAll("[id]").forEach(function (element) {
      element.removeAttribute("id");
    });

    archive.appendChild(summary);
    archive.appendChild(content);
    translation.appendChild(archive);
  }

  document.querySelectorAll("[data-set-language]").forEach(function (button) {
    button.addEventListener("click", function () {
      setLanguage(button.dataset.setLanguage, true);
    });
  });

  document.querySelectorAll("[data-banking-lab-link]").forEach(function (link) {
    link.addEventListener("click", function () {
      try {
        window.localStorage.setItem("banking-metrics-lab:language", "en");
      } catch (error) {
        // Navigation still works when storage is disabled.
      }
    });
  });

  attachOriginalArchive();
  setLanguage(preferredLanguage(), false);
})();

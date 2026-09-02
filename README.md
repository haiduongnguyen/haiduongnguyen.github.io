# haiduongnguyen.github.io

Personal bilingual portfolio and learning blog built with Jekyll and hosted on GitHub Pages.

## Content model

- Every public page contains Vietnamese and English sections marked with `data-lang="vi"` and `data-lang="en"`.
- The global language switch is implemented in `assets/js/language.js` and remembers the visitor's choice in `localStorage`.
- English is the default for first-time visitors; an explicit query-string or saved language preference takes precedence.
- Page-specific `title_vi`, `title_en`, `description_vi`, and `description_en` values update browser metadata when the language changes.
- Writing pages opt into the complete `/writing/` index with a `writing_topic` front-matter value.
- Banking examples must remain aggregated, anonymized, or synthetic.

## Local development

The local Ruby/Jekyll toolchain lives in the isolated sibling directory
`../blog_github_venv`; Docker is not required.

```powershell
.\scripts\blog.ps1 serve
```

Build without starting the development server:

```powershell
.\scripts\blog.ps1 build
```

Before publishing, check internal links and the responsive layout at 375, 768, 1024, and 1440 pixels.

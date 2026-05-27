# CLAUDE.md — borisandrews.github.io

Jekyll academic portfolio. Theme: `jekyll-theme-minimal` (heavily customised).

## Build

```
bundle exec jekyll serve   # local preview at localhost:4000
```

No Makefile. Edit source files directly; compiled CSS is in `assets/css/` (do not edit — regenerated from `_sass/`).

## Directory map

| Path | Purpose |
|---|---|
| `_config.yml` | Site-wide settings (title, email, logo, theme) |
| `_layouts/default.html` | Master template (header, nav, footer) |
| `_sass/jekyll-theme-minimal.scss` | All custom styles — edit here |
| `_sass/fonts.scss` | Font config (JetBrains Mono preferred) |
| `_includes/` | Reusable Liquid components (see below) |
| `index.md` | Homepage (research, highlights, CV section, conferences, collaborators, reading group, open problems) |
| `publications/<slug>/index.md` | Individual paper pages |
| `collaborators/` | Collaborator listing page |
| `cv/` | CV page |
| `reading-group/` | FEM reading group page |
| `open-problems/` | Open problems page |
| `assets/img/` | Images (portrait, collaborator photos, favicon) |
| `assets/pdf/` | PDF files |
| `assets/ipynb/` | Jupyter notebooks, referenced from the private `notebooks/` page |

## `_includes/` structure

The site is data-driven via includes — avoid duplicating information by adding it here first.

| Subdirectory | Content |
|---|---|
| `collaborators/<name>/full.md` + `short.md` | Collaborator profile (full and inline versions) |
| `conferences/<name>.md` | Conference entry |
| `publications/` | Publication lists by status (papers, review, drafts, other) |
| `journals/<abbrev>.md` | Journal name/link |
| `organisations/` | Funding bodies, universities |
| `interest/` | Research interest snippets |
| `highlight-box.md` | Clickable highlighted box component |
| `reveal-box.md` | Expandable/collapsible section component |
| `gallery.md` | Collaborator photo gallery |
| `timeline.md` | CV timeline component |

Usage in pages: Liquid include tags pointing to files under `_includes/`, e.g. `collaborators/patrick/short.md`, `journals/sisc.md`.

## Style conventions

- **Headings**: ALL CAPS (consistent throughout site).
- **Maths**: KaTeX + MathJax both loaded; use standard LaTeX in backtick fences or `$$...$$`.
- **Colours** (defined in `_sass/jekyll-theme-minimal.scss`):
  - Background: warm beige `#FBF6E5`
  - Headings: brown `#B3532A`
  - Links: blue `#578ACC`
- **Paper page pattern** (see `publications/geometric-flows/index.md` as canonical example):
  1. YAML front matter with `title` and `permalink`
  2. Full paper title as `# H1`
  3. Authors line using Liquid include tags for co-authors (e.g. `collaborators/patrick/short.md`)
  4. Date + venue line
  5. Optional `highlight-box` for arXiv/DOI link
  6. Pull-quote abstract snippet in `> blockquote`
  7. `reveal-box` for full abstract
  8. Further sections as needed (Related Works, Open Problems, etc.)

## Adding content

**New publication page**: create `publications/<slug>/index.md` following the pattern above; add entry to `_includes/publications/` list file for appropriate status.

**New collaborator**: add `_includes/collaborators/<name>/short.md` and `full.md`; optionally add photo to `assets/img/collaborators/`.

**New conference**: add `_includes/conferences/<name>.md` and include it in `index.md`.

## What not to touch

- `assets/css/` — compiled, regenerated on build.
- `googleddcaaf3c3cd4feed.html` — Google Search Console verification file.
- `sitemap.xml` — keep in sync with actual pages if edited manually.

# CLAUDE.md — borisandrews.github.io

Jekyll academic portfolio. Theme: `jekyll-theme-minimal` (heavily customised).

## Build

**There is no local build.** The repo has no `Gemfile` and no `_site/`, and Jekyll is not installed on this machine — `bundle exec jekyll serve` fails with "Could not locate Gemfile". The site is built and deployed by GitHub Pages on push to `main`.

So changes cannot be previewed locally as things stand. Verify by inspection instead: every `{% include %}` path you write must correspond to an existing file under `_includes/` (a missing include is a hard build failure on Pages). The one thing that *is* locally buildable is the PDF CV — see `cv/assets/pdf/CLAUDE.md`.

No Makefile. Edit source files directly; compiled CSS is in `assets/css/` (do not edit — regenerated from `_sass/`).

## Directory map

| Path | Purpose |
|---|---|
| `_config.yml` | Site-wide settings (title, email, logo, theme) |
| `_layouts/default.html` | Master template (header, portrait, sidebar nav, footer) |
| `_layouts/blank.html` | Stripped template: no sidebar, no nav, **no KaTeX/MathJax**, just a "Back to home" arrow |
| `_sass/jekyll-theme-minimal.scss` | All custom styles — edit here |
| `_sass/fonts.scss` | Font config (JetBrains Mono preferred) |
| `_includes/` | Reusable Liquid components (see below) |
| `index.md` | Homepage (research, highlights, CV section, conferences, collaborators, reading group, open problems) |
| `publications/<slug>/index.md` | Individual paper pages |
| `collaborators/` | Collaborator listing page |
| `cv/` | CV page |
| `reading-group/` | FEM reading group page |
| `open-problems/` | Open problems page |
| `geofem-workshop/` | Page for the ERC GeoFEM workshop Boris co-organises (Oxford, 24–27 May 2027) |
| `assets/img/` | Images (portrait, collaborator photos, favicon) |
| `assets/pdf/` | PDF files |
| `assets/ipynb/` | Jupyter notebooks, referenced from the private `notebooks/` page |

## `_includes/` structure

The site is data-driven via includes — avoid duplicating information by adding it here first.

| Subdirectory | Content |
|---|---|
| `collaborators/<name>/full.md` + `short.md` | Collaborator profile (full and inline versions) |
| `conferences/<year>/<name>.md` | Conference entry, filed under the year it happens |
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

**New standalone page**: `<slug>/index.md` with front matter of just `title` and `permalink: /<slug>/` — **do not** add a `layout:` key. Jekyll applies `default` (sidebar, nav, maths) on its own, which is what every page here except `reading-group/` wants; that one opts into `layout: blank` deliberately. A new page is *not* automatically reachable: the sidebar nav is hardcoded in `_layouts/default.html`, so either add an `<li>` there or link the page from wherever it belongs (`geofem-workshop/` is reached from the `UPCOMING` list in `index.md`, the way paper pages are reached from the publication lists).

**New conference**: add `_includes/conferences/<year>/<name>.md` (one line: the linked event name, or plain text if it has no site yet) and include it wherever it is referenced — the `UPCOMING` list in `index.md`, the TALKS lines in `cv/index.md`, or a publication page.

**New person**: `_includes/collaborators/<firstname>/short.md`, one line, `[Full Name](link)`. `full.md`, a photo under `assets/img/collaborators/` and an entry on `collaborators/index.md` are only for genuine research collaborators — people who appear merely as organisers or co-hosts (the Oberwolfach organisers, the GeoFEM workshop co-organisers) get `short.md` alone.

**Revised arXiv preprint** (a new vN of a paper already on the site) touches four places, and it is easy to stop after the first:

1. `_includes/publications/all/<slug>.md` — the date in the table row.
2. `_includes/publications/lists/4-review.md` — the lists are hand-ordered **newest first**, so a bumped date usually means moving the line.
3. `publications/<slug>/index.md` — the date heading, *and both copies of the abstract*: the bolded pull-quote `> blockquote` and the full text inside the FULL ABSTRACT reveal-box. Check the surrounding prose too; it paraphrases the abstract, so a changed term needs changing there as well.
4. `cv/assets/pdf/components/papers.tex` — the `\cventry` date, likely also reordered. Rebuild `cv.pdf`.

The DOI link (`10.48550/arXiv.NNNN.NNNNN`) is versionless and never changes.

Get the abstract and dates from the **API**, not the abs page — `https://export.arxiv.org/api/query?id_list=<id>` returns `<published>` (v1), `<updated>` (current version) and a verbatim `<summary>`, with no risk of a paraphrase creeping into a quoted abstract. Note plain `http://` returns an empty body; use `https` and `-L`.

**The arXiv date is always the date of the most recent version**, never v1 — Boris settled this in Aug 2026, and all rows were brought into line then (`parker` JAN.2025→NOV.2025, `sp-integrators-a` APR.2025→SEP.2025, `sp-integrators-b` NOV.2025→AUG.2026). It applies to published papers too, where the arXiv date sits beside a separate journal date; only the arXiv half moves. Take it from the API's `<updated>`, not `<published>`.

**New organised event**: an event Boris co-organises goes in three places — the `UPCOMING` list in `index.md`, `_includes/minisymposia/<name>.md` for the CV page's HOSTED WORKSHOPS & MINISYMPOSIA section, and a matching `\cventry` in `cv/assets/pdf/components/minisymposia.tex` (the PDF CV duplicates the content in raw LaTeX with hardcoded `\href`s — it shares no includes with the site, so it must be edited by hand and rebuilt).

## What not to touch

- `assets/css/` — compiled, regenerated on build.
- `googleddcaaf3c3cd4feed.html` — Google Search Console verification file.
- `sitemap.xml` — keep in sync with actual pages if edited manually.

## Adding CLAUDE.md files

Any new CLAUDE.md created inside this directory must be added to the `exclude` list in `_config.yml`. Jekyll processes all `.md` files it finds, and Liquid syntax in CLAUDE.md files will break the build. The current excludes are `CLAUDE.md`, `assets/ipynb/CLAUDE.md`, `cv/CLAUDE.md`, and `cv/assets/pdf/CLAUDE.md`.

# CLAUDE.md — cv/

Website CV page at `/cv/`. Mirrors the LaTeX PDF CV in `assets/pdf/`.

## Files

| File | Purpose |
|---|---|
| `index.md` | Main CV page (Jekyll/Liquid source) |
| `assets/pdf/cv.tex` | LaTeX source for the PDF CV |
| `assets/pdf/cv.pdf` | Compiled PDF — linked from the page |
| `assets/pdf/components/` | LaTeX section components |

See `assets/pdf/CLAUDE.md` for details on the LaTeX source.

## Page structure (`index.md`)

Standard Jekyll page with YAML front matter (`title: CV`, `permalink: /cv/`).
The page opens and closes with `cv-download.md` (a highlight-box linking to `cv.pdf`).

Sections in order — the *ideal* order given by the `% N` comments in `assets/pdf/cv.tex`. The PDF shuffles its sections to fit pages; this page has no such constraint, so it keeps the ideal order:

| Section | Source |
|---|---|
| EMPLOYMENT | `_includes/employment/oxford.md` |
| EDUCATION | `_includes/education/phd.md` + `education/mmath.md` |
| RESEARCH INTERESTS | `_includes/interests.md` |
| PUBLICATIONS & PREPRINTS | `_includes/publications/lists/1-papers.md` etc. |
| PRIZES, AWARDS & SCHOLARSHIPS | Inline markdown (no include) |
| TALKS | Inline markdown using `_includes/conferences/` and `_includes/universities/` |
| HOSTED WORKSHOPS & MINISYMPOSIA | `_includes/minisymposia/<name>.md` |
| TEACHING | Inline markdown (no include) |
| SUPERVISION | `_includes/supervision/<name>.md` |
| OTHER EXPERIENCE | `_includes/experience/<name>.md` |
| LANGUAGES | Inline markdown (no include) |

Sections the PDF leaves out are commented out here too, not deleted: Prizes (its `\input` is commented out in `cv.tex`), HTML under programming languages, and the 2023 Tokamak Energy internal presentation, which the PDF never listed (synced Oct 2026). Wording follows the PDF, which is authoritative; links may differ (the web links paper titles to the site's own pages, the PDF to DOIs).

Publications lists are shared with the main publications page (`_includes/publications/lists/`); updating a list file updates both pages.

The `_includes/minisymposia/` directory is broader than its name: it backs the
HOSTED WORKSHOPS & MINISYMPOSIA section, so organised workshops live there too
(`fetc.md`). Don't add a parallel `_includes/workshops/`.

## Visual conventions

- Section headings are ALL CAPS (`##`) matching the rest of the site.
- Visual separator between date and entry: `<code>&#124;</code>` (renders as `|`).
- Talks lines use `*upcoming*` note with `*(\*upcoming)*` at end of section.
- Commented-out sections (e.g. upcoming publications) are kept for easy reinstatement.

## Keeping in sync with the LaTeX CV

When adding entries, update both `index.md` and the relevant `components/*.tex` file so the PDF and website stay consistent. The PDF is the primary CV distributed externally; the website version is the browsable counterpart.

## Jekyll exclusion

This CLAUDE.md is listed in `_config.yml` under `exclude` to prevent Jekyll from processing it.

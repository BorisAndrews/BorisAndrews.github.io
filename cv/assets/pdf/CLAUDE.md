# CLAUDE.md — cv/assets/pdf/

LaTeX source for the PDF CV, compiled to `cv.pdf` which is linked from the website CV page.

## Build

**Never run `latexmk` here** (root CLAUDE.md: Boris's VS Code rebuilds in this directory, and two builds at once corrupt `cv.aux`). When the tracked `cv.pdf` needs refreshing, build out of tree and copy the result in — only when Boris asks, since this is the PDF he reads and the site serves:

```sh
Software/latex-check --clean Mine/Other/Website/cv/assets/pdf/cv.tex
cp ~/Library/Caches/claude-latex/cv-*/cv.pdf Mine/Other/Website/cv/assets/pdf/cv.pdf
```

The paragraph below about `latexmk --pdf cv.tex` is how Boris's editor builds it, not a command to run.


```
latexmk --pdf cv.tex
```

Run from this directory (`cv/assets/pdf/`). No Makefile — invoke `latexmk` directly.
Build artefacts (`*.aux`, `*.log`, `*.fls`, `*.fdb_latexmk`, `*.out`, `*.synctex.gz`) can be ignored.

## Document class & packages

- `moderncv`, style `classic`, 12pt, a4paper, roman font family
- `palatino` for body text; `\fontfamily{qag}` (Avant Garde / TeX Gyre Adventor) for the title block
- `geometry` with `scale=0.8`
- `fancyhdr` for the footer: "Last updated: \today" in `color2` (grey), right-aligned
- `hyperref` with `linkcolour` blue (`#4C72B0`)
- FontAwesome icons via `\faGoogle`, `\faGithub`, `\faOrcid`, `\faLinkedin`, `\faEnvelope`, `\faGlobe`

## Colour palette

| Name | Hex | Usage |
|---|---|---|
| `color0` | `#000000` | Body text |
| `color1` | `#C44E52` (seabornred) | Section headers |
| `color2` | `#B2B2B2` (grey) | Footer |
| `linkcolour` | `#4C72B0` (seabornblue) | Hyperlinks |

### The `\definecolor` block must come BEFORE `\moderncvstyle`

This is order-sensitive and fails silently. `moderncvstyleclassic.sty` snapshots the scheme colours the moment it loads:

```latex
\colorlet{sectioncolor}{color1}   % and bodyrulecolor, namecolor, titlecolor, …
```

`\colorlet` copies the *current value*; it is not an alias. And `moderncv.cls` initialises `color0`–`color3` to **black**. So if `\definecolor{color1}{...}` comes after `\moderncvstyle{classic}`, the section headings and rules are already frozen black, and the CV builds clean but comes out looking greyscale — only the things that use `\textcolor{color1}` at point of use (the itemize bullets) stay red.

This bit in Aug 2026 on a new machine: it was latent for years because older moderncv did not use `\colorlet` here. Fixed by moving the `\definecolor` block above `\moderncvstyle` (moderncv 2.5.1, TeX Live 2026). Do not reorder it back.

Hyperlinks are unaffected either way — `linkcolour` is resolved by hyperref at use time, so blue links surviving while headings go black is the diagnostic signature of this bug, not evidence that colour is fine.

## Entry macro

All CV entries use `\cventry`:

```latex
\cventry{date}{title}{subtitle}{institution}{}{%
  \begin{itemize}
    \item ...
  \end{itemize}%
}
```

The fifth argument is always empty (moderncv uses it for grade/GPA — unused here).
Dates are plain strings, e.g. `2025 -- 2027 \emph{(predicted)}` or `30 Apr 2026`.

## Section structure

Sections use `\section{\textsc{...}}`, subsections use `\subsection{...}` (plain or `\small{\textcolor{color0}{...}}` for parenthetical labels like "(In review)").
`\vspace{0mm}` and `\vspace{1mm}` are used between entries for spacing.

Four explicit `\newpage`s in `cv.tex` divide it into five blocks, one page each, so the CV is **five** pages (Boris's layout since Oct 2026): (1) employment, education, research interests, languages; (2) publications; (3) talks; (4) hosted workshops & minisymposia, teaching, supervision; (5) other experience. Boris moved to this when the four-page layout ran out of room on page 1, so it is deliberate — don't try to squeeze it back to four. Check `Output written on cv.pdf (N pages…)` after adding an entry: a block that outgrows its page shows up as a sixth page.

Note `prizes.tex` and `references.tex` are commented out in `cv.tex`; they are not in the PDF.

## Component files

Each section is a separate file under `components/`; order in `cv.tex` determines page layout:

| File | Section |
|---|---|
| `employment.tex` | Employment |
| `education.tex` | Education |
| `interests.tex` | Research Interests |
| `languages.tex` | Languages |
| `papers.tex` | Publications & Preprints |
| `presentations.tex` | Talks (invited & other) |
| `minisymposia.tex` | Hosted Workshops & Minisymposia (organised workshops go here too) |
| `teaching.tex` | Teaching (grouped by academic year; a second role in the same year is a `\cventry` with an empty date) |
| `supervision.tex` | Supervision |
| `experience.tex` | Other Experience |
| `prizes.tex` | Prizes, Awards & Scholarships (commented out in cv.tex) |
| `references.tex` | References (commented out in cv.tex) |

## Where PDF links point

The PDF goes out to people who won't browse the site, so its `\href`s point at
**external, citable targets** — a DOI, or an arXiv DOI (`https://doi.org/10.48550/arXiv.<id>`) —
not at `borisandrews.github.io/publications/...` pages. Boris removed a
website-page link from Matin's supervision entry (Sep 2026) and asked for the
arXiv link instead. The website CV is different: there, the same project title
links to the internal paper page, and that's intended. So "keeping in sync"
means the same entries, not identical link targets.

(The FETC workshop entry in `minisymposia.tex` is the exception, since the
workshop page is the only place its details live.)

## Keeping in sync with the website CV

The LaTeX CV and `cv/index.md` cover the same information — keep them in sync when adding entries. The PDF is the authoritative version for layout; the website version uses Liquid includes for most sections.

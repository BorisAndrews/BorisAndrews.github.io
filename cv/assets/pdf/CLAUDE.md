# CLAUDE.md — cv/assets/pdf/

LaTeX source for the PDF CV, compiled to `cv.pdf` which is linked from the website CV page.

## Build

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

Three explicit `\newpage`s in `cv.tex` divide it into four blocks, one page each, so the CV is **four** pages: employment–teaching, supervision–publications, presentations, then minisymposia–languages. (An older note here said three; a block has been added since.) Each block currently fits its page with little room, so check `Output written on cv.pdf (N pages…)` after adding an entry — a spill shows up as a fifth page.

Note `prizes.tex` and `references.tex` are commented out in `cv.tex`; they are not in the PDF.

## Component files

Each section is a separate file under `components/`; order in `cv.tex` determines page layout:

| File | Section |
|---|---|
| `employment.tex` | Employment |
| `education.tex` | Education |
| `interests.tex` | Research Interests |
| `prizes.tex` | Prizes, Awards & Scholarships |
| `papers.tex` | Publications & Preprints |
| `teaching.tex` | Teaching |
| `supervision.tex` | Supervision |
| `presentations.tex` | Talks (invited & other) |
| `minisymposia.tex` | Hosted Workshops & Minisymposia (organised workshops go here too) |
| `experience.tex` | Other Experience |
| `languages.tex` | Languages |
| `references.tex` | References (commented out in cv.tex) |

## Keeping in sync with the website CV

The LaTeX CV and `cv/index.md` cover the same information — keep them in sync when adding entries. The PDF is the authoritative version for layout; the website version uses Liquid includes for most sections.

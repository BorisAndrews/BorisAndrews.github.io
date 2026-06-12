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
`\newpage` separates the three physical pages: page 1 (employment–prizes), page 2 (publications–supervision), page 3 (presentations–languages).

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
| `minisymposia.tex` | Hosted Minisymposia |
| `experience.tex` | Other Experience |
| `languages.tex` | Languages |
| `references.tex` | References (commented out in cv.tex) |

## Keeping in sync with the website CV

The LaTeX CV and `cv/index.md` cover the same information — keep them in sync when adding entries. The PDF is the authoritative version for layout; the website version uses Liquid includes for most sections.

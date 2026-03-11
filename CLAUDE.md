# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Math 4025: Statistical Machine Learning** (Spring 2026) course website for Dr. Eric Friedlander at the College of Idaho. It is a [Quarto](https://quarto.org/) website that auto-deploys to GitHub Pages at https://EricFriedlander.github.io/math4025sp26/.

The **Quizzes and Exams** for the course are stored separately in `/home/efriedlander/Dropbox/Teaching/MATH-4025-Quizzes/` — this folder must **never** be pushed to GitHub or published publicly.

## Common Commands

All commands run from the project root using the `math-4025-sp26` conda environment.

```bash
# Activate environment
conda activate math-4025-sp26

# Preview site locally (live reload)
quarto preview

# Render the entire site
quarto render

# Render a single file
quarto render slides/13-missing-data.qmd
quarto render hw/04-hw-classification.qmd
```

Deployment to GitHub Pages happens automatically via GitHub Actions on push to `master`. To manually publish:
```bash
quarto publish gh-pages
```

## Architecture

### Content pipeline
All content is written in `.qmd` (Quarto Markdown). The site is configured in `_quarto.yml` (sidebar navigation, theme, footer). The homepage (`index.qmd`) renders the course schedule from `course-info/schedule.csv` using **R + `gt`** — this is the only R-heavy file. All slides and homework use **Python**.

### Schedule management
`course-info/schedule.csv` is the single source of truth for what appears on the schedule page. Add a row and set the `Publish` column to `x` to make it visible. Columns: `Publish, week, due, type, topic, reading, slides, video, assignment`.

### Slides
- Located in `slides/`, rendered as **Reveal.js** presentations
- Shared config in `slides/_metadata.yml` (author, footer, theme, `scrollable: true`, `echo: true`)
- Numbered sequentially: `00-welcome`, `01-big-picture`, …, `13-missing-data`
- Standard slide setup block:
  ```python
  import pandas as pd
  import numpy as np
  from plotnine import *
  from itables import show
  ```

### Homework
- Located in `hw/`, rendered as standard HTML documents
- Students submit via GitHub Classroom (linked in sidebar)

### Quizzes & Exams (separate repo)
- Stored in `/home/efriedlander/Dropbox/Teaching/MATH-4025-Quizzes/`
- Rendered to **PDF** (not HTML): `format: pdf` in the YAML front matter
- Files follow the pattern `Quiz-N.qmd` / `Quiz-N.pdf`

### Freeze behavior
- `execute: freeze: auto` is set globally in `_quarto.yml` — Quarto caches executed outputs in `_freeze/` and only re-executes changed files
- `index.qmd` overrides this with `freeze: false` so the schedule always re-renders

## Key Conventions

- **Tables:** Use `from itables import show` and call `show(df)` in Python blocks
- **Plots:** Prefer `plotnine` (ggplot2-style); `seaborn`/`matplotlib` also available
- **Missing data viz:** Use `import missingno as msno`
- **Data loading:** Use `pyhere` for robust relative paths; `pyreadr` for `.rds` files
- **Preprocessing/modeling:** Use `scikit-learn` Pipelines and `ColumnTransformer` to avoid data leakage; use `feature_engine.RareLabelEncoder` for lumping rare categories
- **Data:** Raw datasets live in `data/` (e.g., `ameshousing.csv`, `ameshousing_missing.csv`, `framingham.csv`)
- **Paths in slides:** Data is at `../data/` relative to the `slides/` directory

## Environment

- **Python:** `math-4025-sp26` conda env (Python 3.14, defined in `environment.yml`)
- **R:** Managed via `renv` (only needed for `index.qmd` schedule rendering)
- **Key Python packages:** `scikit-learn`, `pandas`, `numpy`, `plotnine`, `itables`, `missingno`, `feature_engine`, `statsmodels`, `islp`, `pyreadr`, `pyhere`, `polars`, `seaborn`

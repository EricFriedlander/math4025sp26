# MATH 4025 — StarFormation Project

**Group members:**
- [Name] — [email]
- [Name] — [email]
- [Name] — [email]
- [Name] — [email]

**Assigned target variable:** [fill in from Canvas]

**GitHub repository:** [URL]

---

## Project Overview

[Brief description of your analysis — fill this in as your project develops.]

---

## Repository Structure

```
data/                  Raw data files (do not modify)
GroupPlanningWorksheet.qmd   Group planning document (render this first!)
GroupPlanningWorksheet.html  Rendered worksheet (commit after rendering)
[your analysis files]  Add your .qmd analysis files here
```

Suggested organization for your analysis files:
- `eda.qmd` — Exploratory data analysis
- `modeling.qmd` — Model building and evaluation
- `slides/` — Presentation slides (can be a Quarto Reveal.js presentation)
- `executive-summary.qmd` — One-page executive summary

---

## How to Reproduce

1. Activate the course conda environment:
   ```
   conda activate math-4025-sp26
   ```

2. Render the group planning worksheet (do this first as a Quarto warm-up):
   ```
   quarto render GroupPlanningWorksheet.qmd
   ```

3. Render your analysis files:
   ```
   quarto render eda.qmd
   quarto render modeling.qmd
   ```

---

## Data

Data are from the MIRION catalog of Yellowballs (Wolf-Chase et al. 2025,
<https://iopscience.iop.org/article/10.3847/1538-4357/ae31f6>).

See the course website for:
- **Project Instructions** — full description of deliverables, rubric, and data variables
- **Data Wrangling Tips** — how to load and merge the raw data files

---

## Project Resources

- Project Instructions and Data Wrangling Tips: [course website — see Canvas for link]
- Quarto + Python Guide: [course website — see Canvas for link]
- GitHub Classroom: [see Canvas for assignment link]

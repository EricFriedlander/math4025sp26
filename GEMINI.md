# Gemini Context: Math 4025 (Spring 2026)

## Project Overview
This directory contains the source materials for the **Statistical Machine Learning** (Math 4025) course website for Spring 2026.

*   **Course:** Math 4025 (Spring 2026).
*   **Instructor:** Dr. Eric Friedlander.
*   **Institution:** College of Idaho.
*   **Primary Language:** Python (transitioned from R).
*   **Textbook:** ISLP (Introduction to Statistical Learning with Python).
*   **Live Site:** https://EricFriedlander.github.io/math4025sp26/

## Directory Structure
The root directory constitutes the active Quarto project.

*   `_archive/`: Legacy R-based materials from Spring 2025 (MAT 427). Use for reference only.
    *   `slides/`: Legacy lecture slides.
    *   `hw/`: Legacy homework assignments.
*   `course-info/`: Course-level documentation.
    *   `syllabus.qmd`: Course syllabus (updated with 2026 grading and URL).
    *   `overview.qmd`: Course overview (Instructor, Class Meetings).
    *   `support.qmd`: Support resources.
    *   `computing-access.qmd` & `computing-python-resources.qmd`: Computing setup and resources.
*   `slides/`: Lecture slides (migrated from archive and converted to Python).
    *   `00-welcome.qmd`, `01-big-picture.qmd`, `02-StatisticalLearning.qmd`.
    *   `_metadata.yml`: Shared configuration for all slides.
    *   `images/`: Slide-specific images.
*   `hw/`: Homework assignments (empty).
*   `data/`: Course datasets.
    *   `schedule.csv`: Source of truth for the course schedule.
*   `jobs/`: Job application assignments (empty).
*   `prepare/`: Preparation materials (empty).
*   `images/`: Static image assets (e.g., logo).
*   `_quarto.yml`: Main Quarto configuration.
*   `environment.yml`: Conda environment definition.
*   `index.qmd`: Homepage (displays the Course Schedule).

## Development & Usage

### 1. Tools
*   **Quarto:** Website builder.
*   **Python:** Primary programming language.
*   **Conda/Mamba:** Use the `math-4025-sp26` environment for all Python code in this workspace.
*   **VS Code:** Primary editor.

### 2. Automatic Deployment
The website is automatically rendered and published to GitHub Pages via a GitHub Action whenever changes are pushed to the `main` branch.
*   **Workflow file:** `.github/workflows/publish.yml`

### 3. Common Commands
Run these commands from the **project root**.

*   **Preview Site:**
    ```bash
    quarto preview
    ```
*   **Render Site:**
    ```bash
    quarto render
    ```
*   **Publish Site:**
    ```bash
    quarto publish gh-pages
    ```
*   **Render Specific File:**
    ```bash
    quarto render course-info/syllabus.qmd
    ```

### 3. Key Conventions
*   **Content:** Written in `.qmd` (Quarto Markdown).
*   **Code Blocks:** Use `{python}` blocks.
*   **Tables:** Use the `show` function from the `itables` library to display Python data frames.
*   **Plotting:** Use `plotnine` for visualizations (ggplot2 style).
*   **Data Loading:** Use `pyreadr` for `.rds` files and `pyhere` for robust relative paths.
*   **Configuration:** Global settings in `_quarto.yml`. Sidebar navigation is configured here.
*   **Paths:** Relative paths should ideally generally work, but be mindful of the folder structure (e.g., referencing images from `course-info/`).
*   **Data:** Store raw data in `data/`.

## Workflow Automation
The project utilizes the Gemini CLI for assistance.
*   **.gemini/prompts/**: Stores reusable prompts for common tasks.
    *   `sync-context.md`: Analyzes project changes, updates documentation, and handles git operations.

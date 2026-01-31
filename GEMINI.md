# Gemini Context: Math 4025 (Spring 2026)

## Project Overview
This directory contains the source materials for the **Statistical Machine Learning** (Math 4025) course website for Spring 2026.

*   **Course:** Math 4025 (Spring 2026).
*   **Instructor:** Dr. Eric Friedlander.
*   **Institution:** College of Idaho.
*   **Primary Language:** Python (transitioned from R).
*   **Textbook:** ISLP (Introduction to Statistical Learning with Python).

## Directory Structure
The root directory constitutes the active Quarto project.

*   `_archive/`: Legacy R-based materials from Spring 2025 (MAT 427). Use for reference only.
*   `course-info/`: Course-level documentation.
    *   `syllabus.qmd`: Course syllabus.
    *   `schedule.qmd`: Course schedule.
    *   `support.qmd`: Support resources.
    *   `computing-access.qmd` & `computing-python-resources.qmd`: Computing setup and resources.
*   `slides/`: Lecture slides (empty).
*   `hw/`: Homework assignments (empty).
*   `data/`: Course datasets (empty).
*   `jobs/`: Job application assignments (empty).
*   `prepare/`: Preparation materials (empty).
*   `images/`: Static image assets (e.g., logo).
*   `_quarto.yml`: Main Quarto configuration.
*   `index.qmd`: Homepage.

## Development & Usage

### 1. Tools
*   **Quarto:** Website builder.
*   **Python:** Primary programming language.
*   **VS Code:** Primary editor.

### 2. Common Commands
Run these commands from the **project root**.

*   **Preview Site:**
    ```bash
    quarto preview
    ```
*   **Render Site:**
    ```bash
    quarto render
    ```
*   **Render Specific File:**
    ```bash
    quarto render course-info/syllabus.qmd
    ```

### 3. Key Conventions
*   **Content:** Written in `.qmd` (Quarto Markdown).
*   **Code Blocks:** Use `{python}` blocks.
*   **Configuration:** Global settings in `_quarto.yml`. Sidebar navigation is configured here.
*   **Paths:** Relative paths should ideally generally work, but be mindful of the folder structure (e.g., referencing images from `course-info/`).
*   **Data:** Store raw data in `data/`.

## Workflow Automation
The project utilizes the Gemini CLI for assistance.
*   **.gemini/prompts/**: Stores reusable prompts for common tasks.
    *   `sync-context.md`: Analyzes project changes, updates documentation, and handles git operations.

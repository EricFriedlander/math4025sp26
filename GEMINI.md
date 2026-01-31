# Gemini Context: Math 4025 (Spring 2026) / MAT 427 (Spring 2025)

## Project Overview
This directory contains the source materials for a course website, likely for **Statistical Machine Learning**. 

**Note on Context:**
*   **Directory Name:** `math4025sp26` (Suggests Math 4025, Spring 2026).
*   **Configuration (`_quarto.yml`):** "MAT 427 - Spring 2025" (Suggests the content is from the previous year's iteration).
*   **Current Date:** Jan 2026.
*   **Inference:** The user is likely setting up the Spring 2026 course (`Math 4025`) using materials from Spring 2025 (`MAT 427`). The main project files currently reside in the `_archive/` directory.
*   **Key Change for 2026:** The course content is being reimplemented using **Python**, replacing the previous R-based curriculum.

## Directory Structure
The root directory contains the VS Code workspace and an `_archive` folder which houses the actual Quarto project.

*   `_archive/`: **Project Root**. Contains the Quarto configuration and source files (currently R-based).
    *   `_quarto.yml`: Main configuration file for the website (navigation, theme, metadata).
    *   `index.qmd`: Home page.
    *   `syllabus.qmd`: Course syllabus.
    *   `schedule.qmd`: Course schedule.
    *   `hw/`: Homework assignments (`.qmd` files).
    *   `data/`: Datasets used in the course (`.csv`, `.rds`, etc.).
    *   `images/`: Static image assets.
    *   `_site/`: Generated HTML output (do not edit directly).
    *   `_freeze/`: Quarto freeze files (cached computations).

## Development & Usage

### 1. Tools
*   **Quarto:** The publishing system used to build the website.
*   **Python:** The primary programming language for the new Spring 2026 content.
*   **R:** The legacy language used in the `_archive` materials.
*   **VS Code:** The editor environment.

### 2. Common Commands
Since the project source is in `_archive`, commands should be directed there.

*   **Preview Site:**
    ```bash
    quarto preview _archive
    ```
*   **Render Site:**
    ```bash
    quarto render _archive
    ```
*   **Render Specific File:**
    ```bash
    quarto render _archive/syllabus.qmd
    ```

### 3. Key Conventions
*   **Content:** Written in `.qmd` (Quarto Markdown).
*   **Code Blocks:** Transitioning from `{r}` blocks to `{python}` blocks for executable code.
*   **Configuration:** Global settings are in `_quarto.yml`. Page-specific settings are in the YAML header of each `.qmd` file.
*   **Data:** Store raw data in `_archive/data/`.
*   **Frozen Computations:** The `_freeze` directory stores the results of executed code.

## Workflow Automation
The project utilizes the Gemini CLI for assistance.
*   **.gemini/prompts/**: Stores reusable prompts for common tasks.
    *   `sync-context.md`: Analyzes project changes, updates documentation, and handles git operations.
# Sync Project Context and Push to GitHub

Review the current workspace to identify all file changes (staged and unstaged) since the last commit. Analyze these changes to understand what work has been done (by either you or the user).

Based on this analysis:
1. Update `GEMINI.md` to reflect the current project state, recording any new patterns, tools, or conventions revealed by the recent changes.
2. Run `conda env export > environment.yml` to store environment.
3. Stage all changes, including the updated `GEMINI.md`.
4. Create a concise, descriptive commit message that summarizes the actual work done (e.g., 'Refactor authentication logic and update docs', not just 'Update context').
5. Commit the changes.
6. Push the commit to the remote repository.
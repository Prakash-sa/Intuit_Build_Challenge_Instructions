# Contribution Guidelines

Thank you for your interest in improving the Intuit Build Challenge project! This document summarizes the expectations for new contributions so that the code base remains reliable and easy to maintain.

## Tooling Workflow

Before opening a pull request:

1. **Install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Format and lint**
   ```bash
   ruff check .
   ruff format .
   bandit -r assignment1 assignment2
   ```
3. **Static typing**
   ```bash
   mypy assignment1 assignment2
   ```
4. **Tests + coverage**
   ```bash
   pytest --cov=. --cov-report=term --cov-fail-under=80
   ```
5. **Security scan**
   ```bash
   pip-audit -r requirements.txt
   ```

All steps above are enforced in CI; ensure they pass locally to avoid churn.

## Coding Standards

- **Style**: follow Ruff/Black defaults (PEP 8 with automated formatting). Prefer descriptive names; keep functions focused on a single responsibility.
- **Typing**: new modules must include type hints; run `mypy` to guard against regressions.
- **Testing**: every feature or bug fix requires unit tests that cover both success and failure paths. Keep tests colocated in the `tests/assignment{1,2}` hierarchy mirroring module names.
- **Docs**: update `README.md` and relevant module docstrings whenever behavior changes. Complex logic should include brief inline comments.

## Git & PR Hygiene

- Use small, focused commits and descriptive messages.
- Rebase onto the latest `main` before opening a PR.
- Reference any related issues in the PR description.

By following these guidelines, we ensure the code base remains production-ready and welcoming to future contributors. 🎉

# Intuit Build Challenge (Python)

This repository contains production-grade solutions for the two required assignments using Python 3.11+ with comprehensive unit tests and documentation.

## Project Structure

- `assignment1/` – Producer/consumer package split into `containers.py`, `buffer.py`, `workers.py`, and `system.py` for clear responsibilities.
- `assignment2/` – Sales analytics package with dedicated `models.py`, `data_loader.py`, `analyzer.py`, and `reporting.py` modules.
- `tests/` – Pytest suites covering both assignments.
- `requirements.txt` – Minimal runtime/test dependency list (only `pytest`).
- `Dockerfile` / `docker-compose.yml` – Containerized workflows for demos, reports, and tests.
- `scripts/` – Tooling (e.g., copyright checker) referenced by CI.
- `CONTRIBUTING.md` – Coding standards and workflow expectations.

## Getting Started

1. **Install dependencies**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Honor the repository header policy:** every Python file must begin with `# Copyright (c) 2025 Intuit Build Challenge`. You can verify locally via:
   ```bash
   python3 scripts/check_copyright.py
   ```
3. **Run Assignment 1 demo**
   ```bash
   python3 -m assignment1.producer_consumer
   ```
4. **Run Assignment 2 analyses (prints all results to the console)**
   ```bash
   python3 -m assignment2.main
   ```
   The CLI uses `assignment2.data_loader.CSVSalesLoader` to populate `assignment2.analyzer.SalesAnalyzer`, then renders the consolidated report via `assignment2.reporting.SalesReport`.

## Docker Usage

Build the image (done automatically when using Compose):

```bash
docker compose build
```

Run the Assignment 1 demo inside a container:

```bash
docker compose run --rm assignment1-demo
```

Run the Assignment 2 report generator:

```bash
docker compose run --rm assignment2-report
```

Execute the full pytest + coverage suite in-container:

```bash
docker compose run --rm tests
```

## Sample Output (Assignment 2)

```
Total revenue by region:
  East: $6,460.00
  North: $11,425.00
  South: $5,500.00
  West: $9,090.00

Average discount by category:
  Services: 8.33%
  Software: 5.00%

Top products by revenue:
  Cloud Suite: $16,020.00
  Analytics Pro: $5,900.00
  Implementation: $4,500.00

Monthly sales summary:
  2025-01: orders=2, units=8, revenue=$8,130.00
  2025-02: orders=2, units=12, revenue=$6,125.00
  2025-03: orders=2, units=5, revenue=$9,060.00
  2025-04: orders=2, units=7, revenue=$3,400.00
  2025-05: orders=2, units=5, revenue=$5,760.00

Best salesperson by region:
  East: Riley ($4,560.00)
  North: Avery ($9,300.00)
  South: Jamie ($4,000.00)
  West: Morgan ($6,930.00)
```

## Testing

Execute the full automated suite at any time:

```bash
python3 -m pytest
```

The tests validate thread coordination invariants, buffer behavior, and every analytical query on the CSV dataset.

To mirror the CI gate locally (requires `pytest-cov`), run:

```bash
python3 -m pytest --cov=. --cov-report=term --cov-fail-under=80
```

Static typing and linting:

```bash
mypy assignment1 assignment2
ruff check . && ruff format --check .
bandit -r assignment1 assignment2
pip-audit -r requirements.txt
```

## Continuous Integration

Every push and pull request triggers `.github/workflows/tests.yml`, which installs dependencies, enforces the copyright header,
runs vulnerability scans via `pip-audit` and `bandit`, and executes the full pytest suite with an enforced 80% minimum coverage threshold.

## Architectural Notes

- **Assignment 1 (Producer/Consumer):** `ProducerConsumerSystem` accepts injectable source/destination/buffer instances and producer/consumer factories, so the orchestration layer adheres to Dependency Inversion and is easy to extend (e.g., swapping queue types or sentinels for different deployments).
- **Assignment 2 (Analytics):** `SalesAnalyzer` focuses solely on computations; data access lives in `CSVSalesLoader`, and presentation in `SalesReport`. This separation keeps Single Responsibility intact and allows alternative loaders/reporters to be plugged in without touching the analyzer.

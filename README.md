# 🐍 Python data structures, algorithms, and design patterns

![CI](https://img.shields.io/badge/tests-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.x-blue)
![TDD](https://img.shields.io/badge/methodology-TDD-purple)

A **Test‑Driven Development (TDD) playground** for Python.

Implementations of classic data structures and algorithms in Python with unit tests, complexity analysis, and practical examples.

## 🗂 Project Structure

```text
python-data-structures-and-algorithms
│
├── common/
├── data_structures/
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   ├── graph/
│   └── dynamic_programming/
│
├── tests/
├── benchmarks/
└── pyproject.toml
└── README.md
└── requirements.txt
```

* `src/` contains production code
* `tests/` mirrors the same structure and contains all unit tests

## 🛠 Requirements

* **Python** ≥ 3.x
* **pip**

### Recommended Tools

* [pytest](https://docs.pytest.org/) – test runner
* [coverage](https://coverage.readthedocs.io/) – code coverage
* [pytest-cov](https://pytest-cov.readthedocs.io/) – coverage integration for pytest
* [pylint](https://pylint.org/) – static code analysis

---

## 🚀 Getting Started

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

```bash
pip install -e .
pip install pytest
```

Update dependencies

```bash
python  -m pip install -r requirements.txt --upgrade
```

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Stop after the first failure:

```bash
pytest -x
```

Run a single test file:

```bash
pytest tests/algorithms/strings/test_stringutil.py
```

Run test from a venv:

```bash
.\.venv\Scripts\python.exe -m pytest
```

## 📊 Code Coverage

Run code coverage:

```bash
coverage run --source=src -m pytest
coverage report
```

Generate an HTML report:

```bash
coverage html
```

### Using pytest-cov (recommended)

`pytest-cov` also reports files without tests:

```bash
pytest --cov=src tests/
pytest --cov=src tests/ --cov-report=html
```

### Run tests and update coverage

```bash
pytest --cov=your_package --cov-report=term-missing --cov-report=html
```

## 🔍 Static Analysis (pylint)

Run pylint on source and tests (ignoring missing docstrings):

```bash
pylint src --disable=missing-docstring
pylint tests --disable=missing-docstring
```

## 📦 Managing Dependencies

Update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## Linting with pylint

Check code format with pylint:

```bash
pylint
```

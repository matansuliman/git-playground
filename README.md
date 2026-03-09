# SonarCloud Demo

![CI](https://github.com/matansuliman/sonarcloud-demo/actions/workflows/ci.yaml/badge.svg)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=matansuliman_sonarcloud-demo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=matansuliman_sonarcloud-demo)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=matansuliman_sonarcloud-demo&metric=coverage)](https://sonarcloud.io/summary/new_code?id=matansuliman_sonarcloud-demo)

A demonstration repository showcasing a simple Python calculator application integrated with **GitHub Actions** and **SonarCloud** for continuous integration and code quality analysis.

## Features

- **App Calculator**: A basic calculator module providing core mathematical operations:
  - `add(x, y)`: Returns the sum of `x` and `y`.
  - `devide(x, y)`: Returns the quotient of `x` divided by `y`.
- **Automated Testing**: Comprehensive unit tests written using `pytest`.
- **CI/CD Pipeline**: GitHub Actions workflow (`ci.yaml`) that:
  - Runs the test suite automatically on push/PR.
  - Generates coverage reports (`coverage.xml`).
  - Scans the codebase using SonarCloud to enforce code quality and security standards.

## Project Structure

```
.
├── app/                        # Application source code
├── tests/                      # Unit tests (pytest)
├── .github/workflows/ci.yaml   # GitHub Actions pipeline definition
├── sonar-project.properties    # SonarCloud configuration file
└── requirements.txt            # Python dependencies
```

## Local Development

### Prerequisites

- Python 3.11+
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/matansuliman/sonarcloud-demo.git
   cd sonarcloud-demo
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Running Tests

To run the test suite and generate a coverage report locally, use `pytest`:

```bash
pytest --cov=app --cov-report=xml
```

This command runs the tests inside the `tests/` directory and generates the `coverage.xml` file used by SonarCloud for code coverage analysis.
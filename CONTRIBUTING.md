# Contributing to Metis Agent Starter Kit

Thank you for your interest in contributing to the Metis Agent Starter Kit! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [Adding Examples](#adding-examples)
- [Adding Templates](#adding-templates)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Feature Requests](#feature-requests)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Set up the development environment
4. Create a branch for your changes
5. Make your changes
6. Test your changes
7. Submit a pull request

## Development Environment

### Prerequisites

- Python 3.8 or higher
- pip
- virtualenv or conda (recommended)

### Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the Metis Agent package:
   ```bash
   pip install metis-agent
   ```

3. Install development dependencies:
   ```bash
   pip install pytest black isort flake8
   ```

## Coding Standards

We follow these coding standards:

- **PEP 8**: For Python code style
- **Type Hints**: Use type hints for function parameters and return values
- **Docstrings**: Use Google-style docstrings
- **Imports**: Sort imports using isort
- **Formatting**: Format code using Black

Run the following commands to check your code:

```bash
# Format code
black .
isort .

# Check for errors
flake8 .
```

## Pull Request Process

1. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them with descriptive commit messages:
   ```bash
   git commit -m "Add feature: your feature description"
   ```

3. Push your branch to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Submit a pull request to the main repository

5. Address any feedback from reviewers

6. Once approved, your pull request will be merged

## Adding Examples

When adding new examples:

1. Create a new Python file in the `examples` directory
2. Follow the existing example structure
3. Include detailed comments explaining the code
4. Update the README.md to mention your new example
5. Ensure your example works with the latest version of Metis Agent

## Adding Templates

When adding new templates:

1. Create a new directory in the `templates` directory
2. Include a main Python file with the template implementation
3. Add any necessary supporting files
4. Include a README.md file explaining how to use the template
5. Update the main README.md to mention your new template

## Documentation

Update documentation for any changes you make:

- Update docstrings for modified functions and classes
- Update README.md if necessary
- Add examples for new features

## Issue Reporting

When reporting issues, please include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Environment information (OS, Python version, package versions)
- Any relevant logs or error messages

## Feature Requests

For feature requests, please include:

- A clear and descriptive title
- A detailed description of the proposed feature
- Any relevant examples or use cases
- If possible, a rough implementation plan

Thank you for contributing to the Metis Agent Starter Kit!
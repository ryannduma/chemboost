# Contributing to ChemBoost

First off, thank you for considering contributing to ChemBoost! It's people like you that make ChemBoost such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include any error messages

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* Use a clear and descriptive title
* Provide a step-by-step description of the suggested enhancement
* Provide specific examples to demonstrate the steps
* Describe the current behavior and explain which behavior you expected to see instead
* Explain why this enhancement would be useful

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Process

1. Set up your development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate  # Windows
   pip install -e ".[dev]"
   pre-commit install
   ```

2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```

3. Make your changes:
   * Write meaningful commit messages
   * Add tests for new functionality
   * Update documentation as needed

4. Run the test suite:
   ```bash
   pytest
   ```

5. Submit a pull request

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Python Styleguide

* Follow PEP 8
* Use type hints for function arguments and return values
* Write docstrings for all public methods and functions
* Use meaningful variable names
* Keep functions focused and small

### Documentation Styleguide

* Use Markdown for documentation
* Reference functions and classes using backticks
* Include code examples when useful
* Keep explanations clear and concise

## Additional Notes

### Issue and Pull Request Labels

* `bug`: Something isn't working
* `enhancement`: New feature or request
* `documentation`: Improvements or additions to documentation
* `good first issue`: Good for newcomers
* `help wanted`: Extra attention is needed

## Recognition

Contributors will be recognized in the project's README and release notes.

## Questions?

Feel free to contact the maintainers if you have any questions. 
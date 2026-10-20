# Contributing

Thank you for your interest in improving Mini RAG Python.

## Development setup

1. Fork or clone the repository.
2. Create a virtual environment.
3. Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

4. Run the test suite:

```bash
pytest -v
```

## Suggested contribution workflow

Create a branch:

```bash
git checkout -b feature/my-improvement
```

Make your changes, run the tests, and commit:

```bash
git add .
git commit -m "Add my improvement"
```

Then push your branch and create a pull request.

## Code guidelines

- Keep functions small and readable.
- Add docstrings for public functions and classes.
- Add or update tests when changing behavior.
- Never commit passwords, API keys, or secrets.

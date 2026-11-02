# 0005. Code style: ruff

- Status: Accepted
- Date: 2026-11-02

## Context

The project has two kinds of code:

- Generated code in `src/ubl_bindings/v*/`. xsdata formats it with its own ruff configuration and a line length of 79.
- Hand-written code: `src/ubl_bindings/__init__.py`, `scripts/` and `tests/`.

The hand-written code had no formatter and no linter. The `dev` group already installs ruff, because `xsdata[cli]` requires it.

## Options

1. ruff for formatting and linting.
2. Black, isort and flake8: the same result with three tools.
3. No tools: style by review only.

## Decision

Option 1, with this configuration in `pyproject.toml`:

- Line length 120. The longest line of the existing code has 102 characters.
- Lint rules: E, F, W, I, UP, B, SIM, PTH, RUF.
- The target Python version comes from `requires-python`.
- The generated code is excluded. We do not edit generated code. See ADR 0001.
- The ruff version is pinned in the `dev` group, so that a new ruff version does not change the result of the CI.

We do not use a type checker for now. The generated classes have type hints. The hand-written code is small.

## Consequences

- `uv run ruff format` formats the code. `uv run ruff check` finds lint errors.
- The CI fails if the code is not formatted or has lint errors.
- ruff also formats the Python examples in Markdown files.
- To update ruff, change the pin and fix the new findings in one commit.

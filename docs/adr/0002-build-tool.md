# 0002. Build tool: uv with uv_build

- Status: Accepted
- Date: 2026-11-02

## Context

The project needs two tools:

- A build backend. It makes the wheel and the source distribution from `pyproject.toml`.
- A workflow tool. It manages the virtual environment, the dependencies and the publication to PyPI.

The library is pure Python. It contains generated code and the UBL XSD schemas. The function `ubl_bindings.validate()` reads the schemas at runtime. Thus the schemas must be in the wheel.

## Options

Build backends:

1. uv_build: the default backend of `uv init`. Simple configuration, but it requires a strict layout and cannot map a folder from outside the package into the wheel.
2. hatchling: standard configuration. It can copy a folder from outside the package into the wheel with `force-include`.
3. setuptools: known by most maintainers, but it needs more configuration for package data.
4. flit-core, poetry-core, pdm-backend: few options for data files, or tied to their own workflow tool.

Workflow tools:

1. uv: environments, lock file, build and publication in one tool.
2. hatch: similar to uv, with test matrices.
3. Poetry or PDM: no advantage for this project.
4. pip, build and twine: no extra tool, but more manual steps.

## Decision

We use uv as the workflow tool and uv_build as the build backend.

We keep the schemas inside the package, at `src/ubl_bindings/schemas/<release>/xsd/`. Thus uv_build puts them into the wheel without extra configuration.

## Consequences

- One tool for the full workflow: `uv sync`, `uv run`, `uv build` and `uv publish`.
- `pyproject.toml` uses only standard fields and the `[tool.uv]` sections.
- The schemas are next to the code that reads them. The library finds them relative to its own files.
- Each release adds its schemas (5 to 7 MB uncompressed) to the wheel.
- If we need a file layout that uv_build does not support, we change the backend to hatchling. This change does not affect the workflow with uv.

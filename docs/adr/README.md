# Architecture Decision Records

This folder contains the architecture decision records (ADR) of this project. An ADR records one decision, the reasons for it and its consequences.

## Format

- One file for each decision: `NNNN-short-title.md`.
- Sections: _Status_, _Context_, _Options_, _Decision_, _Consequences_.
- Status values: "Proposed", "Accepted", "Superseded by NNNN".
- Do not change the decision in an accepted ADR. Write a new ADR that supersedes it.

## Records

| No.  | Title                                                          | Status   |
| ---- | -------------------------------------------------------------- | -------- |
| 0001 | [Code generator: xsdata](0001-code-generator.md)               | Accepted |
| 0002 | [Build tool: uv with uv_build](0002-build-tool.md)             | Accepted |
| 0003 | [Project name: ubl-bindings](0003-project-name.md)             | Accepted |
| 0004 | [No packages for UBL 1.0 and UBL 2.0](0004-ubl-1.0-and-2.0.md) | Accepted |
| 0005 | [Code style: ruff](0005-code-style.md)                         | Accepted |
| 0006 | [Versioning: SemVer](0006-versioning.md)                       | Accepted |

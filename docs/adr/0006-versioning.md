# 0006. Versioning: SemVer

- Status: Accepted
- Date: 2026-11-02

## Context

Users need to know if an update can break their code. The public API has two parts:

- The functions and constants in `ubl_bindings`, for example `parse()`, `validate()`, `RELEASES` and `LATEST`.
- The generated classes in `ubl_bindings.v*` and the names of their fields.

A new version of xsdata or a change in `.xsdata.xml` can rename generated classes or fields. For users, this is a breaking change, also if no hand-written code changes.

One package contains all UBL releases. Thus the version of the package cannot be the version of UBL.

uv_build reads the version only from `pyproject.toml`. It cannot take the version from a git tag.

## Options

1. Semantic Versioning (SemVer).
2. Calendar Versioning (CalVer), for example `26.11`, like xsdata.

## Decision

Option 1: [SemVer 2.0](https://semver.org/).

| Change                                                                   | Version |
| ------------------------------------------------------------------------ | ------- |
| A function, a generated class or a field is renamed or removed           | MAJOR   |
| A UBL release is removed                                                 | MAJOR   |
| A new UBL release, a new function or support for a new Python version    | MINOR   |
| Support for a Python version that has reached its end of life is removed | MINOR   |
| A bug fix, or a change to the documentation or the tests                 | PATCH   |

A new UBL release also changes `LATEST`, the default release of `parse()` and `validate()`. Then `parse()` returns classes from a different package. We treat this as a MINOR change. The README tells users to give `release=` if their code depends on one release.

Before version 1.0.0, a breaking change increases MINOR, and all other changes increase PATCH. We release 1.0.0 when the API is stable.

The version is in `pyproject.toml`. To change it, use `uv version --bump major|minor|patch`. Each release has a git tag `vX.Y.Z`.

Each release has an entry in `CHANGELOG.md` in the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.

## Consequences

- A user can pin `ubl-bindings>=X.Y,<X+1` to get updates without breaking changes.
- Each update of xsdata needs a review of the diff of the generated code. If a class or field name changes, the next release is MAJOR.
- The changelog marks breaking changes, so that users know what to change.

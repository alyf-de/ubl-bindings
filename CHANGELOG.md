# Changelog

All notable changes to this project are in this file. The format is [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The project uses [Semantic Versioning](https://semver.org/). See [ADR 0006](docs/adr/0006-versioning.md).

## [Unreleased]

### Added

- Best-effort parsing: `parse(source, strict=False)` reads documents that are not valid. Missing mandatory elements become `None`. Unknown elements and attributes are skipped.

### Changed

- **Breaking:** `parse()` is strict by default. It raises `ValueError` for an unknown attribute or a value that cannot be converted. Before, it skipped unknown attributes and kept such values as strings.

### Fixed

- `parse()` raises `ValueError` with the name of the missing element if a mandatory element is missing. Before, it raised `TypeError`.

## [0.1.0] - 2026-11-02

### Added

- Generated classes for all document types of UBL 2.1, 2.2, 2.3, 2.4 and 2.5.
- `parse()`, `validate()`, `to_xml()` and `detect_version()`.
- The XSD schemas of each release, for validation.
- Each release reads UBL 2.0 documents and documents of older 2.x releases.

[Unreleased]: https://github.com/alyf-de/ubl-bindings/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/alyf-de/ubl-bindings/releases/tag/v0.1.0

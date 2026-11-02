# 0003. Project name: ubl-bindings

- Status: Accepted
- Date: 2026-11-02

## Context

The project needs a distribution name on PyPI and an import name.

These PyPI names are taken:

- `python-ubl`: a UBL 2.1 library for invoices and credit notes, with Peppol support. Its import name is `ubl`.
- `ubl` and `pyubl`: placeholders without files.

If two installed distributions use the same import name, one overwrites the other. Thus our import name must not be `ubl`.

OASIS treats its name and the names and abbreviations of its specifications as trademarks. This includes "OASIS", "UBL" and "Universal Business Language". The [OASIS trademark policy](https://www.oasis-open.org/policies-guidelines/trademark/) says:

- OASIS welcomes references to its specifications and implementations of them.
- The marks refer to OASIS and its official outputs.
- A product name that contains an OASIS mark must show an acknowledgement notice.

A name with "OASIS", for example `oasis-ubl`, looks like an official OASIS product. A name with "UBL" is common practice for implementations, for example python-ubl and ph-ubl.

## Decision

- Distribution name: `ubl-bindings`.
- Import name: `ubl_bindings`.

"XML data bindings" is the usual term for classes generated from an XML schema. The name tells what the library is: a full mapping of the UBL schemas, not a helper for one document type.

We show the OASIS trademark acknowledgement in the README and in `NOTICE`.

## Consequences

- `pip install ubl-bindings`, then `import ubl_bindings`.
- The library can be installed next to python-ubl.
- The repository uses the same name: `ubl-bindings`.

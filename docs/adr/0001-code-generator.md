# 0001. Code generator: xsdata

- Status: Accepted
- Date: 2026-11-02

## Context

This library makes its Python classes from the official UBL XSD schemas. We need a generator that:

1. Reads the unmodified XSD files of each UBL release.
2. Makes classes for all document types of a release (65 in UBL 2.1, 101 in UBL 2.5).
3. Keeps the shared schemas (for example `UBL-CommonAggregateComponents`) in shared modules.
4. Parses and exports documents without data loss.
5. Makes code that a maintainer can read and debug.

### A property of the UBL schemas

UBL uses the same local names in different namespaces. Examples:

- The type `AmountType` exists in `cbc`, `udt` and `cct`. `cbc:AmountType` extends `udt:AmountType`, which extends `cct:AmountType`.
- `cbc:PriceType` is an element (a code for the price type). `cac:PriceType` is the complex type of the `cac:Price` element.
- `cbc:PartyType` is an element. `cac:PartyType` is the complex type of the `cac:Party` element.

A generator that ignores namespaces mixes up these names.

### Earlier prototype

An earlier internal prototype (February 2025) used xsdata 24.12 with UBL 2.1. It had these properties:

- A configuration file `.xsdata.xml` with `Structure` set to "namespaces". The generator makes one module for each XML namespace.
- 131 modules with 83,000 lines in total, for all 65 document types.
- A script that parsed the example invoice and exported it again.
- No tests and no validation of the output.

## Options

1. [generateDS](https://www.davekuhlman.org/generateDS.html) (MIT license).
2. [xsdata](https://xsdata.readthedocs.io/) (MIT license).
3. Write our own generator, or fork one of the generators above.

## Experiment

We tested generateDS 2.44.3 and xsdata 26.10 with Python 3.14 and lxml 6.1.3. For each release, we used the official examples in the `xml/` folder of the release ZIP. For each example, we did these steps:

1. Parse the example with the generated code.
2. Export the result to XML.
3. Validate the output against the XSD of the same release.
4. Compare the output with the input: element names, attributes and text.

### generateDS

- On the unmodified UBL 2.1 schemas, generateDS stops with "Extension/restriction recursion detected" for `TextType` and `AmountType`. The cause is the name clash between `cbc`, `udt` and `cct`.
- As a workaround, we added a prefix to the type names in the `cct` and `udt` schemas. After this change, generateDS made code for UBL 2.1.
- The same workaround does not work for UBL 2.5. In UBL 2.5, the qualified data types also clash with `cbc`, for example `AllowanceChargeReasonCodeType`. Each release needs its own changes to the schemas.
- The `--one-file-per-xsd` mode makes Python files that do not compile. The import lines contain the XSD file names, for example `from .UBL-Invoice-2.1 import InvoiceType`.
- Thus each document type needs one file that contains all shared schemas. The file for the **Invoice** has 173,000 lines (8.6 MB). The files for the 39 document types with examples have 332 MB in total.
- The generated code mixes up the clashing element names. For example, it parses `cac:SenderParty` into the class for `cbc:PartyType`. All child elements of the party are lost.

### xsdata

- xsdata reads the unmodified schemas of UBL 2.1 and UBL 2.5.
- It makes one module for each namespace. The document types share these modules.
- Round trip: all examples parse, and all output is valid. Some output values have a different lexical form, but the same value:
  - `12:00:01.000` becomes `12:00:01`.
  - `11:30:00.0Z` becomes `11:30:00Z`.
  - `0` becomes `false`.
  - Line breaks in base64 data are removed.

### Results

|                                    | generateDS 2.44.3                    | xsdata 26.10                        |
| ---------------------------------- | ------------------------------------ | ----------------------------------- |
| Unmodified UBL 2.1 schemas         | Fails                                | Works                               |
| UBL 2.5 schemas                    | Fails, also with the 2.1 workaround  | Works                               |
| Shared modules                     | No (invalid Python)                  | Yes, one module for each namespace  |
| Size, UBL 2.1                      | 8.6 MB for each document type        | 4.0 MB, 60,000 lines, 65 types      |
| Size, UBL 2.5                      | Not tested                           | 5.9 MB, 87,000 lines, 101 types     |
| Generation time, UBL 2.1           | About 1 s for each document type     | 4.4 s for all document types        |
| Round trip, UBL 2.1 (56 examples)  | 3 equal, 34 data lost, 16 invalid, 3 not well-formed | 32 equal, 24 lexical changes only |
| Round trip, UBL 2.5 (75 examples)  | Not tested                           | 48 equal, 27 lexical changes only   |
| Runtime dependencies               | lxml, six                            | xsdata, typing-extensions (lxml optional) |
| Generated code                     | Classes with getters and setters, `valueOf_` | Dataclasses with type hints, snake_case fields |

## Decision

We use xsdata.

- We keep one `.xsdata.xml` configuration in the repository. It sets `Structure` to "namespaces", as in the prototype.
- We pin the xsdata version that generates the code.
- We do not fork or write a generator now. If xsdata blocks us later, we first try an xsdata plugin or a fork. We write our own generator only if both fail.

## Consequences

- The library has a runtime dependency on xsdata. xsdata parses and exports the generated dataclasses.
- Export changes the lexical form of some values (see above). The values do not change. But a changed document has a different byte sequence, so an XML signature on it is no longer valid. To verify a signature, use the original bytes.
- All UBL 2.x releases use the same namespaces. Thus each release needs its own Python package, for example `ubl_bindings.v2_1` and `ubl_bindings.v2_5`. We set this with the `Package` option for each release.
- With "namespaces" as the structure, import paths are long, for example `ubl_bindings.v2_1.oasis.names.specification.ubl.schema.xsd.invoice_2`. Short imports can come later from hand-written modules.
- A new xsdata version can change the generated code. We update xsdata on purpose, generate the code again and review the diff.
- The round trip from the experiment becomes the main test of the test suite.

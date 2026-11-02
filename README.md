# ubl-bindings

Python data bindings for all [UBL](https://www.oasis-open.org/committees/ubl/) document types. The classes are generated from the official XSD schemas. Use them to read, write and validate UBL documents.

> **Status:** alpha. The API can change.

## Why this library

- **All document types.** UBL 2.1 has 65 document types and UBL 2.5 has 101. All of them have classes, not only the **Invoice** and the **Credit Note**. This includes, for example, **Order**, **Despatch Advice** and **Catalogue**.
- **All current releases.** UBL 2.1, 2.2, 2.3, 2.4 and 2.5 are supported. To add a release, generate its code and run the tests.
- **Complete.** Each element and attribute of the schemas has a field in a class. Data that a hand-written model does not know is not lost.
- **Tested with the official examples.** Each example document of each release is parsed, exported, validated and compared with the input. The examples cover about half of the document types, for example 56 of 101 in UBL 2.5.
- **XSD validation included.** The schemas are part of the package.
- **No profile rules.** The library does not add the rules of Peppol, XRechnung or EN 16931. You can build such rules on top of it.

The classes are close to the schemas. Thus the API is more verbose than the API of a hand-written model for one document type.

## Supported UBL releases

| Release | Status         | Document types | Python package         | Specification                                                |
| ------- | -------------- | -------------- | ---------------------- | ------------------------------------------------------------ |
| 2.1     | OASIS Standard | 65             | `ubl_bindings.v2_1`    | [UBL-2.1.html](https://docs.oasis-open.org/ubl/UBL-2.1.html) |
| 2.2     | OASIS Standard | 81             | `ubl_bindings.v2_2`    | [UBL-2.2.html](https://docs.oasis-open.org/ubl/UBL-2.2.html) |
| 2.3     | OASIS Standard | 91             | `ubl_bindings.v2_3`    | [UBL-2.3.html](https://docs.oasis-open.org/ubl/UBL-2.3.html) |
| 2.4     | OASIS Standard | 93             | `ubl_bindings.v2_4`    | [UBL-2.4.html](https://docs.oasis-open.org/ubl/UBL-2.4.html) |
| 2.5     | OASIS Standard | 101            | `ubl_bindings.v2_5`    | [UBL-2.5.html](https://docs.oasis-open.org/ubl/UBL-2.5.html) |

UBL 2.0 has no package of its own. Each release from 2.1 on can read UBL 2.0 documents. The tests do this with the official 2.0 examples. To write a UBL 2.0 document, do not use elements that were added after 2.0. `validate()` cannot do a check against the 2.0 schemas.

UBL 1.0 is not supported. It uses different namespaces and a different structure. See [ADR 0004](docs/adr/0004-ubl-1.0-and-2.0.md).

## Installation

```sh
pip install ubl-bindings
```

The library supports Python 3.10 and later.

## Usage

### Read a document

```python
import ubl_bindings

invoice = ubl_bindings.parse("invoice.xml")

print(invoice.id.value)  # "TOSL108"
print(invoice.legal_monetary_total.payable_amount.value)  # Decimal("729")
```

`parse()` returns an instance of the class for the root element, for example `Invoice` or `Order`. By default it uses the latest release. Each release can read the documents of all older 2.x releases.

To use a specific release:

```python
invoice = ubl_bindings.parse("invoice.xml", release="2.1")
```

A new version of this library can add a new UBL release. Then the default release changes, and `parse()` returns classes from a different package. If your code depends on the classes of one release, give `release=`.

### Read a document that is not valid

By default, `parse()` is strict. It raises `ValueError` if the document does not fit the classes, for example if a mandatory element is missing or an element is unknown. Strict parsing is not a full validation. For example, it accepts elements in the wrong order. Use `validate()` to find all errors.

To read as much as possible from a document that is not valid, for example a received invoice, use best-effort mode:

```python
invoice = ubl_bindings.parse("invoice.xml", strict=False)
```

In best-effort mode:

- A missing mandatory element or attribute is `None`.
- Unknown elements and attributes are skipped. Their data is lost.
- A value that cannot be converted, for example the amount `abc`, stays a string. xsdata shows a `ConverterWarning`.

### Write a document

```python
from decimal import Decimal

from xsdata.models.datatype import XmlDate

import ubl_bindings
from ubl_bindings.v2_5 import (
    AccountingCustomerParty,
    AccountingSupplierParty,
    Id,
    Invoice,
    InvoiceLine,
    IssueDate,
    Item,
    LegalMonetaryTotal,
    LineExtensionAmount,
    PayableAmount,
)

invoice = Invoice(
    id=Id(value="INV-1"),
    issue_date=IssueDate(value=XmlDate(2026, 11, 2)),
    accounting_supplier_party=AccountingSupplierParty(),
    accounting_customer_party=AccountingCustomerParty(),
    legal_monetary_total=LegalMonetaryTotal(
        payable_amount=PayableAmount(value=Decimal("100.00"), currency_id="EUR"),
    ),
    invoice_line=[
        InvoiceLine(
            id=Id(value="1"),
            line_extension_amount=LineExtensionAmount(value=Decimal("100.00"), currency_id="EUR"),
            item=Item(),
        ),
    ],
)

xml = ubl_bindings.to_xml(invoice)
```

`to_xml()` uses the usual prefixes `cac`, `cbc` and `ext`.

### Validate a document

```python
errors = ubl_bindings.validate("invoice.xml")  # [] if the document is valid
```

The validation uses the XSD schemas only. It does not check business rules.

### Find the release of a document

All UBL 2.x releases use the same XML namespaces. A document can state its release in the optional `cbc:UBLVersionID` element:

```python
ubl_bindings.detect_version("invoice.xml")  # "2.1", or None if the element is missing
```

### Export changes the form of some values

The value stays the same, but the text can change. For example, `12:00:01.000` becomes `12:00:01` and `0` becomes `false`. Thus an XML signature on an exported document is not valid. To check a signature, use the original bytes.

Export also removes the `xsi:schemaLocation` attribute. This attribute is only a hint for tools.

## Out of scope

- Business rules that are not in the XSD schemas, for example EN 16931, XRechnung or Peppol Schematron rules.
- Other syntaxes, for example UN/CEFACT Cross Industry Invoice (CII).
- Conversion between UBL releases.

## Development

We use [uv](https://docs.astral.sh/uv/). See [ADR 0002](docs/adr/0002-build-tool.md).

```sh
uv sync                 # make the environment
uv run pytest           # run the tests
uv run ruff format      # format the code
uv run ruff check       # find lint errors
uv build                # make the wheel and the source distribution
```

The ruff configuration is in `pyproject.toml`. See [ADR 0005](docs/adr/0005-code-style.md).

### Versioning

We use [Semantic Versioning](https://semver.org/). A renamed generated class or field is a breaking change. A new UBL release is a minor change. See [ADR 0006](docs/adr/0006-versioning.md).

To make a release:

1. Run `uv version --bump major|minor|patch`.
2. Move the entries under "Unreleased" in `CHANGELOG.md` to a section for the new version.
3. Commit, then add the tag `vX.Y.Z`.
4. Push the commit and the tag. The release workflow checks that the tag is the version in `pyproject.toml`, then publishes the package to PyPI.

### Layout

```
ubl-bindings/
├── src/ubl_bindings/
│   ├── __init__.py       # parse, validate, to_xml, detect_version (hand-written)
│   ├── schemas/
│   │   ├── 2.1/xsd/      # XSD files from the official release ZIP
│   │   ├── ...
│   │   └── 2.5/xsd/
│   ├── v2_1/             # generated code for UBL 2.1
│   ├── ...
│   └── v2_5/             # generated code for UBL 2.5
├── .xsdata.xml           # generator configuration
├── scripts/
│   └── generate.py       # runs the generator for one or all releases
├── tests/
│   └── examples/         # example documents from each release ZIP
└── docs/adr/             # architecture decision records
```

Rules for this layout:

- Code in `src/ubl_bindings/v*/` is generated. Do not edit it by hand. Change the generator configuration, then generate again.
- The schemas are part of the package, because `validate()` reads them at runtime. We keep only the `xsd/` folder of each release ZIP.

### Code generation

We use [xsdata](https://xsdata.readthedocs.io/) to make Python dataclasses from the XSD schemas. See [ADR 0001](docs/adr/0001-code-generator.md). xsdata makes one module for each XML namespace. All document types of a release share these modules.

The version of xsdata in the `dev` dependency group is pinned. To update it, change the pin, generate the code for all releases and review the diff.

```sh
uv run scripts/generate.py 2.5   # generate the code for one release
uv run scripts/generate.py       # generate the code for all releases
```

### Add a new UBL release

1. Download the release ZIP from `https://docs.oasis-open.org/ubl/os-UBL-<release>/UBL-<release>.zip`.
2. Copy the `xsd/` folder of the ZIP to `src/ubl_bindings/schemas/<release>/xsd/`.
3. Copy the `xml/` folder of the ZIP to `tests/examples/<release>/`.
4. Add the release to `RELEASES` in `src/ubl_bindings/__init__.py`.
5. Run `uv run scripts/generate.py <release>`.
6. Run `uv run pytest`.
7. Add the release to the table in this README.

### Tests

The main test is a round trip over the official examples. For each release and each example of the same or an older release, the test does these steps. The UBL 2.0 examples count as an older release.

1. Parse the example.
2. Export the result to XML.
3. Validate the output against the XSD schemas of the release.
4. Compare the output with the input. The comparison ignores differences in the lexical form of a value and the `xsi:schemaLocation` attribute.

Each new release brings its own examples. Thus the test suite grows without new test code.

Other tests:

- `tests/test_api.py` tests the public functions.
- `tests/test_readme.py` runs the example in "Write a document" and validates the result.

The CI workflow runs the tests on the oldest supported and the latest Python version. It also generates the code for all releases again and fails if the result is not the committed code.

## License

The code of this project is licensed under the [MIT License](LICENSE).

The UBL schemas, the UBL examples and the code generated from them come from OASIS, W3C and ETSI. Their own licenses apply. See [NOTICE](NOTICE).

"OASIS", "UBL" and "Universal Business Language" are trademarks of OASIS, the open standards consortium where the UBL specification is owned and developed. UBL is a copyrighted © work of OASIS Open. All rights reserved. This project is not an official OASIS product.

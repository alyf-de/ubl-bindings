# python-ubl

A Python library to read, write and validate [OASIS UBL](https://www.oasis-open.org/committees/ubl/) documents.

> **Status:** early design. This README describes the plan. Nothing is implemented yet.

## Goals

- Support all document types of each supported UBL release, not only the **Invoice**.
- Generate the code from the official XSD schemas. Do not write the data classes by hand.
- Add a new UBL release with one command and a test run.
- Keep the generated code in the repository, so that users do not need the generator.

## Supported UBL releases

| Release | Status          | Document types | Specification                                               |
| ------- | --------------- | -------------- | ----------------------------------------------------------- |
| 2.1     | OASIS Standard  | 65             | [UBL-2.1.html](https://docs.oasis-open.org/ubl/UBL-2.1.html) |
| 2.5     | OASIS Standard  | 101            | [UBL-2.5.html](https://docs.oasis-open.org/ubl/UBL-2.5.html) |

Other 2.x releases (2.2, 2.3, 2.4) use the same process. We add them when a user needs them.

## Background: UBL versions and namespaces

All UBL 2.x releases use the same XML namespaces, for example `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`. The namespace does not tell you the minor version.

A document can state its version in the optional `cbc:UBLVersionID` element. If this element is missing, the library cannot know the version from the XML alone.

Each minor release is backward compatible. A valid UBL 2.1 document is also valid against the UBL 2.5 schemas. But a UBL 2.5 document can contain elements that UBL 2.1 does not know.

Because of this, the library keeps one separate package for each release. The caller selects the release. A helper reads `cbc:UBLVersionID` when the caller does not know the release.

## Planned layout

```
python-ubl/
├── src/ubl/
│   ├── __init__.py       # version detection and shared helpers (hand-written)
│   ├── schemas/
│   │   ├── 2.1/xsd/      # XSD files, copied from the official release ZIP
│   │   └── 2.5/xsd/
│   ├── v2_1/             # generated code for UBL 2.1
│   └── v2_5/             # generated code for UBL 2.5
├── .xsdata.xml           # generator configuration
├── scripts/
│   └── generate.py       # runs the generator for one release
└── tests/
    └── examples/         # official example documents from each release ZIP
```

Rules for this layout:

- Code in `src/ubl/v*/` is generated. Do not edit it by hand. Change the generator or its configuration, then generate again.
- Hand-written code stays in `src/ubl/__init__.py` and a small number of modules next to it.
- Each `src/ubl/schemas/<release>/` folder contains only the files that the generator and the validator need. The schemas are part of the package, because `ubl.validate()` reads them at runtime. The full release ZIP also contains PDF, HTML and code list files. We do not keep these.

## Code generation

We use [xsdata](https://xsdata.readthedocs.io/) to make Python dataclasses from the XSD schemas. xsdata also parses XML into these dataclasses and exports them to XML. [ADR 0001](docs/adr/0001-code-generator.md) compares xsdata with generateDS.

The UBL schemas share many common files, for example `UBL-CommonAggregateComponents-2.xsd` and `UBL-CommonBasicComponents-2.xsd`. xsdata makes one module for each XML namespace. All document types of a release use these shared modules.

### Add a new UBL release

1. Download the release ZIP from `https://docs.oasis-open.org/ubl/os-UBL-<release>/UBL-<release>.zip`.
2. Copy the `xsd/` folder of the ZIP to `src/ubl/schemas/<release>/xsd/`.
3. Copy the `xml/` folder of the ZIP to `tests/examples/<release>/`.
4. Run `uv run scripts/generate.py <release>`.
5. Run the tests.
6. Add the release to the table in this README.

## Planned usage

The API below is a draft. Names can change when we see the generated code.

```python
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from ubl.v2_5 import Invoice

invoice = XmlParser().parse("invoice.xml", Invoice)
print(invoice.id.value)

xml = XmlSerializer().render(invoice)
```

Detect the release of an unknown document:

```python
import ubl

release = ubl.detect_version("invoice.xml")  # "2.1", "2.5" or None
```

Validate a document against the XSD schemas of a release:

```python
ubl.validate("invoice.xml", release="2.1")
```

## Tests

The main test is a round trip over the official examples of each release:

1. Parse each example file with the generated code.
2. Export the result to XML.
3. Validate the output against the XSD schemas of the same release.
4. Compare the output with the input.

Each new release brings its own examples. Thus the test suite grows without new test code.

## Out of scope

- Business rules that are not in the XSD schemas, for example EN 16931, XRechnung or Peppol Schematron rules.
- Other syntaxes, for example UN/CEFACT Cross Industry Invoice (CII).
- Conversion between UBL releases.

## Development

The library supports Python 3.10 and later.

We use [uv](https://docs.astral.sh/uv/) for the environment, the build and the publication. See [ADR 0002](docs/adr/0002-build-tool.md).

```sh
uv sync      # make the environment
uv run ...   # run a command in the environment
uv build     # make the wheel and the source distribution
```

## License

The code of this project is licensed under the [MIT License](LICENSE).

The UBL schemas, the UBL examples and the code generated from them come from OASIS, W3C and ETSI. Their own licenses apply. See [NOTICE](NOTICE).

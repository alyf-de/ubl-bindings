"""Read, write and validate UBL documents.

The generated classes for each release are in `ubl_bindings.v2_1`, `ubl_bindings.v2_5`, ...
This module adds shortcuts for the common tasks.
"""

import dataclasses
import importlib
from functools import cache
from os import PathLike
from pathlib import Path

from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

RELEASES = ("2.1", "2.2", "2.3", "2.4", "2.5")
LATEST = RELEASES[-1]

UBL_NAMESPACE_PREFIX = "urn:oasis:names:specification:ubl:schema:xsd:"
CBC = UBL_NAMESPACE_PREFIX + "CommonBasicComponents-2"
PREFIXES = {
    "cac": UBL_NAMESPACE_PREFIX + "CommonAggregateComponents-2",
    "cbc": CBC,
    "ext": UBL_NAMESPACE_PREFIX + "CommonExtensionComponents-2",
}

Source = str | PathLike | bytes


def parse(source: Source, release: str = LATEST, strict: bool = True):
    """Parse a UBL document into an instance of the class for its root element.

    A release can read the documents of all older 2.x releases.

    strict=True raises ValueError if the document does not fit the classes: a mandatory element
    is missing, an element or attribute is unknown, or a value cannot be converted.

    strict=False parses as much as possible. A missing mandatory element becomes None. Unknown
    elements and attributes are skipped. A value that cannot be converted stays a string.
    """
    return Release(release).parse(source, strict)


def validate(source: Source, release: str = LATEST) -> list[str]:
    """Validate a UBL document against the XSD schemas. Return the errors."""
    return Release(release).validate(source)


def to_xml(document) -> str:
    """Export a document to XML, with the usual UBL namespace prefixes."""
    document_namespace = type(document).Meta.namespace
    serializer = XmlSerializer(config=SerializerConfig(indent="  "))
    return serializer.render(document, ns_map={None: document_namespace, **PREFIXES})


def detect_version(source: Source) -> str | None:
    """Return the value of cbc:UBLVersionID, or None if the document has none."""
    version_id = parse_root(read(source)).findtext(f"{{{CBC}}}UBLVersionID")
    return version_id.strip() if version_id else None


class Release:
    """The generated classes and the XSD schemas of one UBL release."""

    def __init__(self, version: str):
        if version not in RELEASES:
            raise ValueError(f"Unsupported UBL release {version!r}. Supported: {', '.join(RELEASES)}")

        self.version = version
        self.bindings = importlib.import_module(f"ubl_bindings.v{version.replace('.', '_')}")
        self.schema_dir = Path(__file__).parent / "schemas" / version / "xsd"

    def parse(self, source: Source, strict: bool):
        data = read(source)
        document_name = etree.QName(parse_root(data)).localname
        document_class = getattr(self.bindings, document_name)
        config = STRICT if strict else BEST_EFFORT
        return XmlParser(config=config).from_bytes(data, document_class)

    def validate(self, source: Source) -> list[str]:
        root = parse_root(read(source))
        schema = self.schema(etree.QName(root).localname)
        if schema.validate(root):
            return []

        return [str(error) for error in schema.error_log]

    def schema(self, document_name: str) -> etree.XMLSchema:
        return load_schema(self.schema_dir / "maindoc" / f"UBL-{document_name}-{self.version}.xsd")


def read(source: Source) -> bytes:
    if isinstance(source, bytes):
        return source

    return Path(source).read_bytes()


def parse_root(data: bytes) -> etree._Element:
    root = etree.fromstring(data)
    if not root.tag.startswith("{" + UBL_NAMESPACE_PREFIX):
        raise ValueError(f"Not a UBL document. Root element: {root.tag}")

    return root


def create_strict(cls: type, params: dict):
    """Create an instance. Raise ValueError if a mandatory field is missing."""
    missing = [describe(field) for field in missing_fields(cls, params)]
    if missing:
        raise ValueError(
            f"{cls.__name__} misses the mandatory {', '.join(missing)}. "
            "Use validate() to find all errors, or parse(..., strict=False) to read the document anyway."
        )

    return cls(**params)


def create_best_effort(cls: type, params: dict):
    """Create an instance. Set missing mandatory fields to None."""
    missing = {field.name: None for field in missing_fields(cls, params)}
    return cls(**params, **missing)


def missing_fields(cls: type, params: dict) -> list[dataclasses.Field]:
    return [
        field
        for field in dataclasses.fields(cls)
        if field.init
        and field.name not in params
        and field.default is dataclasses.MISSING
        and field.default_factory is dataclasses.MISSING
    ]


def describe(field: dataclasses.Field) -> str:
    # The generated fields store the XML name and node type. The text content of an element has neither.
    if "name" not in field.metadata:
        return "text value"

    return f"{field.metadata['type'].lower()} {field.metadata['name']}"


STRICT = ParserConfig(
    class_factory=create_strict,
    fail_on_unknown_attributes=True,
    fail_on_converter_warnings=True,
)
BEST_EFFORT = ParserConfig(
    class_factory=create_best_effort,
    fail_on_unknown_properties=False,
)


@cache
def load_schema(path: Path) -> etree.XMLSchema:
    # Loading a UBL schema takes about a second, so we keep each one.
    return etree.XMLSchema(etree.parse(str(path)))

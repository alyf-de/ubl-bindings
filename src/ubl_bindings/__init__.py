"""Read, write and validate UBL documents.

The generated classes for each release are in `ubl_bindings.v2_1`, `ubl_bindings.v2_5`, ...
This module adds shortcuts for the common tasks.

All functions take and return XML as bytes. Reading and writing files is up to the caller.
"""

import dataclasses
import importlib
from functools import cache
from pathlib import Path

from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

__all__ = ["LATEST", "RELEASES", "detect_version", "parse", "to_xml", "validate"]

RELEASES = ("2.1", "2.2", "2.3", "2.4", "2.5")
LATEST = RELEASES[-1]

_UBL_NAMESPACE_PREFIX = "urn:oasis:names:specification:ubl:schema:xsd:"
_CBC = _UBL_NAMESPACE_PREFIX + "CommonBasicComponents-2"
_PREFIXES = {
    "cac": _UBL_NAMESPACE_PREFIX + "CommonAggregateComponents-2",
    "cbc": _CBC,
    "ext": _UBL_NAMESPACE_PREFIX + "CommonExtensionComponents-2",
}


def parse(xml: bytes, release: str = LATEST, strict: bool = True):
    """Parse a UBL document into an instance of the class for its root element.

    A release can read the documents of all older 2.x releases.

    strict=True raises ValueError if the document does not fit the classes: a mandatory element
    is missing, an element or attribute is unknown, or a value cannot be converted.

    strict=False parses as much as possible. A missing mandatory element becomes None. Unknown
    elements and attributes are skipped. A value that cannot be converted stays a string.
    """
    return _Release(release).parse(xml, strict)


def validate(xml: bytes, release: str = LATEST) -> list[str]:
    """Validate a UBL document against the XSD schemas. Return the errors."""
    return _Release(release).validate(xml)


def to_xml(document) -> bytes:
    """Export a document to UTF-8 encoded XML, with the usual UBL namespace prefixes."""
    document_namespace = type(document).Meta.namespace
    serializer = XmlSerializer(config=SerializerConfig(indent="  "))
    xml = serializer.render(document, ns_map={None: document_namespace, **_PREFIXES})
    return xml.encode()


def detect_version(xml: bytes) -> str | None:
    """Return the value of cbc:UBLVersionID, or None if the document has none."""
    version_id = _parse_root(xml).findtext(f"{{{_CBC}}}UBLVersionID")
    return version_id.strip() if version_id else None


class _Release:
    """The generated classes and the XSD schemas of one UBL release."""

    def __init__(self, version: str):
        if version not in RELEASES:
            raise ValueError(f"Unsupported UBL release {version!r}. Supported: {', '.join(RELEASES)}")

        self.version = version
        self.bindings = importlib.import_module(f"ubl_bindings.v{version.replace('.', '_')}")
        self.schema_dir = Path(__file__).parent / "schemas" / version / "xsd"

    def parse(self, xml: bytes, strict: bool):
        document_name = etree.QName(_parse_root(xml)).localname
        document_class = getattr(self.bindings, document_name)
        config = _STRICT if strict else _BEST_EFFORT
        return XmlParser(config=config).from_bytes(xml, document_class)

    def validate(self, xml: bytes) -> list[str]:
        root = _parse_root(xml)
        schema = self.schema(etree.QName(root).localname)
        if schema.validate(root):
            return []

        return [str(error) for error in schema.error_log]

    def schema(self, document_name: str) -> etree.XMLSchema:
        return _load_schema(self.schema_dir / "maindoc" / f"UBL-{document_name}-{self.version}.xsd")


def _parse_root(xml: bytes) -> etree._Element:
    # Without this check, lxml would read a path or text as broken XML, with a confusing error.
    if not isinstance(xml, bytes):
        raise TypeError(f"Expected XML as bytes, got {type(xml).__name__}. Read files with Path.read_bytes().")

    root = etree.fromstring(xml)
    if not root.tag.startswith("{" + _UBL_NAMESPACE_PREFIX):
        raise ValueError(f"Not a UBL document. Root element: {root.tag}")

    return root


def _create_strict(cls: type, params: dict):
    """Create an instance. Raise ValueError if a mandatory field is missing."""
    missing = [_describe(field) for field in _missing_fields(cls, params)]
    if missing:
        raise ValueError(
            f"{cls.__name__} misses the mandatory {', '.join(missing)}. "
            "Use validate() to find all errors, or parse(..., strict=False) to read the document anyway."
        )

    return cls(**params)


def _create_best_effort(cls: type, params: dict):
    """Create an instance. Set missing mandatory fields to None."""
    missing = {field.name: None for field in _missing_fields(cls, params)}
    return cls(**params, **missing)


def _missing_fields(cls: type, params: dict) -> list[dataclasses.Field]:
    return [
        field
        for field in dataclasses.fields(cls)
        if field.init
        and field.name not in params
        and field.default is dataclasses.MISSING
        and field.default_factory is dataclasses.MISSING
    ]


def _describe(field: dataclasses.Field) -> str:
    # The generated fields store the XML name and node type. The text content of an element has neither.
    if "name" not in field.metadata:
        return "text value"

    return f"{field.metadata['type'].lower()} {field.metadata['name']}"


_STRICT = ParserConfig(
    class_factory=_create_strict,
    fail_on_unknown_attributes=True,
    fail_on_converter_warnings=True,
)
_BEST_EFFORT = ParserConfig(
    class_factory=_create_best_effort,
    fail_on_unknown_properties=False,
)


@cache
def _load_schema(path: Path) -> etree.XMLSchema:
    # Loading a UBL schema takes about a second, so we keep each one.
    return etree.XMLSchema(etree.parse(str(path)))

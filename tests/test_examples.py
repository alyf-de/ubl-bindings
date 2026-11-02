"""Round trip over the official example documents of each UBL release.

Each release reads its own examples and the examples of all older releases.
UBL 2.0 has no bindings, but each release must read its examples.
"""

import re
from pathlib import Path

import pytest
from lxml import etree

import ubl_bindings

EXAMPLES_DIR = Path(__file__).parent / "examples"
XMLDSIG = "http://www.w3.org/2000/09/xmldsig#"
SCHEMA_LOCATION = "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"
UNSUPPORTED_RELEASES = ("2.0",)


def ubl_examples(release: str) -> list[Path]:
    # The release ZIPs also contain a few files that are not UBL documents.
    return [
        path
        for path in sorted((EXAMPLES_DIR / release).glob("*.xml"))
        if etree.parse(str(path)).getroot().tag.startswith("{" + ubl_bindings.UBL_NAMESPACE_PREFIX)
    ]


def round_trip_cases() -> list:
    cases = []
    for index, release in enumerate(ubl_bindings.RELEASES):
        for example_release in UNSUPPORTED_RELEASES + ubl_bindings.RELEASES[: index + 1]:
            for path in ubl_examples(example_release):
                case_id = f"{release}-reads-{example_release}/{path.name}"
                cases.append(pytest.param(release, path, id=case_id))

    return cases


@pytest.mark.parametrize("release, path", round_trip_cases())
def test_round_trip(release: str, path: Path):
    source = path.read_bytes()

    document = ubl_bindings.parse(source, release=release)
    output = ubl_bindings.to_xml(document)

    assert ubl_bindings.validate(output, release=release) == []
    assert content_lines(output) == content_lines(source)


def content_lines(xml: bytes) -> list[str]:
    """One line for each element: path, attributes and normalized text."""
    tree = etree.fromstring(xml).getroottree()
    return [
        f"{tree.getelementpath(element)} {content_attributes(element)} {normalize_text(element)!r}"
        for element in tree.iter(etree.Element)
    ]


def content_attributes(element: etree._Element) -> list[tuple[str, str]]:
    # xsi:schemaLocation is only a hint for tools. xsdata does not keep it.
    return sorted((name, value) for name, value in element.attrib.items() if name != SCHEMA_LOCATION)


def normalize_text(element: etree._Element) -> str:
    """Remove differences in the lexical form that do not change the value."""
    text = (element.text or "").strip()
    name = etree.QName(element)

    # 12:00:01.000 -> 12:00:01
    text = re.sub(r"(\d\d:\d\d:\d\d)\.0+(?!\d)", r"\1", text)

    # UBL names all boolean elements "...Indicator". 0/1 -> false/true
    if name.localname.endswith("Indicator"):
        text = {"0": "false", "1": "true"}.get(text, text)

    # Base64 data can contain line breaks.
    if name.namespace == XMLDSIG or name.localname.endswith("BinaryObject"):
        text = re.sub(r"\s+", "", text)

    return text

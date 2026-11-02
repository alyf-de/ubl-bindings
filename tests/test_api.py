from pathlib import Path

import pytest

import ubl_bindings
from ubl_bindings.v2_1 import Invoice

INVOICE_2_1 = Path(__file__).parent / "examples" / "2.1" / "UBL-Invoice-2.1-Example.xml"


def test_parse_returns_class_of_root_element():
    invoice = ubl_bindings.parse(INVOICE_2_1, release="2.1")

    assert isinstance(invoice, Invoice)
    assert invoice.id.value == "TOSL108"


def test_detect_version():
    assert ubl_bindings.detect_version(INVOICE_2_1) == "2.1"


def test_validate_reports_missing_element():
    # cbc:ID is mandatory in an invoice.
    xml = INVOICE_2_1.read_bytes().replace(b"<cbc:ID>TOSL108</cbc:ID>", b"", 1)

    errors = ubl_bindings.validate(xml, release="2.1")

    assert len(errors) == 1
    assert "IssueDate" in errors[0]


def test_parse_rejects_other_xml():
    with pytest.raises(ValueError, match="Not a UBL document"):
        ubl_bindings.parse(b"<html/>")


def test_unsupported_release():
    with pytest.raises(ValueError, match="Unsupported UBL release"):
        ubl_bindings.parse(INVOICE_2_1, release="1.0")

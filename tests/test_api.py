from pathlib import Path

import pytest
from xsdata.exceptions import ConverterWarning

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


MISSING_ELEMENT = (b"<cbc:IssueDate>2009-12-15</cbc:IssueDate>", b"")
MISSING_ATTRIBUTE = (b'<cbc:TaxAmount currencyID="EUR">292.20', b"<cbc:TaxAmount>292.20")
UNKNOWN_ELEMENT = (b"<cbc:Note ", b"<cbc:Foo>x</cbc:Foo><cbc:Note ")
UNKNOWN_ATTRIBUTE = (b"<cbc:Note ", b'<cbc:Note foo="x" ')
INVALID_VALUE = (b">292.20<", b">abc<")


@pytest.mark.parametrize(
    "change, error",
    [
        (MISSING_ELEMENT, "Invoice misses the mandatory element IssueDate"),
        (MISSING_ATTRIBUTE, "TaxAmount misses the mandatory attribute currencyID"),
        (UNKNOWN_ELEMENT, "Unknown property .*Foo"),
        (UNKNOWN_ATTRIBUTE, "Unknown attribute .*foo"),
        (INVALID_VALUE, "`abc` is not a valid `Decimal`"),
    ],
)
def test_strict_parse_rejects_document_that_does_not_fit(change, error):
    with pytest.raises(ValueError, match=error):
        ubl_bindings.parse(broken_invoice(change), release="2.1")


def test_best_effort_parse_reads_document_that_does_not_fit():
    xml = broken_invoice(MISSING_ELEMENT, MISSING_ATTRIBUTE, UNKNOWN_ELEMENT, UNKNOWN_ATTRIBUTE, INVALID_VALUE)

    with pytest.warns(ConverterWarning, match="abc"):
        invoice = ubl_bindings.parse(xml, release="2.1", strict=False)

    assert invoice.id.value == "TOSL108"
    assert invoice.issue_date is None
    assert invoice.tax_total[0].tax_amount.currency_id is None
    assert invoice.tax_total[0].tax_amount.value == "abc"
    assert ubl_bindings.validate(ubl_bindings.to_xml(invoice).encode(), release="2.1") != []


def broken_invoice(*changes: tuple[bytes, bytes]) -> bytes:
    xml = INVOICE_2_1.read_bytes()
    for old, new in changes:
        assert old in xml
        xml = xml.replace(old, new, 1)

    return xml


def test_parse_rejects_other_xml():
    with pytest.raises(ValueError, match="Not a UBL document"):
        ubl_bindings.parse(b"<html/>")


def test_unsupported_release():
    with pytest.raises(ValueError, match="Unsupported UBL release"):
        ubl_bindings.parse(INVOICE_2_1, release="1.0")

from __future__ import annotations

from dataclasses import dataclass

from ubl_bindings.v2_5.oasis.names.specification.bdndr.schema.xsd.unqualified_data_types_1 import (
    IdentifierType,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2"
)


@dataclass(kw_only=True)
class ReferencedSignatureIdtype(IdentifierType):
    class Meta:
        name = "ReferencedSignatureIDType"


@dataclass(kw_only=True)
class ReferencedSignatureId(ReferencedSignatureIdtype):
    class Meta:
        name = "ReferencedSignatureID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:SignatureBasicComponents-2"

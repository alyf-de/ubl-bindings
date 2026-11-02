from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_4.org.etsi.uri.pkg_01903.v1.mod_3 import (
    CertIdlistV2Type,
    CertificateValues,
    ObjectIdentifierType,
    RevocationValues,
    XadEstimeStampType,
)
from ubl_bindings.v2_4.org.w3.pkg_2000.pkg_09.xmldsig import DigestMethod

__NAMESPACE__ = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class RecomputedDigestValueType:
    value: bytes = field(
        default=b"",
        metadata={
            "format": "base64",
        },
    )
    order: int = field(
        metadata={
            "name": "Order",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class ArchiveTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class CompleteCertificateRefsTypeV2:
    cert_refs: CertIdlistV2Type = field(
        metadata={
            "name": "CertRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.4.1#",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class RecomputedDigestValue(RecomputedDigestValueType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class RefsOnlyTimeStampV2(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class SpdocSpecification(ObjectIdentifierType):
    class Meta:
        name = "SPDocSpecification"
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class SigAndRefsTimeStampV2(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class ValidationDataType:
    certificate_values: None | CertificateValues = field(
        default=None,
        metadata={
            "name": "CertificateValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    revocation_values: None | RevocationValues = field(
        default=None,
        metadata={
            "name": "RevocationValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    uri: None | str = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class AttributeCertificateRefsV2(CompleteCertificateRefsTypeV2):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class CompleteCertificateRefsV2(CompleteCertificateRefsTypeV2):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class RenewedDigestsType:
    digest_method: DigestMethod = field(
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    recomputed_digest_value: list[RecomputedDigestValue] = field(
        default_factory=list,
        metadata={
            "name": "RecomputedDigestValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.4.1#",
            "min_occurs": 1,
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class SignaturePolicyStoreType:
    spdoc_specification: SpdocSpecification = field(
        metadata={
            "name": "SPDocSpecification",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.4.1#",
        }
    )
    signature_policy_document_or_sig_pol_doc_local_uri: None | bytes | str = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "SignaturePolicyDocument",
                        "type": bytes,
                        "namespace": "http://uri.etsi.org/01903/v1.4.1#",
                        "format": "base64",
                    },
                    {
                        "name": "SigPolDocLocalURI",
                        "type": str,
                        "namespace": "http://uri.etsi.org/01903/v1.4.1#",
                    },
                ),
            },
        )
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TimeStampValidationData(ValidationDataType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class RenewedDigests(RenewedDigestsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"


@dataclass(kw_only=True)
class SignaturePolicyStore(SignaturePolicyStoreType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.4.1#"

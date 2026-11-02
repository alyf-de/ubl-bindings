from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from xsdata.models.datatype import XmlDateTime

from ubl_bindings.v2_4.org.w3.pkg_2000.pkg_09.xmldsig import (
    CanonicalizationMethod,
    DigestMethod,
    DigestValue,
    Signature,
    Transforms,
    X509IssuerSerialType,
)

__NAMESPACE__ = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class AnyType:
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass(kw_only=True)
class CrlidentifierType:
    class Meta:
        name = "CRLIdentifierType"

    issuer: str = field(
        metadata={
            "name": "Issuer",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    issue_time: XmlDateTime = field(
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    number: None | int = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
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
class DocumentationReferencesType:
    documentation_reference: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DocumentationReference",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class EncapsulatedPkidataType:
    class Meta:
        name = "EncapsulatedPKIDataType"

    value: bytes = field(
        default=b"",
        metadata={
            "format": "base64",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )
    encoding: None | str = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class IncludeType:
    uri: str = field(
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    referenced_data: None | bool = field(
        default=None,
        metadata={
            "name": "referencedData",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class IntegerListType:
    int_value: list[int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


class QualifierType(Enum):
    OIDAS_URI = "OIDAsURI"
    OIDAS_URN = "OIDAsURN"


@dataclass(kw_only=True)
class QualifyingPropertiesReferenceType:
    uri: str = field(
        metadata={
            "name": "URI",
            "type": "Attribute",
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
class ResponderIdtype:
    class Meta:
        name = "ResponderIDType"

    by_name_or_by_key: None | str | bytes = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ByName",
                    "type": str,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "ByKey",
                    "type": bytes,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                    "format": "base64",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Spuri:
    class Meta:
        name = "SPURI"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: str = field(default="")


@dataclass(kw_only=True)
class SignatureProductionPlaceType:
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    state_or_province: None | str = field(
        default=None,
        metadata={
            "name": "StateOrProvince",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    country_name: None | str = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class SignatureProductionPlaceV2Type:
    city: None | str = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    street_address: None | str = field(
        default=None,
        metadata={
            "name": "StreetAddress",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    state_or_province: None | str = field(
        default=None,
        metadata={
            "name": "StateOrProvince",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    postal_code: None | str = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    country_name: None | str = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class SigningTime:
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

    value: XmlDateTime = field()


@dataclass(kw_only=True)
class AnyType(AnyType):
    class Meta:
        name = "Any"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CrlvaluesType:
    class Meta:
        name = "CRLValuesType"

    encapsulated_crlvalue: list[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "EncapsulatedCRLValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CertificateValuesType:
    encapsulated_x509_certificate_or_other_certificate: list[
        EncapsulatedPkidataType | AnyType
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EncapsulatedX509Certificate",
                    "type": EncapsulatedPkidataType,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "OtherCertificate",
                    "type": AnyType,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
            ),
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
class CertifiedRolesListType:
    certified_role: list[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "CertifiedRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ClaimedRolesListType:
    claimed_role: list[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "ClaimedRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CommitmentTypeQualifiersListType:
    commitment_type_qualifier: list[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "CommitmentTypeQualifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class CounterSignatureType:
    signature: Signature = field(
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
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
class DigestAlgAndValueType:
    digest_method: DigestMethod = field(
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    digest_value: DigestValue = field(
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass(kw_only=True)
class EncapsulatedPkidata(EncapsulatedPkidataType):
    class Meta:
        name = "EncapsulatedPKIData"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class IdentifierType:
    value: str = field(default="")
    qualifier: None | QualifierType = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Include(IncludeType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class NoticeReferenceType:
    organization: str = field(
        metadata={
            "name": "Organization",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    notice_numbers: IntegerListType = field(
        metadata={
            "name": "NoticeNumbers",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )


@dataclass(kw_only=True)
class OcspidentifierType:
    class Meta:
        name = "OCSPIdentifierType"

    responder_id: ResponderIdtype = field(
        metadata={
            "name": "ResponderID",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    produced_at: XmlDateTime = field(
        metadata={
            "name": "ProducedAt",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    uri: None | str = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class OcspvaluesType:
    class Meta:
        name = "OCSPValuesType"

    encapsulated_ocspvalue: list[EncapsulatedPkidataType] = field(
        default_factory=list,
        metadata={
            "name": "EncapsulatedOCSPValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OtherAttributeCertificate(AnyType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class OtherCertStatusRefsType:
    other_ref: list[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "OtherRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OtherCertStatusValuesType:
    other_value: list[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "OtherValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class QualifyingPropertiesReference(QualifyingPropertiesReferenceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class ReferenceInfoType:
    digest_method: DigestMethod = field(
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    digest_value: DigestValue = field(
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
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
class SigPolicyQualifiersListType:
    sig_policy_qualifier: list[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "SigPolicyQualifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SignatureProductionPlace(SignatureProductionPlaceType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignatureProductionPlaceV2(SignatureProductionPlaceV2Type):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignedAssertion(AnyType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class UnsignedDataObjectPropertiesType:
    unsigned_data_object_property: list[AnyType] = field(
        default_factory=list,
        metadata={
            "name": "UnsignedDataObjectProperty",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
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
class X509AttributeCertificate(EncapsulatedPkidataType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class AttrAuthoritiesCertValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CrlrefType:
    class Meta:
        name = "CRLRefType"

    digest_alg_and_value: DigestAlgAndValueType = field(
        metadata={
            "name": "DigestAlgAndValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    crlidentifier: None | CrlidentifierType = field(
        default=None,
        metadata={
            "name": "CRLIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class CertIdtype:
    class Meta:
        name = "CertIDType"

    cert_digest: DigestAlgAndValueType = field(
        metadata={
            "name": "CertDigest",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    issuer_serial: X509IssuerSerialType = field(
        metadata={
            "name": "IssuerSerial",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    uri: None | str = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CertIdtypeV2:
    class Meta:
        name = "CertIDTypeV2"

    cert_digest: DigestAlgAndValueType = field(
        metadata={
            "name": "CertDigest",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    issuer_serial_v2: None | bytes = field(
        default=None,
        metadata={
            "name": "IssuerSerialV2",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "format": "base64",
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
class CertificateValues(CertificateValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CertifiedRoleTypeV2:
    x509_attribute_certificate_or_other_attribute_certificate: (
        None | X509AttributeCertificate | OtherAttributeCertificate
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "X509AttributeCertificate",
                    "type": X509AttributeCertificate,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "OtherAttributeCertificate",
                    "type": OtherAttributeCertificate,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class ClaimedRoles(ClaimedRolesListType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CounterSignature(CounterSignatureType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class OcsprefType:
    class Meta:
        name = "OCSPRefType"

    ocspidentifier: OcspidentifierType = field(
        metadata={
            "name": "OCSPIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    digest_alg_and_value: None | DigestAlgAndValueType = field(
        default=None,
        metadata={
            "name": "DigestAlgAndValue",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class ObjectIdentifierType:
    identifier: IdentifierType = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    documentation_references: None | DocumentationReferencesType = field(
        default=None,
        metadata={
            "name": "DocumentationReferences",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class ReferenceInfo(ReferenceInfoType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class RevocationValuesType:
    crlvalues: None | CrlvaluesType = field(
        default=None,
        metadata={
            "name": "CRLValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ocspvalues: None | OcspvaluesType = field(
        default=None,
        metadata={
            "name": "OCSPValues",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_values: None | OtherCertStatusValuesType = field(
        default=None,
        metadata={
            "name": "OtherValues",
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


@dataclass(kw_only=True)
class SpuserNoticeType:
    class Meta:
        name = "SPUserNoticeType"

    notice_ref: None | NoticeReferenceType = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    explicit_text: None | str = field(
        default=None,
        metadata={
            "name": "ExplicitText",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class SignedAssertionsListType:
    signed_assertion: list[SignedAssertion] = field(
        default_factory=list,
        metadata={
            "name": "SignedAssertion",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SignerRoleType:
    claimed_roles: None | ClaimedRolesListType = field(
        default=None,
        metadata={
            "name": "ClaimedRoles",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    certified_roles: None | CertifiedRolesListType = field(
        default=None,
        metadata={
            "name": "CertifiedRoles",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class UnsignedDataObjectProperties(UnsignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class AttributeRevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CrlrefsType:
    class Meta:
        name = "CRLRefsType"

    crlref: list[CrlrefType] = field(
        default_factory=list,
        metadata={
            "name": "CRLRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CertIdlistType:
    class Meta:
        name = "CertIDListType"

    cert: list[CertIdtype] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CertIdlistV2Type:
    class Meta:
        name = "CertIDListV2Type"

    cert: list[CertIdtypeV2] = field(
        default_factory=list,
        metadata={
            "name": "Cert",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CertifiedRolesListTypeV2:
    certified_role: list[CertifiedRoleTypeV2] = field(
        default_factory=list,
        metadata={
            "name": "CertifiedRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CommitmentTypeIndicationType:
    commitment_type_id: ObjectIdentifierType = field(
        metadata={
            "name": "CommitmentTypeId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    object_reference_or_all_signed_data_objects: list[str | object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ObjectReference",
                    "type": str,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "AllSignedDataObjects",
                    "type": object,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
            ),
        },
    )
    commitment_type_qualifiers: None | CommitmentTypeQualifiersListType = (
        field(
            default=None,
            metadata={
                "name": "CommitmentTypeQualifiers",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            },
        )
    )


@dataclass(kw_only=True)
class DataObjectFormatType:
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    object_identifier: None | ObjectIdentifierType = field(
        default=None,
        metadata={
            "name": "ObjectIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    mime_type: None | str = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    encoding: None | str = field(
        default=None,
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    object_reference: str = field(
        metadata={
            "name": "ObjectReference",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class GenericTimeStampType:
    include_or_reference_info: list[Include | ReferenceInfo] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Include",
                    "type": Include,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "ReferenceInfo",
                    "type": ReferenceInfo,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
            ),
        },
    )
    canonicalization_method: None | CanonicalizationMethod = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    encapsulated_time_stamp_or_xmltime_stamp: list[
        EncapsulatedPkidataType | AnyType
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EncapsulatedTimeStamp",
                    "type": EncapsulatedPkidataType,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "XMLTimeStamp",
                    "type": AnyType,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
            ),
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
class OcsprefsType:
    class Meta:
        name = "OCSPRefsType"

    ocspref: list[OcsprefType] = field(
        default_factory=list,
        metadata={
            "name": "OCSPRef",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ObjectIdentifier(ObjectIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class RevocationValues(RevocationValuesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SpuserNotice(SpuserNoticeType):
    class Meta:
        name = "SPUserNotice"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignaturePolicyIdType:
    sig_policy_id: ObjectIdentifierType = field(
        metadata={
            "name": "SigPolicyId",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    transforms: None | Transforms = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    sig_policy_hash: DigestAlgAndValueType = field(
        metadata={
            "name": "SigPolicyHash",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        }
    )
    sig_policy_qualifiers: None | SigPolicyQualifiersListType = field(
        default=None,
        metadata={
            "name": "SigPolicyQualifiers",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class SignedAssertions(SignedAssertionsListType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignerRole(SignerRoleType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CertifiedRolesV2(CertifiedRolesListTypeV2):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CommitmentTypeIndication(CommitmentTypeIndicationType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CompleteCertificateRefsType:
    cert_refs: CertIdlistType = field(
        metadata={
            "name": "CertRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
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
class CompleteRevocationRefsType:
    crlrefs: None | CrlrefsType = field(
        default=None,
        metadata={
            "name": "CRLRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    ocsprefs: None | OcsprefsType = field(
        default=None,
        metadata={
            "name": "OCSPRefs",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_refs: None | OtherCertStatusRefsType = field(
        default=None,
        metadata={
            "name": "OtherRefs",
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


@dataclass(kw_only=True)
class DataObjectFormat(DataObjectFormatType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class OtherTimeStampType(GenericTimeStampType):
    include: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    reference_info: list[ReferenceInfo] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceInfo",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SignaturePolicyIdentifierType:
    signature_policy_id_or_signature_policy_implied: (
        None | SignaturePolicyIdType | object
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SignaturePolicyId",
                    "type": SignaturePolicyIdType,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "SignaturePolicyImplied",
                    "type": object,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class SigningCertificate(CertIdlistType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SigningCertificateV2(CertIdlistV2Type):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class XadEstimeStampType(GenericTimeStampType):
    class Meta:
        name = "XAdESTimeStampType"

    reference_info: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class AllDataObjectsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class ArchiveTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class AttributeCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class AttributeRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CompleteCertificateRefs(CompleteCertificateRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class CompleteRevocationRefs(CompleteRevocationRefsType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class IndividualDataObjectsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class OtherTimeStamp(OtherTimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class RefsOnlyTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SigAndRefsTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignaturePolicyIdentifier(SignaturePolicyIdentifierType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignatureTimeStamp(XadEstimeStampType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignerRoleV2Type:
    claimed_roles: None | ClaimedRoles = field(
        default=None,
        metadata={
            "name": "ClaimedRoles",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    certified_roles_v2: None | CertifiedRolesV2 = field(
        default=None,
        metadata={
            "name": "CertifiedRolesV2",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signed_assertions: None | SignedAssertions = field(
        default=None,
        metadata={
            "name": "SignedAssertions",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )


@dataclass(kw_only=True)
class XadEstimeStamp(XadEstimeStampType):
    class Meta:
        name = "XAdESTimeStamp"
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignedDataObjectPropertiesType:
    data_object_format: list[DataObjectFormat] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectFormat",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    commitment_type_indication: list[CommitmentTypeIndication] = field(
        default_factory=list,
        metadata={
            "name": "CommitmentTypeIndication",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    all_data_objects_time_stamp: list[AllDataObjectsTimeStamp] = field(
        default_factory=list,
        metadata={
            "name": "AllDataObjectsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    individual_data_objects_time_stamp: list[
        IndividualDataObjectsTimeStamp
    ] = field(
        default_factory=list,
        metadata={
            "name": "IndividualDataObjectsTimeStamp",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
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
class SignerRoleV2(SignerRoleV2Type):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class UnsignedSignaturePropertiesType:
    choice: list[
        CounterSignature
        | SignatureTimeStamp
        | CompleteCertificateRefs
        | CompleteRevocationRefs
        | AttributeCertificateRefs
        | AttributeRevocationRefs
        | SigAndRefsTimeStamp
        | RefsOnlyTimeStamp
        | CertificateValues
        | RevocationValues
        | AttrAuthoritiesCertValues
        | AttributeRevocationValues
        | ArchiveTimeStamp
        | object
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CounterSignature",
                    "type": CounterSignature,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "SignatureTimeStamp",
                    "type": SignatureTimeStamp,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "CompleteCertificateRefs",
                    "type": CompleteCertificateRefs,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "CompleteRevocationRefs",
                    "type": CompleteRevocationRefs,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "AttributeCertificateRefs",
                    "type": AttributeCertificateRefs,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "AttributeRevocationRefs",
                    "type": AttributeRevocationRefs,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "SigAndRefsTimeStamp",
                    "type": SigAndRefsTimeStamp,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "RefsOnlyTimeStamp",
                    "type": RefsOnlyTimeStamp,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "CertificateValues",
                    "type": CertificateValues,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "RevocationValues",
                    "type": RevocationValues,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "AttrAuthoritiesCertValues",
                    "type": AttrAuthoritiesCertValues,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "AttributeRevocationValues",
                    "type": AttributeRevocationValues,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "name": "ArchiveTimeStamp",
                    "type": ArchiveTimeStamp,
                    "namespace": "http://uri.etsi.org/01903/v1.3.2#",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                },
            ),
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
class SignedDataObjectProperties(SignedDataObjectPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignedSignaturePropertiesType:
    signing_time: None | SigningTime = field(
        default=None,
        metadata={
            "name": "SigningTime",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signing_certificate: None | SigningCertificate = field(
        default=None,
        metadata={
            "name": "SigningCertificate",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signing_certificate_v2: None | SigningCertificateV2 = field(
        default=None,
        metadata={
            "name": "SigningCertificateV2",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signature_policy_identifier: None | SignaturePolicyIdentifier = field(
        default=None,
        metadata={
            "name": "SignaturePolicyIdentifier",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signature_production_place: None | SignatureProductionPlace = field(
        default=None,
        metadata={
            "name": "SignatureProductionPlace",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signature_production_place_v2: None | SignatureProductionPlaceV2 = field(
        default=None,
        metadata={
            "name": "SignatureProductionPlaceV2",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signer_role: None | SignerRole = field(
        default=None,
        metadata={
            "name": "SignerRole",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signer_role_v2: None | SignerRoleV2 = field(
        default=None,
        metadata={
            "name": "SignerRoleV2",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
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
class UnsignedSignatureProperties(UnsignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignedSignatureProperties(SignedSignaturePropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class UnsignedPropertiesType:
    unsigned_signature_properties: None | UnsignedSignatureProperties = field(
        default=None,
        metadata={
            "name": "UnsignedSignatureProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    unsigned_data_object_properties: None | UnsignedDataObjectProperties = (
        field(
            default=None,
            metadata={
                "name": "UnsignedDataObjectProperties",
                "type": "Element",
                "namespace": "http://uri.etsi.org/01903/v1.3.2#",
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
class SignedPropertiesType:
    signed_signature_properties: None | SignedSignatureProperties = field(
        default=None,
        metadata={
            "name": "SignedSignatureProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    signed_data_object_properties: None | SignedDataObjectProperties = field(
        default=None,
        metadata={
            "name": "SignedDataObjectProperties",
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


@dataclass(kw_only=True)
class UnsignedProperties(UnsignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class SignedProperties(SignedPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"


@dataclass(kw_only=True)
class QualifyingPropertiesType:
    signed_properties: None | SignedProperties = field(
        default=None,
        metadata={
            "name": "SignedProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    unsigned_properties: None | UnsignedProperties = field(
        default=None,
        metadata={
            "name": "UnsignedProperties",
            "type": "Element",
            "namespace": "http://uri.etsi.org/01903/v1.3.2#",
        },
    )
    target: str = field(
        metadata={
            "name": "Target",
            "type": "Attribute",
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
class QualifyingProperties(QualifyingPropertiesType):
    class Meta:
        namespace = "http://uri.etsi.org/01903/v1.3.2#"

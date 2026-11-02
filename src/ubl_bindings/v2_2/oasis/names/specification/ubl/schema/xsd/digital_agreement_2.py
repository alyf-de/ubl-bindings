from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_2.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    AgreementCountry,
    DigitalAgreementTerms,
    DigitalProcess,
    GovernorParty,
    ParticipantParty,
    RequiredCertificationDocumentReference,
    Signature,
)
from ubl_bindings.v2_2.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    AgreementTypeCode,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    PreviousVersionId,
    ProfileExecutionId,
    ProfileId,
    RequiredResponseMessageLevelCode,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl_bindings.v2_2.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:DigitalAgreement-2"
)


@dataclass(kw_only=True)
class DigitalAgreementType:
    ublextensions: None | Ublextensions = field(
        default=None,
        metadata={
            "name": "UBLExtensions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    ublversion_id: None | UblversionId = field(
        default=None,
        metadata={
            "name": "UBLVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customization_id: None | CustomizationId = field(
        default=None,
        metadata={
            "name": "CustomizationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_id: None | ProfileId = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_execution_id: None | ProfileExecutionId = field(
        default=None,
        metadata={
            "name": "ProfileExecutionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    id: Id = field(
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: None | Uuid = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate = field(
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_time: None | IssueTime = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    agreement_type_code: None | AgreementTypeCode = field(
        default=None,
        metadata={
            "name": "AgreementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: VersionId = field(
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    previous_version_id: None | PreviousVersionId = field(
        default=None,
        metadata={
            "name": "PreviousVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_response_message_level_code: (
        None | RequiredResponseMessageLevelCode
    ) = field(
        default=None,
        metadata={
            "name": "RequiredResponseMessageLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    governor_party: None | GovernorParty = field(
        default=None,
        metadata={
            "name": "GovernorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    participant_party: list[ParticipantParty] = field(
        default_factory=list,
        metadata={
            "name": "ParticipantParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    agreement_country: list[AgreementCountry] = field(
        default_factory=list,
        metadata={
            "name": "AgreementCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_certification_document_reference: list[
        RequiredCertificationDocumentReference
    ] = field(
        default_factory=list,
        metadata={
            "name": "RequiredCertificationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    digital_agreement_terms: None | DigitalAgreementTerms = field(
        default=None,
        metadata={
            "name": "DigitalAgreementTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    digital_process: list[DigitalProcess] = field(
        default_factory=list,
        metadata={
            "name": "DigitalProcess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class DigitalAgreement(DigitalAgreementType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:DigitalAgreement-2"
        )

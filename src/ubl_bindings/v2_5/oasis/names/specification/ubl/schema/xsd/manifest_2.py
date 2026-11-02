from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    AuthorityParty,
    ConsigneeParty,
    ConsignorParty,
    CrewPerson,
    DocumentDistribution,
    DocumentReference,
    PassengerPerson,
    SendingLogisticsOperatorParty,
    Shipment,
    Signature,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    AdValoremIndicator,
    CustomizationId,
    DeclaredCarriageValueAmount,
    Description,
    Id,
    IssueDate,
    IssueTime,
    ManifestTypeCode,
    Note,
    ProfileExecutionId,
    ProfileId,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    ManifestType as CommonBasicComponents2ManifestType,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:Manifest-2"


@dataclass(kw_only=True)
class ManifestType:
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
    issue_date: None | IssueDate = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: None | IssueTime = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    manifest_type_code: None | ManifestTypeCode = field(
        default=None,
        metadata={
            "name": "ManifestTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    manifest_type: list[CommonBasicComponents2ManifestType] = field(
        default_factory=list,
        metadata={
            "name": "ManifestType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: list[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: list[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: None | VersionId = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    ad_valorem_indicator: None | AdValoremIndicator = field(
        default=None,
        metadata={
            "name": "AdValoremIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_carriage_value_amount: None | DeclaredCarriageValueAmount = field(
        default=None,
        metadata={
            "name": "DeclaredCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sending_logistics_operator_party: SendingLogisticsOperatorParty = field(
        metadata={
            "name": "SendingLogisticsOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    authority_party: None | AuthorityParty = field(
        default=None,
        metadata={
            "name": "AuthorityParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consignor_party: None | ConsignorParty = field(
        default=None,
        metadata={
            "name": "ConsignorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consignee_party: None | ConsigneeParty = field(
        default=None,
        metadata={
            "name": "ConsigneeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    crew_person: list[CrewPerson] = field(
        default_factory=list,
        metadata={
            "name": "CrewPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    passenger_person: list[PassengerPerson] = field(
        default_factory=list,
        metadata={
            "name": "PassengerPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment: None | Shipment = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: list[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_distribution: list[DocumentDistribution] = field(
        default_factory=list,
        metadata={
            "name": "DocumentDistribution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
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


@dataclass(kw_only=True)
class Manifest(ManifestType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:Manifest-2"

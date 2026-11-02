from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    AdditionalDocumentReference,
    DocumentDistribution,
    ExportingCustomsParty,
    ExportingGuarantorParty,
    GoodsItemPassportCounterfoil,
    HolderParty,
    ImportingCustomsParty,
    ImportingGuarantorParty,
    IssuerEndorsement,
    IssuerParty,
    RepresentativeParty,
    Shipment,
    Signature,
    ValidityPeriod,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    CustomizationId,
    ExportReason,
    ExportReasonCode,
    Id,
    IssueDate,
    IssueTime,
    Note,
    ProfileExecutionId,
    ProfileId,
    Status,
    StatusCode,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:GoodsItemPassport-2"
)


@dataclass(kw_only=True)
class GoodsItemPassportType:
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
    status_code: None | StatusCode = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    status: list[Status] = field(
        default_factory=list,
        metadata={
            "name": "Status",
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
    export_reason_code: None | ExportReasonCode = field(
        default=None,
        metadata={
            "name": "ExportReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    export_reason: list[ExportReason] = field(
        default_factory=list,
        metadata={
            "name": "ExportReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_period: None | ValidityPeriod = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    issuer_party: None | IssuerParty = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    holder_party: HolderParty = field(
        metadata={
            "name": "HolderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    representative_party: None | RepresentativeParty = field(
        default=None,
        metadata={
            "name": "RepresentativeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exporting_guarantor_party: None | ExportingGuarantorParty = field(
        default=None,
        metadata={
            "name": "ExportingGuarantorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    importing_guarantor_party: None | ImportingGuarantorParty = field(
        default=None,
        metadata={
            "name": "ImportingGuarantorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exporting_customs_party: None | ExportingCustomsParty = field(
        default=None,
        metadata={
            "name": "ExportingCustomsParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    importing_customs_party: None | ImportingCustomsParty = field(
        default=None,
        metadata={
            "name": "ImportingCustomsParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment: Shipment = field(
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    goods_item_passport_counterfoil: list[GoodsItemPassportCounterfoil] = (
        field(
            default_factory=list,
            metadata={
                "name": "GoodsItemPassportCounterfoil",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
                "min_occurs": 1,
            },
        )
    )
    issuer_endorsement: None | IssuerEndorsement = field(
        default=None,
        metadata={
            "name": "IssuerEndorsement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_document_reference: list[AdditionalDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDocumentReference",
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
class GoodsItemPassport(GoodsItemPassportType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:GoodsItemPassport-2"
        )

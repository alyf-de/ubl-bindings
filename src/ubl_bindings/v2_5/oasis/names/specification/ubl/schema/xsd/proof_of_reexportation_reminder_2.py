from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    AdditionalDocumentReference,
    ExportingGuarantorParty,
    GoodsItemPassportCounterfoil,
    ImportingCustomsParty,
    ImportingGuarantorParty,
    IssuerEndorsement,
    PaymentTerms,
    ProofOfReexportationRequestDocumentReference,
    Signature,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    CopyIndicator,
    CustomizationId,
    GoodsItemPassportId,
    Id,
    IssueDate,
    IssueTime,
    Note,
    ProcedureCode,
    ProfileExecutionId,
    ProfileId,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:ProofOfReexportationReminder-2"


@dataclass(kw_only=True)
class ProofOfReexportationReminderType:
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
    copy_indicator: None | CopyIndicator = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
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
    procedure_code: ProcedureCode = field(
        metadata={
            "name": "ProcedureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
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
    goods_item_passport_id: None | GoodsItemPassportId = field(
        default=None,
        metadata={
            "name": "GoodsItemPassportID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    proof_of_reexportation_request_document_reference: ProofOfReexportationRequestDocumentReference = field(
        metadata={
            "name": "ProofOfReexportationRequestDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    importing_guarantor_party: ImportingGuarantorParty = field(
        metadata={
            "name": "ImportingGuarantorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exporting_guarantor_party: ExportingGuarantorParty = field(
        metadata={
            "name": "ExportingGuarantorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    importing_customs_party: None | ImportingCustomsParty = field(
        default=None,
        metadata={
            "name": "ImportingCustomsParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    issuer_endorsement: None | IssuerEndorsement = field(
        default=None,
        metadata={
            "name": "IssuerEndorsement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: list[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
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
    additional_document_reference: list[AdditionalDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDocumentReference",
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
class ProofOfReexportationReminder(ProofOfReexportationReminderType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:ProofOfReexportationReminder-2"

from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    AdditionalDocumentReference,
    BeneficiaryParty,
    ContractingParty,
    LegalDocumentReference,
    OriginatorCustomerParty,
    ProcurementProject,
    ProcurementProjectLot,
    ProvidedDocumentReference,
    ReceiverParty,
    RequiredDocumentReference,
    Signature,
    TechnicalDocumentReference,
    TenderingProcess,
    TenderingTerms,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    ApprovalDate,
    ContractFolderId,
    CopyIndicator,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    Note,
    PreviousVersionId,
    ProfileExecutionId,
    ProfileId,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CallForTenders-2"


@dataclass(kw_only=True)
class CallForTendersType:
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
    id: None | Id = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
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
    contract_folder_id: ContractFolderId = field(
        metadata={
            "name": "ContractFolderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    approval_date: None | ApprovalDate = field(
        default=None,
        metadata={
            "name": "ApprovalDate",
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
    previous_version_id: None | PreviousVersionId = field(
        default=None,
        metadata={
            "name": "PreviousVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    legal_document_reference: None | LegalDocumentReference = field(
        default=None,
        metadata={
            "name": "LegalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    technical_document_reference: None | TechnicalDocumentReference = field(
        default=None,
        metadata={
            "name": "TechnicalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_document_reference: list[RequiredDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "RequiredDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    provided_document_reference: list[ProvidedDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "ProvidedDocumentReference",
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
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contracting_party: list[ContractingParty] = field(
        default_factory=list,
        metadata={
            "name": "ContractingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    originator_customer_party: list[OriginatorCustomerParty] = field(
        default_factory=list,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    beneficiary_party: list[BeneficiaryParty] = field(
        default_factory=list,
        metadata={
            "name": "BeneficiaryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receiver_party: None | ReceiverParty = field(
        default=None,
        metadata={
            "name": "ReceiverParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tendering_terms: None | TenderingTerms = field(
        default=None,
        metadata={
            "name": "TenderingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tendering_process: None | TenderingProcess = field(
        default=None,
        metadata={
            "name": "TenderingProcess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    procurement_project: ProcurementProject = field(
        metadata={
            "name": "ProcurementProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    procurement_project_lot: list[ProcurementProjectLot] = field(
        default_factory=list,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(kw_only=True)
class CallForTenders(CallForTendersType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:CallForTenders-2"
        )

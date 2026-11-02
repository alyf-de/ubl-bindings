from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    ContractingParty,
    DocumentProviderParty,
    EconomicOperatorParty,
    EmploymentLegislationDocumentReference,
    EnvironmentalLegislationDocumentReference,
    FiscalLegislationDocumentReference,
    InvitationSubmissionPeriod,
    ParticipationRequestReceptionPeriod,
    ProcurementLegislationDocumentReference,
    ProcurementProject,
    ProcurementProjectLot,
    Signature,
    TenderRecipientParty,
    TenderStatusInquiryDocumentReference,
    TenderSubmissionDeadlinePeriod,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    ContractFolderId,
    ContractName,
    CopyIndicator,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    Note,
    ProcedureCode,
    ProfileExecutionId,
    ProfileId,
    UblversionId,
    Uuid,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:TenderStatus-2"


@dataclass(kw_only=True)
class TenderStatusType:
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
    contract_folder_id: None | ContractFolderId = field(
        default=None,
        metadata={
            "name": "ContractFolderID",
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
    contract_name: list[ContractName] = field(
        default_factory=list,
        metadata={
            "name": "ContractName",
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
    procedure_code: None | ProcedureCode = field(
        default=None,
        metadata={
            "name": "ProcedureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tender_submission_deadline_period: (
        None | TenderSubmissionDeadlinePeriod
    ) = field(
        default=None,
        metadata={
            "name": "TenderSubmissionDeadlinePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    invitation_submission_period: None | InvitationSubmissionPeriod = field(
        default=None,
        metadata={
            "name": "InvitationSubmissionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    participation_request_reception_period: (
        None | ParticipationRequestReceptionPeriod
    ) = field(
        default=None,
        metadata={
            "name": "ParticipationRequestReceptionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    procurement_legislation_document_reference: (
        None | ProcurementLegislationDocumentReference
    ) = field(
        default=None,
        metadata={
            "name": "ProcurementLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    fiscal_legislation_document_reference: (
        None | FiscalLegislationDocumentReference
    ) = field(
        default=None,
        metadata={
            "name": "FiscalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    environmental_legislation_document_reference: (
        None | EnvironmentalLegislationDocumentReference
    ) = field(
        default=None,
        metadata={
            "name": "EnvironmentalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    employment_legislation_document_reference: (
        None | EmploymentLegislationDocumentReference
    ) = field(
        default=None,
        metadata={
            "name": "EmploymentLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_status_inquiry_document_reference: list[
        TenderStatusInquiryDocumentReference
    ] = field(
        default_factory=list,
        metadata={
            "name": "TenderStatusInquiryDocumentReference",
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
    contracting_party: ContractingParty = field(
        metadata={
            "name": "ContractingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    economic_operator_party: EconomicOperatorParty = field(
        metadata={
            "name": "EconomicOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_provider_party: None | DocumentProviderParty = field(
        default=None,
        metadata={
            "name": "DocumentProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_recipient_party: None | TenderRecipientParty = field(
        default=None,
        metadata={
            "name": "TenderRecipientParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    procurement_project: None | ProcurementProject = field(
        default=None,
        metadata={
            "name": "ProcurementProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
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
class TenderStatus(TenderStatusType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:TenderStatus-2"
        )

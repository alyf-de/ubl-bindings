from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    DisposalFacilityParty,
    DocumentDistribution,
    DocumentReference,
    NotifierParty,
    ReceiverParty,
    RecoveryFacilityParty,
    SenderParty,
    Shipment,
    Signature,
    WasteNotificationDocumentReference,
    WasteProducerParty,
    WeightStatementDocumentReference,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    ConsignmentQuantity,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    ProfileExecutionId,
    ProfileId,
    SequenceNumberId,
    UblversionId,
    Uuid,
    WasteMovementTypeCode,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:WasteMovement-2"


@dataclass(kw_only=True)
class WasteMovementType:
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
    waste_movement_type_code: None | WasteMovementTypeCode = field(
        default=None,
        metadata={
            "name": "WasteMovementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_number_id: None | SequenceNumberId = field(
        default=None,
        metadata={
            "name": "SequenceNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignment_quantity: None | ConsignmentQuantity = field(
        default=None,
        metadata={
            "name": "ConsignmentQuantity",
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
    sender_party: SenderParty = field(
        metadata={
            "name": "SenderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    receiver_party: ReceiverParty = field(
        metadata={
            "name": "ReceiverParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notifier_party: NotifierParty = field(
        metadata={
            "name": "NotifierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    disposal_facility_party: None | DisposalFacilityParty = field(
        default=None,
        metadata={
            "name": "DisposalFacilityParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    recovery_facility_party: None | RecoveryFacilityParty = field(
        default=None,
        metadata={
            "name": "RecoveryFacilityParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    waste_producer_party: WasteProducerParty = field(
        metadata={
            "name": "WasteProducerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment: Shipment = field(
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    waste_notification_document_reference: (
        None | WasteNotificationDocumentReference
    ) = field(
        default=None,
        metadata={
            "name": "WasteNotificationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    weight_statement_document_reference: list[
        WeightStatementDocumentReference
    ] = field(
        default_factory=list,
        metadata={
            "name": "WeightStatementDocumentReference",
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


@dataclass(kw_only=True)
class WasteMovement(WasteMovementType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:WasteMovement-2"
        )

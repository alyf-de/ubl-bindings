from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_3.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    Consignment,
    DocumentReference,
    ReceiverParty,
    RequestedStatusLocation,
    RequestedStatusPeriod,
    SenderParty,
    Signature,
    TransportExecutionPlanDocumentReference,
)
from ubl_bindings.v2_3.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    CarrierAssignedId,
    CustomizationId,
    Description,
    Id,
    IssueDate,
    IssueTime,
    Name,
    Note,
    OtherInstruction,
    ProfileExecutionId,
    ProfileId,
    ShippingOrderId,
    TransportationStatusTypeCode,
    UblversionId,
    Uuid,
)
from ubl_bindings.v2_3.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:TransportationStatusRequest-2"


@dataclass(kw_only=True)
class TransportationStatusRequestType:
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
    carrier_assigned_id: None | CarrierAssignedId = field(
        default=None,
        metadata={
            "name": "CarrierAssignedID",
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
    name: None | Name = field(
        default=None,
        metadata={
            "name": "Name",
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
    shipping_order_id: None | ShippingOrderId = field(
        default=None,
        metadata={
            "name": "ShippingOrderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    other_instruction: None | OtherInstruction = field(
        default=None,
        metadata={
            "name": "OtherInstruction",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transportation_status_type_code: None | TransportationStatusTypeCode = (
        field(
            default=None,
            metadata={
                "name": "TransportationStatusTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    sender_party: None | SenderParty = field(
        default=None,
        metadata={
            "name": "SenderParty",
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
    transport_execution_plan_document_reference: (
        None | TransportExecutionPlanDocumentReference
    ) = field(
        default=None,
        metadata={
            "name": "TransportExecutionPlanDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consignment: list[Consignment] = field(
        default_factory=list,
        metadata={
            "name": "Consignment",
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
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_status_location: list[RequestedStatusLocation] = field(
        default_factory=list,
        metadata={
            "name": "RequestedStatusLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_status_period: list[RequestedStatusPeriod] = field(
        default_factory=list,
        metadata={
            "name": "RequestedStatusPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(kw_only=True)
class TransportationStatusRequest(TransportationStatusRequestType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:TransportationStatusRequest-2"

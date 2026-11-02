from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_1.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    ReceiverParty,
    ReferencedConsignment,
    ReferencedGoodsItem,
    ReferencedPackage,
    ReferencedTransportEquipment,
    SenderParty,
    Signature,
    TransportationSegment,
)
from ubl_bindings.v2_1.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    CopyIndicator,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    Note,
    ProfileExecutionId,
    ProfileId,
    TransportExecutionPlanReferenceId,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl_bindings.v2_1.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:GoodsItemItinerary-2"
)


@dataclass(kw_only=True)
class GoodsItemItineraryType:
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
    issue_time: IssueTime = field(
        metadata={
            "name": "IssueTime",
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
    version_id: VersionId = field(
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_execution_plan_reference_id: TransportExecutionPlanReferenceId = field(
        metadata={
            "name": "TransportExecutionPlanReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
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
    referenced_consignment: list[ReferencedConsignment] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedConsignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    referenced_transport_equipment: list[ReferencedTransportEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    referenced_package: list[ReferencedPackage] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    referenced_goods_item: list[ReferencedGoodsItem] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedGoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transportation_segment: list[TransportationSegment] = field(
        default_factory=list,
        metadata={
            "name": "TransportationSegment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class GoodsItemItinerary(GoodsItemItineraryType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:GoodsItemItinerary-2"
        )

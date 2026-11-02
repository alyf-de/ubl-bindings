from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_4.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    ApplicablePeriod,
    ApplicableRegulation,
    BeneficiaryParty,
    GuaranteeDocumentReference,
    GuarantorParty,
    ImmobilizedSecurity,
    InterestedParty,
    Signature,
)
from ubl_bindings.v2_4.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    ConstitutionCode,
    ContractFolderId,
    CopyIndicator,
    CustomizationId,
    GuaranteeTypeCode,
    Id,
    IssueDate,
    IssueTime,
    LiabilityAmount,
    Note,
    ProfileExecutionId,
    ProfileId,
    Purpose,
    UblversionId,
    Uuid,
)
from ubl_bindings.v2_4.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:GuaranteeCertificate-2"
)


@dataclass(kw_only=True)
class GuaranteeCertificateType:
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
    guarantee_type_code: None | GuaranteeTypeCode = field(
        default=None,
        metadata={
            "name": "GuaranteeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    purpose: list[Purpose] = field(
        default_factory=list,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    liability_amount: LiabilityAmount = field(
        metadata={
            "name": "LiabilityAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    constitution_code: None | ConstitutionCode = field(
        default=None,
        metadata={
            "name": "ConstitutionCode",
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
    applicable_period: None | ApplicablePeriod = field(
        default=None,
        metadata={
            "name": "ApplicablePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    applicable_regulation: list[ApplicableRegulation] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableRegulation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    guarantee_document_reference: list[GuaranteeDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "GuaranteeDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    immobilized_security: list[ImmobilizedSecurity] = field(
        default_factory=list,
        metadata={
            "name": "ImmobilizedSecurity",
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
    guarantor_party: GuarantorParty = field(
        metadata={
            "name": "GuarantorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    interested_party: InterestedParty = field(
        metadata={
            "name": "InterestedParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    beneficiary_party: None | BeneficiaryParty = field(
        default=None,
        metadata={
            "name": "BeneficiaryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(kw_only=True)
class GuaranteeCertificate(GuaranteeCertificateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:GuaranteeCertificate-2"

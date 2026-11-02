from __future__ import annotations

from dataclasses import dataclass, field

from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_aggregate_components_2 import (
    AccountingCustomerParty,
    AccountingSupplierParty,
    AdditionalDocumentReference,
    AllowanceCharge,
    BeneficiaryParty,
    BuyerCustomerParty,
    Contract,
    Delivery,
    DeliveryTerms,
    DestinationCountry,
    FreightForwarderParty,
    LegalMonetaryTotal,
    OrderChangeDocumentReference,
    OrderDocumentReference,
    OrderLine,
    OrderReference,
    OriginatorCustomerParty,
    OriginatorDocumentReference,
    PaymentExchangeRate,
    PaymentMeans,
    PaymentTerms,
    PricingExchangeRate,
    SellerSupplierParty,
    Signature,
    TaxExchangeRate,
    TaxTotal,
    TransactionConditions,
    ValidityPeriod,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_basic_components_2 import (
    AccountingCost,
    AccountingCostCode,
    CopyIndicator,
    CustomerReference,
    CustomizationId,
    DocumentCurrencyCode,
    GrossVolumeMeasure,
    GrossWeightMeasure,
    Id,
    IssueDate,
    IssueTime,
    LineCountNumeric,
    NetNetWeightMeasure,
    NetVolumeMeasure,
    NetWeightMeasure,
    Note,
    OrderResponseCode,
    PricingCurrencyCode,
    ProfileExecutionId,
    ProfileId,
    SalesOrderId,
    TaxCurrencyCode,
    TotalPackagesQuantity,
    UblversionId,
    Uuid,
)
from ubl_bindings.v2_5.oasis.names.specification.ubl.schema.xsd.common_extension_components_2 import (
    Ublextensions,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:OrderResponse-2"


@dataclass(kw_only=True)
class OrderResponseType:
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
    sales_order_id: None | SalesOrderId = field(
        default=None,
        metadata={
            "name": "SalesOrderID",
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
    order_response_code: None | OrderResponseCode = field(
        default=None,
        metadata={
            "name": "OrderResponseCode",
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
    document_currency_code: None | DocumentCurrencyCode = field(
        default=None,
        metadata={
            "name": "DocumentCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pricing_currency_code: None | PricingCurrencyCode = field(
        default=None,
        metadata={
            "name": "PricingCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_currency_code: None | TaxCurrencyCode = field(
        default=None,
        metadata={
            "name": "TaxCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_packages_quantity: None | TotalPackagesQuantity = field(
        default=None,
        metadata={
            "name": "TotalPackagesQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_weight_measure: None | GrossWeightMeasure = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: None | NetWeightMeasure = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_net_weight_measure: None | NetNetWeightMeasure = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: None | GrossVolumeMeasure = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: None | NetVolumeMeasure = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customer_reference: None | CustomerReference = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: None | AccountingCostCode = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: None | AccountingCost = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_count_numeric: None | LineCountNumeric = field(
        default=None,
        metadata={
            "name": "LineCountNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_period: list[ValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    order_reference: list[OrderReference] = field(
        default_factory=list,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    order_document_reference: list[OrderDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "OrderDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    order_change_document_reference: list[OrderChangeDocumentReference] = (
        field(
            default_factory=list,
            metadata={
                "name": "OrderChangeDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    originator_document_reference: None | OriginatorDocumentReference = field(
        default=None,
        metadata={
            "name": "OriginatorDocumentReference",
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
    contract: list[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
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
    seller_supplier_party: SellerSupplierParty = field(
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    buyer_customer_party: BuyerCustomerParty = field(
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    originator_customer_party: None | OriginatorCustomerParty = field(
        default=None,
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
    freight_forwarder_party: None | FreightForwarderParty = field(
        default=None,
        metadata={
            "name": "FreightForwarderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_supplier_party: None | AccountingSupplierParty = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_customer_party: None | AccountingCustomerParty = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: list[Delivery] = field(
        default_factory=list,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: None | DeliveryTerms = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_means: list[PaymentMeans] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMeans",
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
    allowance_charge: list[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transaction_conditions: None | TransactionConditions = field(
        default=None,
        metadata={
            "name": "TransactionConditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_exchange_rate: None | TaxExchangeRate = field(
        default=None,
        metadata={
            "name": "TaxExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pricing_exchange_rate: None | PricingExchangeRate = field(
        default=None,
        metadata={
            "name": "PricingExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_exchange_rate: None | PaymentExchangeRate = field(
        default=None,
        metadata={
            "name": "PaymentExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    destination_country: None | DestinationCountry = field(
        default=None,
        metadata={
            "name": "DestinationCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: list[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    legal_monetary_total: None | LegalMonetaryTotal = field(
        default=None,
        metadata={
            "name": "LegalMonetaryTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    order_line: list[OrderLine] = field(
        default_factory=list,
        metadata={
            "name": "OrderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(kw_only=True)
class OrderResponse(OrderResponseType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:OrderResponse-2"
        )

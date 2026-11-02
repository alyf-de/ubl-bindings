from __future__ import annotations

from dataclasses import dataclass

from ubl_bindings.v2_5.oasis.names.specification.bdndr.schema.xsd.unqualified_data_types_1 import (
    CodeType,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDataTypes-2"
)


@dataclass(kw_only=True)
class AllowanceChargeReasonCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class ChannelCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class ChipCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class CountryIdentificationCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class CurrencyCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class DocumentStatusCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class LanguageCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class LatitudeDirectionCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class LineStatusCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class LongitudeDirectionCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class OperatorCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class PackagingTypeCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class PaymentMeansCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class ReceiptAdviceTypeCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class SubstitutionStatusCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class TransportEquipmentTypeCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class TransportModeCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class UnitOfMeasureCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class WeekDayCodeType(CodeType):
    pass


@dataclass(kw_only=True)
class WeighingMethodCodeType(CodeType):
    pass

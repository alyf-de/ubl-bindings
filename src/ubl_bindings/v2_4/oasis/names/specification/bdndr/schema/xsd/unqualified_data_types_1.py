from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    AmountType as Mod2AmountType,
)
from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    BinaryObjectType as Mod2BinaryObjectType,
)
from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    CodeType as Mod2CodeType,
)
from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    IdentifierType as Mod2IdentifierType,
)
from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    MeasureType as Mod2MeasureType,
)
from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    NumericType as Mod2NumericType,
)
from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    QuantityType as Mod2QuantityType,
)
from ubl_bindings.v2_4.un.unece.uncefact.data.specification.core_component_type_schema_module.mod_2 import (
    TextType as Mod2TextType,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:bdndr:schema:xsd:UnqualifiedDataTypes-1"
)


@dataclass(kw_only=True)
class DateTimeType:
    value: XmlDateTime = field()


@dataclass(kw_only=True)
class DateType:
    value: XmlDate = field()


@dataclass(kw_only=True)
class IndicatorType:
    value: bool = field()


@dataclass(kw_only=True)
class TimeType:
    value: XmlTime = field()


@dataclass(kw_only=True)
class AmountType(Mod2AmountType):
    currency_id: str = field(
        metadata={
            "name": "currencyID",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class BinaryObjectType(Mod2BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class CodeType(Mod2CodeType):
    pass


@dataclass(kw_only=True)
class GraphicType(Mod2BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class IdentifierType(Mod2IdentifierType):
    pass


@dataclass(kw_only=True)
class MeasureType(Mod2MeasureType):
    unit_code: str = field(
        metadata={
            "name": "unitCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class NameType(Mod2TextType):
    pass


@dataclass(kw_only=True)
class NumericType(Mod2NumericType):
    pass


@dataclass(kw_only=True)
class PercentType(Mod2NumericType):
    pass


@dataclass(kw_only=True)
class PictureType(Mod2BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class QuantityType(Mod2QuantityType):
    pass


@dataclass(kw_only=True)
class RateType(Mod2NumericType):
    pass


@dataclass(kw_only=True)
class SoundType(Mod2BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class TextType(Mod2TextType):
    pass


@dataclass(kw_only=True)
class ValueType(Mod2NumericType):
    pass


@dataclass(kw_only=True)
class VideoType(Mod2BinaryObjectType):
    mime_code: str = field(
        metadata={
            "name": "mimeCode",
            "type": "Attribute",
        }
    )

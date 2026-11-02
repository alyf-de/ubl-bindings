from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class CharTwoFieldParamsType:
    m: int = field(
        metadata={
            "name": "M",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )


@dataclass(kw_only=True)
class CurveType:
    a: bytes = field(
        metadata={
            "name": "A",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "format": "base64",
        }
    )
    b: bytes = field(
        metadata={
            "name": "B",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "format": "base64",
        }
    )


@dataclass(kw_only=True)
class DerencodedKeyValueType:
    class Meta:
        name = "DEREncodedKeyValueType"

    value: bytes = field(
        default=b"",
        metadata={
            "format": "base64",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EcvalidationDataType:
    class Meta:
        name = "ECValidationDataType"

    seed: bytes = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "format": "base64",
        }
    )
    hash_algorithm: str = field(
        metadata={
            "name": "hashAlgorithm",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class KeyInfoReferenceType:
    uri: str = field(
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class NamedCurveType:
    uri: str = field(
        metadata={
            "name": "URI",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class PrimeFieldParamsType:
    p: bytes = field(
        metadata={
            "name": "P",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "format": "base64",
        }
    )


@dataclass(kw_only=True)
class X509DigestType:
    value: bytes = field(
        default=b"",
        metadata={
            "format": "base64",
        },
    )
    algorithm: str = field(
        metadata={
            "name": "Algorithm",
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class DerencodedKeyValue(DerencodedKeyValueType):
    class Meta:
        name = "DEREncodedKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class GnB(CharTwoFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class KeyInfoReference(KeyInfoReferenceType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class PnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "PnBFieldParamsType"

    k1: int = field(
        metadata={
            "name": "K1",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    k2: int = field(
        metadata={
            "name": "K2",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    k3: int = field(
        metadata={
            "name": "K3",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )


@dataclass(kw_only=True)
class Prime(PrimeFieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class TnBfieldParamsType(CharTwoFieldParamsType):
    class Meta:
        name = "TnBFieldParamsType"

    k: int = field(
        metadata={
            "name": "K",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )


@dataclass(kw_only=True)
class X509Digest(X509DigestType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class PnB(PnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class TnB(TnBfieldParamsType):
    class Meta:
        namespace = "http://www.w3.org/2009/xmldsig11#"


@dataclass(kw_only=True)
class FieldIdtype:
    class Meta:
        name = "FieldIDType"

    choice: None | Prime | TnB | PnB | GnB | object = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Prime",
                    "type": Prime,
                    "namespace": "http://www.w3.org/2009/xmldsig11#",
                },
                {
                    "name": "TnB",
                    "type": TnB,
                    "namespace": "http://www.w3.org/2009/xmldsig11#",
                },
                {
                    "name": "PnB",
                    "type": PnB,
                    "namespace": "http://www.w3.org/2009/xmldsig11#",
                },
                {
                    "name": "GnB",
                    "type": GnB,
                    "namespace": "http://www.w3.org/2009/xmldsig11#",
                },
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##other",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class EcparametersType:
    class Meta:
        name = "ECParametersType"

    field_id: FieldIdtype = field(
        metadata={
            "name": "FieldID",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    curve: CurveType = field(
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        }
    )
    base: bytes = field(
        metadata={
            "name": "Base",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "format": "base64",
        }
    )
    order: bytes = field(
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "format": "base64",
        }
    )
    co_factor: None | int = field(
        default=None,
        metadata={
            "name": "CoFactor",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        },
    )
    validation_data: None | EcvalidationDataType = field(
        default=None,
        metadata={
            "name": "ValidationData",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
        },
    )


@dataclass(kw_only=True)
class EckeyValueType:
    class Meta:
        name = "ECKeyValueType"

    ecparameters_or_named_curve: None | EcparametersType | NamedCurveType = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "ECParameters",
                        "type": EcparametersType,
                        "namespace": "http://www.w3.org/2009/xmldsig11#",
                    },
                    {
                        "name": "NamedCurve",
                        "type": NamedCurveType,
                        "namespace": "http://www.w3.org/2009/xmldsig11#",
                    },
                ),
            },
        )
    )
    public_key: bytes = field(
        metadata={
            "name": "PublicKey",
            "type": "Element",
            "namespace": "http://www.w3.org/2009/xmldsig11#",
            "format": "base64",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class EckeyValue(EckeyValueType):
    class Meta:
        name = "ECKeyValue"
        namespace = "http://www.w3.org/2009/xmldsig11#"

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["DocSearchParams", "TextOnlyDocSearchRequest", "VectorDocSearchRequest", "HybridDocSearchRequest"]


class TextOnlyDocSearchRequest(TypedDict, total=False):
    text: Required[str]

    connection_pool: object

    lang: str

    limit: int

    metadata_filter: object


class VectorDocSearchRequest(TypedDict, total=False):
    vector: Required[Iterable[float]]

    connection_pool: object

    confidence: float

    lang: str

    limit: int

    metadata_filter: object

    mmr_strength: float


class HybridDocSearchRequest(TypedDict, total=False):
    text: Required[str]

    vector: Required[Iterable[float]]

    connection_pool: object

    alpha: float

    confidence: float

    lang: str

    limit: int

    metadata_filter: object

    mmr_strength: float


DocSearchParams: TypeAlias = Union[TextOnlyDocSearchRequest, VectorDocSearchRequest, HybridDocSearchRequest]

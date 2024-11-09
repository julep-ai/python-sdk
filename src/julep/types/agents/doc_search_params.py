# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DocSearchParams", "TextOnlyDocSearchRequest", "VectorDocSearchRequest", "HybridDocSearchRequest"]


class TextOnlyDocSearchRequest(TypedDict, total=False):
    text: Required[str]

    lang: Literal["en-US"]

    limit: int

    metadata_filter: object

    mmr_strength: float


class VectorDocSearchRequest(TypedDict, total=False):
    vector: Required[Iterable[float]]

    confidence: float

    lang: Literal["en-US"]

    limit: int

    metadata_filter: object

    mmr_strength: float


class HybridDocSearchRequest(TypedDict, total=False):
    text: Required[str]

    vector: Required[Iterable[float]]

    alpha: float

    confidence: float

    lang: Literal["en-US"]

    limit: int

    metadata_filter: object

    mmr_strength: float


DocSearchParams: TypeAlias = Union[TextOnlyDocSearchRequest, VectorDocSearchRequest, HybridDocSearchRequest]

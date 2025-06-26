# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["DocSearchParams", "TextOnlyDocSearchRequest", "VectorDocSearchRequest", "HybridDocSearchRequest"]


class TextOnlyDocSearchRequest(TypedDict, total=False):
    text: Required[str]

    connection_pool: object

    include_embeddings: bool

    lang: str

    limit: int

    metadata_filter: object

    trigram_similarity_threshold: Optional[float]


class VectorDocSearchRequest(TypedDict, total=False):
    vector: Required[Iterable[float]]

    connection_pool: object

    confidence: float

    include_embeddings: bool

    limit: int

    metadata_filter: object

    mmr_strength: float


class HybridDocSearchRequest(TypedDict, total=False):
    text: Required[str]

    vector: Required[Iterable[float]]

    connection_pool: object

    alpha: float

    confidence: float

    include_embeddings: bool

    k_multiplier: int

    lang: str

    limit: int

    metadata_filter: object

    mmr_strength: float

    trigram_similarity_threshold: Optional[float]


DocSearchParams: TypeAlias = Union[TextOnlyDocSearchRequest, VectorDocSearchRequest, HybridDocSearchRequest]

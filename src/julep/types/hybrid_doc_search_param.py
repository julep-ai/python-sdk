# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["HybridDocSearchParam"]


class HybridDocSearchParam(TypedDict, total=False):
    alpha: float

    confidence: float

    include_embeddings: bool

    k_multiplier: int

    lang: str

    limit: int

    max_query_length: int

    metadata_filter: object

    mmr_strength: float

    mode: Literal["hybrid"]

    num_search_messages: int

    trigram_similarity_threshold: float

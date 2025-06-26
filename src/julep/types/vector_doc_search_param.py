# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VectorDocSearchParam"]


class VectorDocSearchParam(TypedDict, total=False):
    confidence: float

    include_embeddings: bool

    lang: str

    limit: int

    max_query_length: int

    metadata_filter: object

    mmr_strength: float

    mode: Literal["vector"]

    num_search_messages: int

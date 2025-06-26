# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TextOnlyDocSearchParam"]


class TextOnlyDocSearchParam(TypedDict, total=False):
    include_embeddings: bool

    lang: str

    limit: int

    max_query_length: int

    metadata_filter: object

    mode: Literal["text"]

    num_search_messages: int

    trigram_similarity_threshold: float

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HybridDocSearch"]


class HybridDocSearch(BaseModel):
    alpha: Optional[float] = None

    confidence: Optional[float] = None

    include_embeddings: Optional[bool] = None

    k_multiplier: Optional[int] = None

    lang: Optional[str] = None

    limit: Optional[int] = None

    max_query_length: Optional[int] = None

    metadata_filter: Optional[object] = None

    mmr_strength: Optional[float] = None

    mode: Optional[Literal["hybrid"]] = None

    num_search_messages: Optional[int] = None

    trigram_similarity_threshold: Optional[float] = None

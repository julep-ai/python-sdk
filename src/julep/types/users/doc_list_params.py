# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["DocListParams"]


class DocListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]

    include_embeddings: bool

    limit: int

    metadata_filter: Dict[str, object]

    offset: int

    sort_by: Literal["created_at", "updated_at"]

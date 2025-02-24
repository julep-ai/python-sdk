# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TransitionListParams"]


class TransitionListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]

    limit: int

    offset: int

    scope_id: Optional[str]

    sort_by: Literal["created_at", "updated_at"]

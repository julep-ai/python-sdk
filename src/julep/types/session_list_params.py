# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    direction: Literal["asc", "desc"]

    limit: int

    offset: int

    sort_by: Literal["created_at", "updated_at"]

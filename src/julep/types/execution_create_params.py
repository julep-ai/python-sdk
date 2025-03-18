# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExecutionCreateParams"]


class ExecutionCreateParams(TypedDict, total=False):
    input: Required[object]

    error: Optional[str]

    metadata: Optional[object]

    output: object

    transition_count: Optional[int]

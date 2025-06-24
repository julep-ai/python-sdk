# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpiderFetchArguments"]


class SpiderFetchArguments(TypedDict, total=False):
    url: Required[str]

    content_type: Literal["application/json", "text/csv", "application/xml", "application/jsonl"]

    params: Optional[object]

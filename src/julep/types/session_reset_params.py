# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SessionResetParams", "RecallOptions"]


class SessionResetParams(TypedDict, total=False):
    auto_run_tools: bool

    context_overflow: Optional[Literal["truncate", "adaptive"]]

    forward_tool_calls: bool

    metadata: Optional[object]

    recall_options: Optional[RecallOptions]

    render_templates: bool

    situation: Optional[str]

    system_template: str

    token_budget: Optional[int]


class RecallOptions(TypedDict, total=False):
    alpha: float

    confidence: float

    lang: Literal["en-US"]

    limit: int

    max_query_length: int

    metadata_filter: object

    mmr_strength: float

    mode: Literal["hybrid", "vector", "text"]

    num_search_messages: int
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SessionCreateParams", "RecallOptions"]


class SessionCreateParams(TypedDict, total=False):
    agent: Optional[str]

    agents: Optional[List[str]]

    auto_run_tools: bool

    context_overflow: Optional[Literal["truncate", "adaptive"]]

    forward_tool_calls: bool

    metadata: Optional[object]

    recall_options: Optional[RecallOptions]

    render_templates: bool

    situation: Optional[str]

    system_template: str

    token_budget: Optional[int]

    user: Optional[str]

    users: Optional[List[str]]


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

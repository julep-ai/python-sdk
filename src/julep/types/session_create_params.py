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

    metadata: Optional[object]

    recall_options: Optional[RecallOptions]

    render_templates: bool

    situation: str

    token_budget: Optional[int]

    user: Optional[str]

    users: Optional[List[str]]


class RecallOptions(TypedDict, total=False):
    confidence: float

    hybrid_alpha: float

    max_query_length: int

    mode: Literal["hybrid", "vector", "text"]

    num_search_messages: int

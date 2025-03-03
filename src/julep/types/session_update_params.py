# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = [
    "SessionUpdateParams",
    "RecallOptions",
    "RecallOptionsVectorDocSearchUpdate",
    "RecallOptionsTextOnlyDocSearchUpdate",
    "RecallOptionsHybridDocSearchUpdate",
]


class SessionUpdateParams(TypedDict, total=False):
    auto_run_tools: bool

    context_overflow: Optional[Literal["truncate", "adaptive"]]

    forward_tool_calls: bool

    metadata: Optional[object]

    recall_options: Optional[RecallOptions]

    render_templates: bool

    situation: Optional[str]

    system_template: Optional[str]

    token_budget: Optional[int]


class RecallOptionsVectorDocSearchUpdate(TypedDict, total=False):
    confidence: float

    lang: str

    limit: int

    max_query_length: int

    metadata_filter: object

    mmr_strength: float

    mode: Literal["vector"]

    num_search_messages: int


class RecallOptionsTextOnlyDocSearchUpdate(TypedDict, total=False):
    lang: str

    limit: int

    max_query_length: int

    metadata_filter: object

    mode: Literal["text"]

    num_search_messages: int


class RecallOptionsHybridDocSearchUpdate(TypedDict, total=False):
    alpha: float

    confidence: float

    lang: str

    limit: int

    max_query_length: int

    metadata_filter: object

    mmr_strength: float

    mode: Literal["hybrid"]

    num_search_messages: int


RecallOptions: TypeAlias = Union[
    RecallOptionsVectorDocSearchUpdate, RecallOptionsTextOnlyDocSearchUpdate, RecallOptionsHybridDocSearchUpdate
]

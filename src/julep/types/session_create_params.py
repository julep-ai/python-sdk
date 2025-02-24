# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SessionCreateParams",
    "RecallOptions",
    "RecallOptionsVectorDocSearch",
    "RecallOptionsTextOnlyDocSearch",
    "RecallOptionsHybridDocSearch",
]


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

    system_template: Optional[str]

    token_budget: Optional[int]

    user: Optional[str]

    users: Optional[List[str]]


class RecallOptionsVectorDocSearch(TypedDict, total=False):
    vector: Required[Iterable[float]]

    confidence: float

    lang: Literal["en-US"]

    limit: int

    max_query_length: int

    metadata_filter: object

    mmr_strength: float

    mode: str

    num_search_messages: int

    text: Optional[str]


class RecallOptionsTextOnlyDocSearch(TypedDict, total=False):
    text: Required[str]

    lang: Literal["en-US"]

    limit: int

    max_query_length: int

    metadata_filter: object

    mode: str

    num_search_messages: int


class RecallOptionsHybridDocSearch(TypedDict, total=False):
    text: Required[str]

    vector: Required[Iterable[float]]

    alpha: float

    confidence: float

    lang: Literal["en-US"]

    limit: int

    max_query_length: int

    metadata_filter: object

    mmr_strength: float

    mode: str

    num_search_messages: int


RecallOptions: TypeAlias = Union[
    RecallOptionsVectorDocSearch, RecallOptionsTextOnlyDocSearch, RecallOptionsHybridDocSearch
]

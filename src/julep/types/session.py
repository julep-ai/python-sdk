# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "Session",
    "RecallOptions",
    "RecallOptionsVectorDocSearch",
    "RecallOptionsTextOnlyDocSearch",
    "RecallOptionsHybridDocSearch",
]


class RecallOptionsVectorDocSearch(BaseModel):
    confidence: Optional[float] = None

    lang: Optional[str] = None

    limit: Optional[int] = None

    max_query_length: Optional[int] = None

    metadata_filter: Optional[object] = None

    mmr_strength: Optional[float] = None

    mode: Optional[Literal["vector"]] = None

    num_search_messages: Optional[int] = None


class RecallOptionsTextOnlyDocSearch(BaseModel):
    lang: Optional[str] = None

    limit: Optional[int] = None

    max_query_length: Optional[int] = None

    metadata_filter: Optional[object] = None

    mode: Optional[Literal["text"]] = None

    num_search_messages: Optional[int] = None


class RecallOptionsHybridDocSearch(BaseModel):
    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[str] = None

    limit: Optional[int] = None

    max_query_length: Optional[int] = None

    metadata_filter: Optional[object] = None

    mmr_strength: Optional[float] = None

    mode: Optional[Literal["hybrid"]] = None

    num_search_messages: Optional[int] = None


RecallOptions: TypeAlias = Union[
    RecallOptionsVectorDocSearch, RecallOptionsTextOnlyDocSearch, RecallOptionsHybridDocSearch, None
]


class Session(BaseModel):
    id: str

    created_at: datetime

    updated_at: datetime

    auto_run_tools: Optional[bool] = None

    context_overflow: Optional[Literal["truncate", "adaptive"]] = None

    forward_tool_calls: Optional[bool] = None

    kind: Optional[str] = None

    metadata: Optional[object] = None

    recall_options: Optional[RecallOptions] = None

    render_templates: Optional[bool] = None

    situation: Optional[str] = None

    summary: Optional[str] = None

    system_template: Optional[str] = None

    token_budget: Optional[int] = None

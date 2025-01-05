# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Session", "RecallOptions"]


class RecallOptions(BaseModel):
    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None

    max_query_length: Optional[int] = None

    metadata_filter: Optional[object] = None

    mmr_strength: Optional[float] = None

    mode: Optional[Literal["hybrid", "vector", "text"]] = None

    num_search_messages: Optional[int] = None


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

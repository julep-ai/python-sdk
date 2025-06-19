# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .hybrid_doc_search import HybridDocSearch
from .vector_doc_search import VectorDocSearch
from .text_only_doc_search import TextOnlyDocSearch

__all__ = ["Session", "RecallOptions"]

RecallOptions: TypeAlias = Union[VectorDocSearch, TextOnlyDocSearch, HybridDocSearch, None]


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

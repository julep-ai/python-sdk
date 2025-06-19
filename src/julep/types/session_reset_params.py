# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .hybrid_doc_search_param import HybridDocSearchParam
from .vector_doc_search_param import VectorDocSearchParam
from .text_only_doc_search_param import TextOnlyDocSearchParam

__all__ = ["SessionResetParams", "RecallOptions"]


class SessionResetParams(TypedDict, total=False):
    auto_run_tools: bool

    context_overflow: Optional[Literal["truncate", "adaptive"]]

    forward_tool_calls: bool

    metadata: Optional[object]

    recall_options: Optional[RecallOptions]

    render_templates: bool

    situation: Optional[str]

    system_template: Optional[str]

    token_budget: Optional[int]


RecallOptions: TypeAlias = Union[VectorDocSearchParam, TextOnlyDocSearchParam, HybridDocSearchParam]

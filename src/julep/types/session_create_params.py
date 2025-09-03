# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .hybrid_doc_search_param import HybridDocSearchParam
from .vector_doc_search_param import VectorDocSearchParam
from .text_only_doc_search_param import TextOnlyDocSearchParam

__all__ = ["SessionCreateParams", "RecallOptions"]


class SessionCreateParams(TypedDict, total=False):
    agent: Optional[str]

    agents: Optional[SequenceNotStr[str]]

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

    users: Optional[SequenceNotStr[str]]


RecallOptions: TypeAlias = Union[VectorDocSearchParam, TextOnlyDocSearchParam, HybridDocSearchParam]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    agent: Optional[str]

    agents: Optional[List[str]]

    context_overflow: Optional[Literal["truncate", "adaptive"]]

    forward_tool_results: Optional[bool]

    metadata: Optional[object]

    render_templates: bool

    situation: str

    token_budget: Optional[int]

    user: Optional[str]

    users: Optional[List[str]]

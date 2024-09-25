# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolPatchParams", "Function", "Integration", "System"]


class ToolPatchParams(TypedDict, total=False):
    agent_id: Required[str]

    function: Optional[Function]
    """Function definition"""

    integration: Optional[Integration]
    """Integration definition"""

    name: Optional[str]

    system: Optional[System]
    """System definition"""

    type: Literal["function", "integration", "system", "api_call"]


class Function(TypedDict, total=False):
    description: Optional[str]

    name: Optional[object]

    parameters: Optional[object]


class Integration(TypedDict, total=False):
    arguments: Optional[object]

    description: Optional[str]

    method: Optional[str]

    provider: Optional[
        Literal["dummy", "dall-e", "duckduckgo", "hackernews", "weather", "wikipedia", "twitter", "webpage", "requests"]
    ]

    setup: Optional[object]


class System(TypedDict, total=False):
    arguments: Optional[object]

    call: Optional[str]

    description: Optional[str]

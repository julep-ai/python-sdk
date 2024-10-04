# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
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


class Function(TypedDict, total=False):
    description: Optional[str]

    name: Optional[object]

    parameters: Optional[object]


class Integration(TypedDict, total=False):
    arguments: Optional[object]

    description: Optional[str]

    method: Optional[str]

    provider: Union[
        Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str, None
    ]

    setup: Optional[object]


class System(TypedDict, total=False):
    arguments: Optional[object]

    call: Optional[str]

    description: Optional[str]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolCreateParams", "Function", "Integration", "System"]


class ToolCreateParams(TypedDict, total=False):
    name: Required[str]

    function: Optional[Function]
    """Function definition"""

    integration: Optional[Integration]
    """Integration definition"""

    system: Optional[System]
    """System definition"""


class Function(TypedDict, total=False):
    description: Optional[str]

    name: Optional[object]

    parameters: Optional[object]


class Integration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]
    ]

    arguments: Optional[object]

    description: Optional[str]

    method: Optional[str]

    setup: Optional[object]


class System(TypedDict, total=False):
    call: Required[str]

    arguments: Optional[object]

    description: Optional[str]

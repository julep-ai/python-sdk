# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolPatchParams", "APICall", "Function", "Integration", "System"]


class ToolPatchParams(TypedDict, total=False):
    agent_id: Required[str]

    api_call: Optional[APICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[Function]
    """Function definition"""

    integration: Optional[Integration]
    """Integration definition"""

    name: Optional[str]

    system: Optional[System]
    """System definition"""


class APICall(TypedDict, total=False):
    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[Dict[str, str]]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    params: Union[str, object, None]

    url: Optional[str]


class Function(TypedDict, total=False):
    description: Optional[str]

    name: Optional[object]

    parameters: Optional[object]


class Integration(TypedDict, total=False):
    arguments: Optional[object]

    method: Optional[str]

    provider: Union[
        Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str, None
    ]

    setup: Optional[object]


class System(TypedDict, total=False):
    arguments: Optional[object]

    call: Optional[str]

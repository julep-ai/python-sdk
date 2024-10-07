# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolUpdateParams", "APICall", "Function", "Integration", "System"]


class ToolUpdateParams(TypedDict, total=False):
    agent_id: Required[str]

    name: Required[str]

    api_call: Optional[APICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[Function]
    """Function definition"""

    integration: Optional[Integration]
    """Integration definition"""

    system: Optional[System]
    """System definition"""


class APICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class Function(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class Integration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class System(TypedDict, total=False):
    operation: Required[
        Literal[
            "create",
            "update",
            "patch",
            "create_or_update",
            "embed",
            "change_status",
            "search",
            "chat",
            "history",
            "delete",
            "get",
            "list",
        ]
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]

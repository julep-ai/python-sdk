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

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    params: Union[str, object, None]

    timeout: Optional[int]

    url: Optional[str]


class Function(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class Integration(TypedDict, total=False):
    arguments: Optional[object]

    method: Optional[str]

    provider: Union[
        Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str, None
    ]

    setup: Optional[object]


class System(TypedDict, total=False):
    arguments: Optional[object]

    operation: Optional[
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

    resource: Optional[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]

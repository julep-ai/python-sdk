# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Tool", "APICall", "Function", "Integration", "System"]


class APICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class Function(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class Integration(BaseModel):
    provider: Union[
        Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str
    ]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class System(BaseModel):
    operation: Literal[
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

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class Tool(BaseModel):
    name: str

    api_call: Optional[APICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[Function] = None
    """Function definition"""

    inherited: Optional[bool] = None

    integration: Optional[Integration] = None
    """Integration definition"""

    system: Optional[System] = None
    """System definition"""

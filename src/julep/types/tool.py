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

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class Function(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class Integration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class System(BaseModel):
    call: str

    arguments: Optional[object] = None


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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolListResponse", "Function", "Integration", "System"]


class Function(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class Integration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    description: Optional[str] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class System(BaseModel):
    call: str

    arguments: Optional[object] = None

    description: Optional[str] = None


class ToolListResponse(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    function: Optional[Function] = None
    """Function definition"""

    integration: Optional[Integration] = None
    """Integration definition"""

    system: Optional[System] = None
    """System definition"""

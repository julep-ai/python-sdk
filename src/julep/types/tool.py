# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tool", "Function", "Integration", "System"]


class Function(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class Integration(BaseModel):
    provider: Literal[
        "dummy", "dall-e", "duckduckgo", "hackernews", "weather", "wikipedia", "twitter", "webpage", "requests"
    ]

    arguments: Optional[object] = None

    description: Optional[str] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class System(BaseModel):
    call: str

    arguments: Optional[object] = None

    description: Optional[str] = None


class Tool(BaseModel):
    name: str

    function: Optional[Function] = None
    """Function definition"""

    inherited: Optional[bool] = None

    integration: Optional[Integration] = None
    """Integration definition"""

    system: Optional[System] = None
    """System definition"""

    type: Optional[Literal["function", "integration", "system", "api_call"]] = None

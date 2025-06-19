# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .function_call_option import FunctionCallOption

__all__ = ["NamedToolChoice"]


class NamedToolChoice(BaseModel):
    function: Optional[FunctionCallOption] = None

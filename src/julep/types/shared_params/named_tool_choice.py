# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .function_call_option import FunctionCallOption

__all__ = ["NamedToolChoice"]


class NamedToolChoice(TypedDict, total=False):
    function: Optional[FunctionCallOption]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolCallStepParam"]


class ToolCallStepParam(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Literal["_"], object]

    label: Optional[str]

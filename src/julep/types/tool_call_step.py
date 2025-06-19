# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolCallStep"]


class ToolCallStep(BaseModel):
    tool: str

    arguments: Union[Literal["_"], object, None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

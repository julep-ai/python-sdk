# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .wait_for_input_info import WaitForInputInfo

__all__ = ["WaitForInputStep"]


class WaitForInputStep(BaseModel):
    wait_for_input: WaitForInputInfo

    kind: Optional[Literal["wait_for_input"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

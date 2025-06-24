# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .case_then_output import CaseThenOutput

__all__ = ["SwitchStepOutput"]


class SwitchStepOutput(BaseModel):
    switch: List[CaseThenOutput]

    kind: Optional[Literal["switch"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ErrorWorkflowStep"]


class ErrorWorkflowStep(BaseModel):
    error: str

    kind: Optional[Literal["error"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

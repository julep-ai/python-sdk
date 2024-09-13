# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransitionListResponse", "Current", "Next"]


class Current(BaseModel):
    step: int

    workflow: str


class Next(BaseModel):
    step: int

    workflow: str


class TransitionListResponse(BaseModel):
    id: str

    created_at: datetime

    current: Current

    execution_id: str

    next: Optional[Next] = None

    output: object

    type: Literal["init", "init_branch", "finish", "finish_branch", "wait", "resume", "error", "step", "cancelled"]

    updated_at: datetime

    metadata: Optional[object] = None

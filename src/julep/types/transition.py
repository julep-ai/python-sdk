# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Transition", "Current", "Next"]


class Current(BaseModel):
    scope_id: str

    step: int

    workflow: str


class Next(BaseModel):
    scope_id: str

    step: int

    workflow: str


class Transition(BaseModel):
    id: str

    created_at: datetime

    current: Current

    execution_id: str

    next: Optional[Next] = None

    output: object

    type: Literal["init", "init_branch", "finish", "finish_branch", "wait", "resume", "error", "step", "cancelled"]

    updated_at: datetime

    metadata: Optional[object] = None

    step_label: Optional[str] = None

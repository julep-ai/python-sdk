# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Execution"]


class Execution(BaseModel):
    id: str

    created_at: datetime

    input: object

    status: Literal["queued", "starting", "running", "awaiting_input", "succeeded", "failed", "cancelled"]

    task_id: str

    updated_at: datetime

    error: Optional[str] = None

    metadata: Optional[object] = None

    output: Optional[object] = None

    transition_count: Optional[int] = None

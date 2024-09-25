# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    id: str

    created_at: datetime

    updated_at: datetime

    context_overflow: Optional[Literal["truncate", "adaptive"]] = None

    forward_tool_results: Optional[bool] = None

    kind: Optional[str] = None

    metadata: Optional[object] = None

    render_templates: Optional[bool] = None

    situation: Optional[str] = None

    summary: Optional[str] = None

    token_budget: Optional[int] = None

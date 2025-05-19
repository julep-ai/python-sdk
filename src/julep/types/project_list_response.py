# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    canonical_name: Optional[str] = None

    metadata: Optional[object] = None

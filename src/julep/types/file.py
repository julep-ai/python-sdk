# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str

    content: str

    created_at: datetime

    hash: str

    name: str

    size: int

    description: Optional[str] = None

    mime_type: Optional[str] = None

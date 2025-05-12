# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: str

    created_at: datetime

    updated_at: datetime

    about: Optional[str] = None

    metadata: Optional[object] = None

    name: Optional[str] = None

    project: Optional[str] = None

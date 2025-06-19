# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserDeleteResponse"]


class UserDeleteResponse(BaseModel):
    id: str

    deleted_at: datetime

    jobs: Optional[List[str]] = None

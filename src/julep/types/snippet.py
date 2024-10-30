# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Snippet"]


class Snippet(BaseModel):
    content: str

    index: int

    embedding: Optional[List[float]] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Doc"]


class Doc(BaseModel):
    id: str

    content: Union[str, List[str]]

    created_at: datetime

    title: str

    embeddings: Union[List[float], List[List[float]], None] = None

    metadata: Optional[object] = None

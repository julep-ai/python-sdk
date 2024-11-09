# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..snippet import Snippet
from ..._models import BaseModel

__all__ = ["DocSearchResponse", "Doc", "DocOwner"]


class DocOwner(BaseModel):
    id: str

    role: Literal["user", "agent"]


class Doc(BaseModel):
    id: str

    owner: DocOwner

    snippet: Snippet

    distance: Optional[float] = None

    metadata: Optional[object] = None

    title: Optional[str] = None


class DocSearchResponse(BaseModel):
    docs: List[Doc]

    time: float

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrowserbaseCompleteSessionArguments"]


class BrowserbaseCompleteSessionArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None

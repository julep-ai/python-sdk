# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BaseTokenLogProb"]


class BaseTokenLogProb(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

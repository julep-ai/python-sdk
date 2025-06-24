# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .base_token_log_prob import BaseTokenLogProb

__all__ = ["TokenLogProb"]


class TokenLogProb(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[BaseTokenLogProb]

    bytes: Optional[List[int]] = None

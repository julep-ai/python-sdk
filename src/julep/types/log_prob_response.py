# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .token_log_prob import TokenLogProb

__all__ = ["LogProbResponse"]


class LogProbResponse(BaseModel):
    content: Optional[List[TokenLogProb]] = None

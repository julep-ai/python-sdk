# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SpiderFetchArguments"]


class SpiderFetchArguments(BaseModel):
    url: str

    content_type: Optional[Literal["application/json", "text/csv", "application/xml", "application/jsonl"]] = None

    params: Optional[object] = None

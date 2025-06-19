# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.doc_reference import DocReference

__all__ = ["DocSearchResponse"]


class DocSearchResponse(BaseModel):
    docs: List[DocReference]

    time: float

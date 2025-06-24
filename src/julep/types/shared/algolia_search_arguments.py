# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AlgoliaSearchArguments"]


class AlgoliaSearchArguments(BaseModel):
    index_name: str

    query: str

    attributes_to_retrieve: Optional[List[str]] = None

    hits_per_page: Optional[int] = None

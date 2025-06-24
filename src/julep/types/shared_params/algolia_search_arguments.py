# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AlgoliaSearchArguments"]


class AlgoliaSearchArguments(TypedDict, total=False):
    index_name: Required[str]

    query: Required[str]

    attributes_to_retrieve: Optional[List[str]]

    hits_per_page: int

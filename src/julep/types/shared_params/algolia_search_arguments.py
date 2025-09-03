# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AlgoliaSearchArguments"]


class AlgoliaSearchArguments(TypedDict, total=False):
    index_name: Required[str]

    query: Required[str]

    attributes_to_retrieve: Optional[SequenceNotStr[str]]

    hits_per_page: int

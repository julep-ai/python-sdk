# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ArxivSearchArguments"]


class ArxivSearchArguments(TypedDict, total=False):
    query: Required[str]

    download_pdf: bool

    id_list: Optional[SequenceNotStr[str]]

    max_results: int

    sort_by: Literal["relevance", "lastUpdatedDate", "submittedDate"]

    sort_order: Literal["ascending", "descending"]

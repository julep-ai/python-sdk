# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ArxivSearchArguments"]


class ArxivSearchArguments(BaseModel):
    query: str

    download_pdf: Optional[bool] = None

    id_list: Optional[List[str]] = None

    max_results: Optional[int] = None

    sort_by: Optional[Literal["relevance", "lastUpdatedDate", "submittedDate"]] = None

    sort_order: Optional[Literal["ascending", "descending"]] = None

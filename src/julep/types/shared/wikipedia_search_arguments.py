# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["WikipediaSearchArguments"]


class WikipediaSearchArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None

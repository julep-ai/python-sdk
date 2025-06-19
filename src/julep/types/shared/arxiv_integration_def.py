# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .arxiv_search_arguments import ArxivSearchArguments

__all__ = ["ArxivIntegrationDef"]


class ArxivIntegrationDef(BaseModel):
    arguments: Optional[ArxivSearchArguments] = None
    """Arguments for Arxiv Search"""

    method: Optional[str] = None

    provider: Optional[Literal["arxiv"]] = None

    setup: Optional[object] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .arxiv_search_arguments import ArxivSearchArguments

__all__ = ["ArxivIntegrationDef"]


class ArxivIntegrationDef(TypedDict, total=False):
    arguments: Optional[ArxivSearchArguments]
    """Arguments for Arxiv Search"""

    method: Optional[str]

    provider: Literal["arxiv"]

    setup: object

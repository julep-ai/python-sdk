# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .wikipedia_search_arguments import WikipediaSearchArguments

__all__ = ["WikipediaIntegrationDef"]


class WikipediaIntegrationDef(TypedDict, total=False):
    arguments: Optional[WikipediaSearchArguments]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: object

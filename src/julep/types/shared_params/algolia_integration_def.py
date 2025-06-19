# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .algolia_setup import AlgoliaSetup
from .algolia_search_arguments import AlgoliaSearchArguments

__all__ = ["AlgoliaIntegrationDef"]


class AlgoliaIntegrationDef(TypedDict, total=False):
    arguments: Optional[AlgoliaSearchArguments]
    """Arguments for Algolia Search"""

    method: Optional[str]

    provider: Literal["algolia"]

    setup: Optional[AlgoliaSetup]
    """Integration definition for Algolia"""

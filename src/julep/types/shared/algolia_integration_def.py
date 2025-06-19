# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .algolia_setup import AlgoliaSetup
from .algolia_search_arguments import AlgoliaSearchArguments

__all__ = ["AlgoliaIntegrationDef"]


class AlgoliaIntegrationDef(BaseModel):
    arguments: Optional[AlgoliaSearchArguments] = None
    """Arguments for Algolia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["algolia"]] = None

    setup: Optional[AlgoliaSetup] = None
    """Integration definition for Algolia"""

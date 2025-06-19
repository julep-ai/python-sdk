# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .brave_search_setup import BraveSearchSetup
from .brave_search_arguments import BraveSearchArguments

__all__ = ["BraveIntegrationDef"]


class BraveIntegrationDef(BaseModel):
    arguments: Optional[BraveSearchArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[BraveSearchSetup] = None
    """Integration definition for Brave Search"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .brave_search_setup import BraveSearchSetup
from .brave_search_arguments import BraveSearchArguments

__all__ = ["BraveIntegrationDef"]


class BraveIntegrationDef(TypedDict, total=False):
    arguments: Optional[BraveSearchArguments]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[BraveSearchSetup]
    """Integration definition for Brave Search"""

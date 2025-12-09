# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BraveSearchSetup"]


class BraveSearchSetup(TypedDict, total=False):
    """Integration definition for Brave Search"""

    brave_api_key: Required[str]

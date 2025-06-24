# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .browserbase_setup import BrowserbaseSetup
from .browserbase_get_session_live_urls_arguments import BrowserbaseGetSessionLiveURLsArguments

__all__ = ["BrowserbaseGetSessionLiveURLsIntegrationDef"]


class BrowserbaseGetSessionLiveURLsIntegrationDef(TypedDict, total=False):
    arguments: Optional[BrowserbaseGetSessionLiveURLsArguments]

    method: Literal["get_live_urls"]

    provider: Literal["browserbase"]

    setup: Optional[BrowserbaseSetup]
    """The setup parameters for the browserbase integration"""

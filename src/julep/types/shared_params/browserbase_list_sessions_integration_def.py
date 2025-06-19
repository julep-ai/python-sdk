# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .browserbase_setup import BrowserbaseSetup
from .browserbase_list_sessions_arguments import BrowserbaseListSessionsArguments

__all__ = ["BrowserbaseListSessionsIntegrationDef"]


class BrowserbaseListSessionsIntegrationDef(TypedDict, total=False):
    arguments: Optional[BrowserbaseListSessionsArguments]

    method: Literal["list_sessions"]

    provider: Literal["browserbase"]

    setup: Optional[BrowserbaseSetup]
    """The setup parameters for the browserbase integration"""

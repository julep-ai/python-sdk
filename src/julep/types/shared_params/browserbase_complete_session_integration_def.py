# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .browserbase_setup import BrowserbaseSetup
from .browserbase_complete_session_arguments import BrowserbaseCompleteSessionArguments

__all__ = ["BrowserbaseCompleteSessionIntegrationDef"]


class BrowserbaseCompleteSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[BrowserbaseCompleteSessionArguments]

    method: Literal["complete_session"]

    provider: Literal["browserbase"]

    setup: Optional[BrowserbaseSetup]
    """The setup parameters for the browserbase integration"""

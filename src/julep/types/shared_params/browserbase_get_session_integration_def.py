# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .browserbase_setup import BrowserbaseSetup
from .browserbase_get_session_arguments import BrowserbaseGetSessionArguments

__all__ = ["BrowserbaseGetSessionIntegrationDef"]


class BrowserbaseGetSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[BrowserbaseGetSessionArguments]

    method: Literal["get_session"]

    provider: Literal["browserbase"]

    setup: Optional[BrowserbaseSetup]
    """The setup parameters for the browserbase integration"""

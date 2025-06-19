# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .browserbase_setup import BrowserbaseSetup
from .browserbase_context_arguments import BrowserbaseContextArguments

__all__ = ["BrowserbaseContextIntegrationDef"]


class BrowserbaseContextIntegrationDef(TypedDict, total=False):
    arguments: Optional[BrowserbaseContextArguments]

    method: Literal["create_context"]

    provider: Literal["browserbase"]

    setup: Optional[BrowserbaseSetup]
    """The setup parameters for the browserbase integration"""

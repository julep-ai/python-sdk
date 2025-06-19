# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .browserbase_setup import BrowserbaseSetup
from .browserbase_extension_arguments import BrowserbaseExtensionArguments

__all__ = ["BrowserbaseExtensionIntegrationDef"]


class BrowserbaseExtensionIntegrationDef(TypedDict, total=False):
    arguments: Optional[BrowserbaseExtensionArguments]

    method: Optional[Literal["install_extension_from_github"]]

    provider: Literal["browserbase"]

    setup: Optional[BrowserbaseSetup]
    """The setup parameters for the browserbase integration"""

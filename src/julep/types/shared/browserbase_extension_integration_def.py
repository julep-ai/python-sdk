# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browserbase_setup import BrowserbaseSetup
from .browserbase_extension_arguments import BrowserbaseExtensionArguments

__all__ = ["BrowserbaseExtensionIntegrationDef"]


class BrowserbaseExtensionIntegrationDef(BaseModel):
    arguments: Optional[BrowserbaseExtensionArguments] = None

    method: Optional[Literal["install_extension_from_github"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[BrowserbaseSetup] = None
    """The setup parameters for the browserbase integration"""

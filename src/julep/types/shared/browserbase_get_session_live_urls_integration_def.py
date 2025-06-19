# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browserbase_setup import BrowserbaseSetup
from .browserbase_get_session_live_urls_arguments import BrowserbaseGetSessionLiveURLsArguments

__all__ = ["BrowserbaseGetSessionLiveURLsIntegrationDef"]


class BrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: Optional[BrowserbaseGetSessionLiveURLsArguments] = None

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[BrowserbaseSetup] = None
    """The setup parameters for the browserbase integration"""

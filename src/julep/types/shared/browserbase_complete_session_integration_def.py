# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .browserbase_setup import BrowserbaseSetup
from .browserbase_complete_session_arguments import BrowserbaseCompleteSessionArguments

__all__ = ["BrowserbaseCompleteSessionIntegrationDef"]


class BrowserbaseCompleteSessionIntegrationDef(BaseModel):
    arguments: Optional[BrowserbaseCompleteSessionArguments] = None

    method: Optional[Literal["complete_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[BrowserbaseSetup] = None
    """The setup parameters for the browserbase integration"""

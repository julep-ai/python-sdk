# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .remote_browser_setup import RemoteBrowserSetup
from .remote_browser_arguments import RemoteBrowserArguments

__all__ = ["RemoteBrowserIntegrationDef"]


class RemoteBrowserIntegrationDef(BaseModel):
    setup: RemoteBrowserSetup
    """The setup parameters for the remote browser"""

    arguments: Optional[RemoteBrowserArguments] = None
    """The arguments for the remote browser"""

    method: Optional[Literal["perform_action"]] = None

    provider: Optional[Literal["remote_browser"]] = None

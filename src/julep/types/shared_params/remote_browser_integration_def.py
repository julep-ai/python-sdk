# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .remote_browser_setup import RemoteBrowserSetup
from .remote_browser_arguments import RemoteBrowserArguments

__all__ = ["RemoteBrowserIntegrationDef"]


class RemoteBrowserIntegrationDef(TypedDict, total=False):
    setup: Required[RemoteBrowserSetup]
    """The setup parameters for the remote browser"""

    arguments: Optional[RemoteBrowserArguments]
    """The arguments for the remote browser"""

    method: Literal["perform_action"]

    provider: Literal["remote_browser"]

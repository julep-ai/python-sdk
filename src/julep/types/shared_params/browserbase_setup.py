# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BrowserbaseSetup"]


class BrowserbaseSetup(TypedDict, total=False):
    """The setup parameters for the browserbase integration"""

    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]

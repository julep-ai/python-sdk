# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BrowserbaseSetupUpdateParam"]


class BrowserbaseSetupUpdateParam(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]

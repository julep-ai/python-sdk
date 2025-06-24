# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .spider_setup import SpiderSetup
from .spider_fetch_arguments import SpiderFetchArguments

__all__ = ["SpiderIntegrationDef"]


class SpiderIntegrationDef(TypedDict, total=False):
    arguments: Optional[SpiderFetchArguments]
    """Arguments for Spider integration"""

    method: Optional[Literal["crawl", "links", "screenshot", "search"]]

    provider: Literal["spider"]

    setup: Optional[SpiderSetup]
    """Setup parameters for Spider integration"""

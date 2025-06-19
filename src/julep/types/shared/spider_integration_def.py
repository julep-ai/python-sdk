# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .spider_setup import SpiderSetup
from .spider_fetch_arguments import SpiderFetchArguments

__all__ = ["SpiderIntegrationDef"]


class SpiderIntegrationDef(BaseModel):
    arguments: Optional[SpiderFetchArguments] = None
    """Arguments for Spider integration"""

    method: Optional[Literal["crawl", "links", "screenshot", "search"]] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[SpiderSetup] = None
    """Setup parameters for Spider integration"""

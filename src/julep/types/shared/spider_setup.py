# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SpiderSetup"]


class SpiderSetup(BaseModel):
    """Setup parameters for Spider integration"""

    spider_api_key: str

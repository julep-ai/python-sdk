# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BrowserbaseSetup"]


class BrowserbaseSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None

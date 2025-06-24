# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RemoteBrowserSetup"]


class RemoteBrowserSetup(BaseModel):
    connect_url: Optional[str] = None

    height: Optional[int] = None

    width: Optional[int] = None

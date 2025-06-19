# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudinarySetup"]


class CloudinarySetup(BaseModel):
    cloudinary_api_key: str

    cloudinary_api_secret: str

    cloudinary_cloud_name: str

    params: Optional[object] = None

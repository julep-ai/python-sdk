# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CloudinaryUploadArguments"]


class CloudinaryUploadArguments(BaseModel):
    file: str

    public_id: Optional[str] = None

    return_base64: Optional[bool] = None

    upload_params: Optional[object] = None

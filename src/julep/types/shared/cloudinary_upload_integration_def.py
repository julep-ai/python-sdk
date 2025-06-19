# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .cloudinary_setup import CloudinarySetup
from .cloudinary_upload_arguments import CloudinaryUploadArguments

__all__ = ["CloudinaryUploadIntegrationDef"]


class CloudinaryUploadIntegrationDef(BaseModel):
    arguments: Optional[CloudinaryUploadArguments] = None
    """Arguments for Cloudinary media upload"""

    method: Optional[Literal["media_upload"]] = None

    provider: Optional[Literal["cloudinary"]] = None

    setup: Optional[CloudinarySetup] = None
    """Setup parameters for Cloudinary integration"""

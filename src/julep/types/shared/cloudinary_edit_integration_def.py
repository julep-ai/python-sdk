# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .cloudinary_setup import CloudinarySetup
from .cloudinary_edit_arguments import CloudinaryEditArguments

__all__ = ["CloudinaryEditIntegrationDef"]


class CloudinaryEditIntegrationDef(BaseModel):
    arguments: Optional[CloudinaryEditArguments] = None
    """Arguments for Cloudinary media edit"""

    method: Optional[Literal["media_edit"]] = None

    provider: Optional[Literal["cloudinary"]] = None

    setup: Optional[CloudinarySetup] = None
    """Setup parameters for Cloudinary integration"""

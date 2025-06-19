# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .cloudinary_setup import CloudinarySetup
from .cloudinary_upload_arguments import CloudinaryUploadArguments

__all__ = ["CloudinaryUploadIntegrationDef"]


class CloudinaryUploadIntegrationDef(TypedDict, total=False):
    arguments: Optional[CloudinaryUploadArguments]
    """Arguments for Cloudinary media upload"""

    method: Literal["media_upload"]

    provider: Literal["cloudinary"]

    setup: Optional[CloudinarySetup]
    """Setup parameters for Cloudinary integration"""

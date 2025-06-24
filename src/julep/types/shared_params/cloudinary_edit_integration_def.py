# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .cloudinary_setup import CloudinarySetup
from .cloudinary_edit_arguments import CloudinaryEditArguments

__all__ = ["CloudinaryEditIntegrationDef"]


class CloudinaryEditIntegrationDef(TypedDict, total=False):
    arguments: Optional[CloudinaryEditArguments]
    """Arguments for Cloudinary media edit"""

    method: Literal["media_edit"]

    provider: Literal["cloudinary"]

    setup: Optional[CloudinarySetup]
    """Setup parameters for Cloudinary integration"""

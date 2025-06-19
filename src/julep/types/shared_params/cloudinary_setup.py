# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudinarySetup"]


class CloudinarySetup(TypedDict, total=False):
    cloudinary_api_key: Required[str]

    cloudinary_api_secret: Required[str]

    cloudinary_cloud_name: Required[str]

    params: Optional[object]

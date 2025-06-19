# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CloudinaryUploadArguments"]


class CloudinaryUploadArguments(TypedDict, total=False):
    file: Required[str]

    public_id: Optional[str]

    return_base64: bool

    upload_params: Optional[object]

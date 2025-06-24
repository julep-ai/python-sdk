# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CloudinaryEditArguments"]


class CloudinaryEditArguments(BaseModel):
    public_id: str

    transformation: List[object]

    return_base64: Optional[bool] = None

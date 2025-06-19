# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["LlamaParseSetup"]


class LlamaParseSetup(BaseModel):
    llamaparse_api_key: str

    params: Optional[object] = None

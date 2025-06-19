# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = ["LlamaParseFetchArguments"]


class LlamaParseFetchArguments(BaseModel):
    file: Union[str, List[str]]

    base64: Optional[bool] = None

    filename: Optional[str] = None

    params: Optional[object] = None

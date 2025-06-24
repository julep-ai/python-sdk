# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ..._models import BaseModel

__all__ = ["FfmpegSearchArguments"]


class FfmpegSearchArguments(BaseModel):
    cmd: str

    file: Union[str, List[str], None] = None

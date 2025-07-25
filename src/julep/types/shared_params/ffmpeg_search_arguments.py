# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["FfmpegSearchArguments"]


class FfmpegSearchArguments(TypedDict, total=False):
    cmd: Required[str]

    file: Union[str, List[str], None]

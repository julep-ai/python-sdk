# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["FfmpegSearchArguments"]


class FfmpegSearchArguments(TypedDict, total=False):
    cmd: Required[str]

    file: Union[str, SequenceNotStr[str], None]

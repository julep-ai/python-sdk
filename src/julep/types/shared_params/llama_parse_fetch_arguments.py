# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["LlamaParseFetchArguments"]


class LlamaParseFetchArguments(TypedDict, total=False):
    file: Required[Union[str, SequenceNotStr[str]]]

    base64: bool

    filename: Optional[str]

    params: Optional[object]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["LlamaParseFetchArguments"]


class LlamaParseFetchArguments(TypedDict, total=False):
    file: Required[Union[str, List[str]]]

    base64: bool

    filename: Optional[str]

    params: Optional[object]

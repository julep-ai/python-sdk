# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WaitForInputInfoParam"]


class WaitForInputInfoParam(TypedDict, total=False):
    info: Required[Dict[str, Union[SequenceNotStr[str], Dict[str, str], Iterable[Dict[str, str]], str]]]

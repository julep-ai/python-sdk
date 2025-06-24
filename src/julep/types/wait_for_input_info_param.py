# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["WaitForInputInfoParam"]


class WaitForInputInfoParam(TypedDict, total=False):
    info: Required[Dict[str, Union[List[str], Dict[str, str], Iterable[Dict[str, str]], str]]]

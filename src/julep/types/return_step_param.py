# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["ReturnStepParam"]

_ReturnStepParamReservedKeywords = TypedDict(
    "_ReturnStepParamReservedKeywords",
    {
        "return": Dict[str, Union[List[str], Dict[str, str], Iterable[Dict[str, str]], str]],
    },
    total=False,
)


class ReturnStepParam(_ReturnStepParamReservedKeywords, total=False):
    label: Optional[str]

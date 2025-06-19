# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["YieldStepParam"]


class YieldStepParam(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, Union[List[str], Dict[str, str], Iterable[Dict[str, str]], str]], Literal["_"]]

    label: Optional[str]

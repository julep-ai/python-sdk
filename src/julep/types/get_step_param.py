# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["GetStepParam"]


class GetStepParam(TypedDict, total=False):
    get: Required[str]

    label: Optional[str]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .sleep_for_param import SleepForParam

__all__ = ["SleepStepParam"]


class SleepStepParam(TypedDict, total=False):
    sleep: Required[SleepForParam]

    label: Optional[str]

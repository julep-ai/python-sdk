# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .wait_for_input_info_param import WaitForInputInfoParam

__all__ = ["WaitForInputStepParam"]


class WaitForInputStepParam(TypedDict, total=False):
    wait_for_input: Required[WaitForInputInfoParam]

    label: Optional[str]

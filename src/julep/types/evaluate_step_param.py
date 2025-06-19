# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluateStepParam"]


class EvaluateStepParam(TypedDict, total=False):
    evaluate: Required[Dict[str, Union[str, object]]]

    label: Optional[str]

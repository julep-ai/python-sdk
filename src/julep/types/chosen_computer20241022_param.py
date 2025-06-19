# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChosenComputer20241022Param"]


class ChosenComputer20241022Param(TypedDict, total=False):
    action: Required[
        Literal[
            "key",
            "type",
            "cursor_position",
            "mouse_move",
            "left_click",
            "right_click",
            "middle_click",
            "double_click",
            "screenshot",
        ]
    ]

    coordinate: Optional[Iterable[int]]

    text: Optional[str]

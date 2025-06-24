# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RemoteBrowserArguments"]


class RemoteBrowserArguments(TypedDict, total=False):
    action: Required[
        Literal[
            "key",
            "type",
            "mouse_move",
            "left_click",
            "left_click_drag",
            "right_click",
            "middle_click",
            "double_click",
            "screenshot",
            "cursor_position",
            "navigate",
            "refresh",
        ]
    ]

    connect_url: Optional[str]

    coordinate: Optional[Iterable[object]]

    text: Optional[str]

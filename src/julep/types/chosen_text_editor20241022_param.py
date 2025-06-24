# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChosenTextEditor20241022Param"]


class ChosenTextEditor20241022Param(TypedDict, total=False):
    command: Required[Literal["str_replace", "insert", "view", "undo_edit"]]

    path: Required[str]

    file_text: Optional[str]

    insert_line: Optional[int]

    new_str: Optional[str]

    old_str: Optional[str]

    view_range: Optional[Iterable[int]]

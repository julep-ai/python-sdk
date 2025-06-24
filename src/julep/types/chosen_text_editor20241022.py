# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChosenTextEditor20241022"]


class ChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None

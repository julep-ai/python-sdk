# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DocCreateParams"]


class DocCreateParams(TypedDict, total=False):
    content: Required[Union[str, SequenceNotStr[str]]]

    title: Required[str]

    connection_pool: object

    embed_instruction: Optional[str]

    metadata: Optional[object]

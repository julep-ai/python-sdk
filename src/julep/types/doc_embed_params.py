# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["DocEmbedParams"]


class DocEmbedParams(TypedDict, total=False):
    text: Required[Union[str, List[str]]]

    embed_instruction: str

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["DocEmbedParams", "SingleEmbedQueryRequest", "MultipleEmbedQueryRequest"]


class SingleEmbedQueryRequest(TypedDict, total=False):
    text: Required[str]

    embed_instruction: str


class MultipleEmbedQueryRequest(TypedDict, total=False):
    text: Required[SequenceNotStr[str]]

    embed_instruction: str


DocEmbedParams: TypeAlias = Union[SingleEmbedQueryRequest, MultipleEmbedQueryRequest]

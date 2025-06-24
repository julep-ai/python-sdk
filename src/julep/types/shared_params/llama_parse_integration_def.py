# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .llama_parse_setup import LlamaParseSetup
from .llama_parse_fetch_arguments import LlamaParseFetchArguments

__all__ = ["LlamaParseIntegrationDef"]


class LlamaParseIntegrationDef(TypedDict, total=False):
    arguments: Optional[LlamaParseFetchArguments]
    """Arguments for LlamaParse integration"""

    method: Optional[str]

    provider: Literal["llama_parse"]

    setup: Optional[LlamaParseSetup]
    """Setup parameters for LlamaParse integration"""

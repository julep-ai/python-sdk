# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .llama_parse_setup import LlamaParseSetup
from .llama_parse_fetch_arguments import LlamaParseFetchArguments

__all__ = ["LlamaParseIntegrationDef"]


class LlamaParseIntegrationDef(BaseModel):
    arguments: Optional[LlamaParseFetchArguments] = None
    """Arguments for LlamaParse integration"""

    method: Optional[str] = None

    provider: Optional[Literal["llama_parse"]] = None

    setup: Optional[LlamaParseSetup] = None
    """Setup parameters for LlamaParse integration"""

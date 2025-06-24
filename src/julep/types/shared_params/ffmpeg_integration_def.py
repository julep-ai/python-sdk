# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .ffmpeg_search_arguments import FfmpegSearchArguments

__all__ = ["FfmpegIntegrationDef"]


class FfmpegIntegrationDef(TypedDict, total=False):
    arguments: Optional[FfmpegSearchArguments]
    """Arguments for Ffmpeg CMD"""

    method: Optional[str]

    provider: Literal["ffmpeg"]

    setup: object

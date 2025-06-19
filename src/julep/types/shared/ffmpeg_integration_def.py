# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .ffmpeg_search_arguments import FfmpegSearchArguments

__all__ = ["FfmpegIntegrationDef"]


class FfmpegIntegrationDef(BaseModel):
    arguments: Optional[FfmpegSearchArguments] = None
    """Arguments for Ffmpeg CMD"""

    method: Optional[str] = None

    provider: Optional[Literal["ffmpeg"]] = None

    setup: Optional[object] = None

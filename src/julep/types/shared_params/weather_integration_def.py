# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .weather_setup import WeatherSetup
from .weather_get_arguments import WeatherGetArguments

__all__ = ["WeatherIntegrationDef"]


class WeatherIntegrationDef(TypedDict, total=False):
    arguments: Optional[WeatherGetArguments]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[WeatherSetup]
    """Integration definition for Weather"""

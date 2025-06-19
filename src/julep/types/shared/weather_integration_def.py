# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .weather_setup import WeatherSetup
from .weather_get_arguments import WeatherGetArguments

__all__ = ["WeatherIntegrationDef"]


class WeatherIntegrationDef(BaseModel):
    arguments: Optional[WeatherGetArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[WeatherSetup] = None
    """Integration definition for Weather"""

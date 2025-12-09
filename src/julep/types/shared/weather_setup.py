# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WeatherSetup"]


class WeatherSetup(BaseModel):
    """Integration definition for Weather"""

    openweathermap_api_key: str

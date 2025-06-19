# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WeatherSetup"]


class WeatherSetup(TypedDict, total=False):
    openweathermap_api_key: Required[str]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SleepFor"]


class SleepFor(BaseModel):
    days: Optional[int] = None

    hours: Optional[int] = None

    minutes: Optional[int] = None

    seconds: Optional[int] = None

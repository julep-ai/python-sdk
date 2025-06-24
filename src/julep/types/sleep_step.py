# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .sleep_for import SleepFor

__all__ = ["SleepStep"]


class SleepStep(BaseModel):
    sleep: SleepFor

    kind: Optional[Literal["sleep"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

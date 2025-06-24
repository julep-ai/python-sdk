# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SetStep"]


class SetStep(BaseModel):
    set: Dict[str, Union[str, object]]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

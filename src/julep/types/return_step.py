# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReturnStep"]


class ReturnStep(BaseModel):
    return_: Dict[str, Union[List[str], Dict[str, str], List[Dict[str, str]], str]] = FieldInfo(alias="return")

    kind: Optional[Literal["return"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

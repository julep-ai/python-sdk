# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["YieldStep"]


class YieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, Union[List[str], Dict[str, str], List[Dict[str, str]], str]], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .foreach_do_output import ForeachDoOutput

__all__ = ["ForeachStepOutput"]


class ForeachStepOutput(BaseModel):
    foreach: ForeachDoOutput

    kind: Optional[Literal["foreach"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

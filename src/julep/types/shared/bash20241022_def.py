# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Bash20241022Def"]


class Bash20241022Def(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None

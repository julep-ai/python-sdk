# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["WaitForInputInfo"]


class WaitForInputInfo(BaseModel):
    info: Dict[str, Union[List[str], Dict[str, str], List[Dict[str, str]], str]]

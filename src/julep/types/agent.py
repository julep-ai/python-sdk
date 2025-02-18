# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Agent"]


class Agent(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    about: Optional[str] = None

    canonical_name: Optional[str] = None

    default_settings: Optional[object] = None

    default_system_template: Optional[str] = None

    instructions: Union[str, List[str], None] = None

    metadata: Optional[object] = None

    model: Optional[str] = None

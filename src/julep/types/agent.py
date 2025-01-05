# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Agent", "DefaultSettings"]


class DefaultSettings(BaseModel):
    frequency_penalty: Optional[float] = None

    length_penalty: Optional[float] = None

    min_p: Optional[float] = None

    presence_penalty: Optional[float] = None

    repetition_penalty: Optional[float] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None


class Agent(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    about: Optional[str] = None

    canonical_name: Optional[str] = None

    default_settings: Optional[DefaultSettings] = None
    """Default settings for the chat session (also used by the agent)"""

    instructions: Union[str, List[str], None] = None

    metadata: Optional[object] = None

    model: Optional[str] = None

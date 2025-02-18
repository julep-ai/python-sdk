# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AgentResetParams"]


class AgentResetParams(TypedDict, total=False):
    name: Required[str]

    about: str

    canonical_name: Optional[str]

    default_settings: Optional[object]

    default_system_template: str

    instructions: Union[str, List[str]]

    metadata: Optional[object]

    model: str

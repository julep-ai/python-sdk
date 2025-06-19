# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DummyIntegrationDef"]


class DummyIntegrationDef(TypedDict, total=False):
    arguments: object

    method: Optional[str]

    provider: Literal["dummy"]

    setup: object

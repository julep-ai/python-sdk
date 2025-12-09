# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailSetup"]


class EmailSetup(TypedDict, total=False):
    """Setup parameters for Email integration"""

    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]

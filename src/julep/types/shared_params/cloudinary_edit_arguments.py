# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["CloudinaryEditArguments"]


class CloudinaryEditArguments(TypedDict, total=False):
    public_id: Required[str]

    transformation: Required[Iterable[object]]

    return_base64: bool

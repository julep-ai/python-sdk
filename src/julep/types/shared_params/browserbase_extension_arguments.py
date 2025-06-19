# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BrowserbaseExtensionArguments"]


class BrowserbaseExtensionArguments(TypedDict, total=False):
    repository_name: Required[Annotated[str, PropertyInfo(alias="repositoryName")]]

    ref: Optional[str]

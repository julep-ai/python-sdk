# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrowserbaseExtensionArguments"]


class BrowserbaseExtensionArguments(BaseModel):
    repository_name: str = FieldInfo(alias="repositoryName")

    ref: Optional[str] = None

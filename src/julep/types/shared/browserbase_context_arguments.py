# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrowserbaseContextArguments"]


class BrowserbaseContextArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")

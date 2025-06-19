# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrowserbaseCreateSessionArguments"]


class BrowserbaseCreateSessionArguments(BaseModel):
    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnstructuredSetup"]


class UnstructuredSetup(BaseModel):
    unstructured_api_key: str

    retry_config: Optional[object] = None

    server: Optional[str] = None

    server_url: Optional[str] = None

    timeout_ms: Optional[int] = None

    url_params: Optional[object] = None

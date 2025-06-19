# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UnstructuredSetup"]


class UnstructuredSetup(TypedDict, total=False):
    unstructured_api_key: Required[str]

    retry_config: Optional[object]

    server: Optional[str]

    server_url: Optional[str]

    timeout_ms: Optional[int]

    url_params: Optional[object]

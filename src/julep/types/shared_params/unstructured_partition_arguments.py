# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["UnstructuredPartitionArguments"]


class UnstructuredPartitionArguments(TypedDict, total=False):
    file: Required[str]

    filename: Optional[str]

    partition_params: Optional[object]

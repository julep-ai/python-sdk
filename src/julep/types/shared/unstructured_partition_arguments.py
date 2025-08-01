# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnstructuredPartitionArguments"]


class UnstructuredPartitionArguments(BaseModel):
    file: str

    filename: Optional[str] = None

    partition_params: Optional[object] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["DocBulkDeleteResponse", "DocBulkDeleteResponseItem"]


class DocBulkDeleteResponseItem(BaseModel):
    id: str

    deleted_at: datetime

    jobs: Optional[List[str]] = None


DocBulkDeleteResponse: TypeAlias = List[DocBulkDeleteResponseItem]

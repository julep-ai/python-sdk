# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .unstructured_setup import UnstructuredSetup
from .unstructured_partition_arguments import UnstructuredPartitionArguments

__all__ = ["UnstructuredIntegrationDef"]


class UnstructuredIntegrationDef(BaseModel):
    arguments: Optional[UnstructuredPartitionArguments] = None
    """Arguments for Unstructured partition integration"""

    method: Optional[str] = None

    provider: Optional[Literal["unstructured"]] = None

    setup: Optional[UnstructuredSetup] = None
    """Setup parameters for Unstructured integration"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .unstructured_setup import UnstructuredSetup
from .unstructured_partition_arguments import UnstructuredPartitionArguments

__all__ = ["UnstructuredIntegrationDef"]


class UnstructuredIntegrationDef(TypedDict, total=False):
    arguments: Optional[UnstructuredPartitionArguments]
    """Arguments for Unstructured partition integration"""

    method: Optional[str]

    provider: Literal["unstructured"]

    setup: Optional[UnstructuredSetup]
    """Setup parameters for Unstructured integration"""

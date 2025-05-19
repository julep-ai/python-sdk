# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DocBulkDeleteParams"]


class DocBulkDeleteParams(TypedDict, total=False):
    delete_all: bool

    metadata_filter: object

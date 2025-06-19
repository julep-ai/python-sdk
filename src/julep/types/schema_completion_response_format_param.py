# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SchemaCompletionResponseFormatParam"]


class SchemaCompletionResponseFormatParam(TypedDict, total=False):
    json_schema: Required[object]

    type: Literal["json_schema"]

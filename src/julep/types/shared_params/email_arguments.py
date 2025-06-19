# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EmailArguments"]

_EmailArgumentsReservedKeywords = TypedDict(
    "_EmailArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class EmailArguments(_EmailArgumentsReservedKeywords, total=False):
    body: Required[str]

    subject: Required[str]

    to: Required[str]

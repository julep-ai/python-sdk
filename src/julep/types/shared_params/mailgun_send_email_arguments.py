# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MailgunSendEmailArguments"]

_MailgunSendEmailArgumentsReservedKeywords = TypedDict(
    "_MailgunSendEmailArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MailgunSendEmailArguments(_MailgunSendEmailArgumentsReservedKeywords, total=False):
    body: Required[str]

    subject: Required[str]

    to: Required[str]

    bcc: Optional[str]

    cc: Optional[str]

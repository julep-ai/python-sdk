# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .mailgun_setup import MailgunSetup
from .mailgun_send_email_arguments import MailgunSendEmailArguments

__all__ = ["MailgunIntegrationDef"]


class MailgunIntegrationDef(TypedDict, total=False):
    arguments: Optional[MailgunSendEmailArguments]
    """Arguments for mailgun.send_email method"""

    method: Optional[Literal["send_email"]]

    provider: Literal["mailgun"]

    setup: Optional[MailgunSetup]
    """Setup parameters for Mailgun integration"""

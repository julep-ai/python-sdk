# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .mailgun_setup import MailgunSetup
from .mailgun_send_email_arguments import MailgunSendEmailArguments

__all__ = ["MailgunIntegrationDef"]


class MailgunIntegrationDef(BaseModel):
    arguments: Optional[MailgunSendEmailArguments] = None
    """Arguments for mailgun.send_email method"""

    method: Optional[Literal["send_email"]] = None

    provider: Optional[Literal["mailgun"]] = None

    setup: Optional[MailgunSetup] = None
    """Setup parameters for Mailgun integration"""

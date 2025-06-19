# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .email_setup import EmailSetup
from .email_arguments import EmailArguments

__all__ = ["EmailIntegrationDef"]


class EmailIntegrationDef(BaseModel):
    arguments: Optional[EmailArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[EmailSetup] = None
    """Setup parameters for Email integration"""

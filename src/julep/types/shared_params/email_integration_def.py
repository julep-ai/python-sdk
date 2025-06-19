# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .email_setup import EmailSetup
from .email_arguments import EmailArguments

__all__ = ["EmailIntegrationDef"]


class EmailIntegrationDef(TypedDict, total=False):
    arguments: Optional[EmailArguments]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[EmailSetup]
    """Setup parameters for Email integration"""

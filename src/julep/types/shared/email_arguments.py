# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailArguments"]


class EmailArguments(BaseModel):
    """Arguments for Email sending"""

    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str

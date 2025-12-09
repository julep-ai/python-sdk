# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EmailSetup"]


class EmailSetup(BaseModel):
    """Setup parameters for Email integration"""

    host: str

    password: str

    port: int

    user: str

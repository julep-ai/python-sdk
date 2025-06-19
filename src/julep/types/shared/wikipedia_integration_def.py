# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .wikipedia_search_arguments import WikipediaSearchArguments

__all__ = ["WikipediaIntegrationDef"]


class WikipediaIntegrationDef(BaseModel):
    arguments: Optional[WikipediaSearchArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None

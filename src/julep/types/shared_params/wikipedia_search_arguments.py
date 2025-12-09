# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WikipediaSearchArguments"]


class WikipediaSearchArguments(TypedDict, total=False):
    """Arguments for Wikipedia Search"""

    query: Required[str]

    load_max_docs: int

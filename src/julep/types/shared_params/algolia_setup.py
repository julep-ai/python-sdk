# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AlgoliaSetup"]


class AlgoliaSetup(TypedDict, total=False):
    algolia_api_key: Required[str]

    algolia_application_id: Required[str]

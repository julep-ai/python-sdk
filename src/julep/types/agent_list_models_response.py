# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AgentListModelsResponse", "Model"]


class Model(BaseModel):
    """Model information returned by the model list endpoint"""

    id: str


class AgentListModelsResponse(BaseModel):
    """Response for the list models endpoint"""

    models: List[Model]

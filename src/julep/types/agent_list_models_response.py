# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AgentListModelsResponse", "Model"]


class Model(BaseModel):
    id: str


class AgentListModelsResponse(BaseModel):
    models: List[Model]

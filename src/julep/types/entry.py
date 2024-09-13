# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "Entry",
    "Content",
    "ContentUnionMember0",
    "ContentUnionMember0Content",
    "ContentUnionMember0ContentModel",
    "ContentUnionMember0ContentModelImageURL",
    "ContentTool",
    "ContentToolFunction",
    "ContentChosenToolCall",
    "ContentChosenToolCallFunction",
    "ContentToolResponse",
    "ContentUnionMember5",
    "ContentUnionMember5UnionMember0",
    "ContentUnionMember5UnionMember0Content",
    "ContentUnionMember5UnionMember0ContentModel",
    "ContentUnionMember5UnionMember0ContentModelImageURL",
    "ContentUnionMember5Tool",
    "ContentUnionMember5ToolFunction",
    "ContentUnionMember5ChosenToolCall",
    "ContentUnionMember5ChosenToolCallFunction",
    "ContentUnionMember5ToolResponse",
]


class ContentUnionMember0Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember0ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ContentUnionMember0ContentModel(BaseModel):
    image_url: ContentUnionMember0ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


ContentUnionMember0: TypeAlias = Union[ContentUnionMember0Content, ContentUnionMember0ContentModel]


class ContentToolFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentTool(BaseModel):
    id: str

    created_at: datetime

    function: ContentToolFunction
    """Function definition"""

    name: str

    updated_at: datetime

    api_call: Optional[object] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    type: Optional[Literal["function", "integration", "system", "api_call"]] = None


class ContentChosenToolCallFunction(BaseModel):
    name: str


class ContentChosenToolCall(BaseModel):
    id: str

    type: Literal["function", "integration", "system", "api_call"]

    api_call: Optional[object] = None

    function: Optional[ContentChosenToolCallFunction] = None

    integration: Optional[object] = None

    system: Optional[object] = None


class ContentToolResponse(BaseModel):
    id: str

    output: object


class ContentUnionMember5UnionMember0Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember5UnionMember0ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ContentUnionMember5UnionMember0ContentModel(BaseModel):
    image_url: ContentUnionMember5UnionMember0ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


ContentUnionMember5UnionMember0: TypeAlias = Union[
    ContentUnionMember5UnionMember0Content, ContentUnionMember5UnionMember0ContentModel
]


class ContentUnionMember5ToolFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentUnionMember5Tool(BaseModel):
    id: str

    created_at: datetime

    function: ContentUnionMember5ToolFunction
    """Function definition"""

    name: str

    updated_at: datetime

    api_call: Optional[object] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    type: Optional[Literal["function", "integration", "system", "api_call"]] = None


class ContentUnionMember5ChosenToolCallFunction(BaseModel):
    name: str


class ContentUnionMember5ChosenToolCall(BaseModel):
    id: str

    type: Literal["function", "integration", "system", "api_call"]

    api_call: Optional[object] = None

    function: Optional[ContentUnionMember5ChosenToolCallFunction] = None

    integration: Optional[object] = None

    system: Optional[object] = None


class ContentUnionMember5ToolResponse(BaseModel):
    id: str

    output: object


ContentUnionMember5: TypeAlias = Union[
    List[ContentUnionMember5UnionMember0],
    ContentUnionMember5Tool,
    ContentUnionMember5ChosenToolCall,
    str,
    ContentUnionMember5ToolResponse,
]

Content: TypeAlias = Union[
    List[ContentUnionMember0], ContentTool, ContentChosenToolCall, str, ContentToolResponse, List[ContentUnionMember5]
]


class Entry(BaseModel):
    id: str

    content: Content
    """The response tool value generated by the model"""

    created_at: datetime

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    source: Literal["api_request", "api_response", "tool_response", "internal", "summarizer", "meta"]

    timestamp: float

    token_count: int

    tokenizer: str

    name: Optional[str] = None

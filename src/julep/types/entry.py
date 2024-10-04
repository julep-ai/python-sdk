# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Entry",
    "Content",
    "ContentUnionMember0",
    "ContentUnionMember0Content",
    "ContentUnionMember0ContentModel",
    "ContentUnionMember0ContentModelImageURL",
    "ContentTool",
    "ContentToolAPICall",
    "ContentToolFunction",
    "ContentToolIntegration",
    "ContentToolSystem",
    "ContentChosenToolCall",
    "ContentChosenToolCallFunction",
    "ContentToolResponse",
    "ContentUnionMember5",
    "ContentUnionMember5UnionMember0",
    "ContentUnionMember5UnionMember0Content",
    "ContentUnionMember5UnionMember0ContentModel",
    "ContentUnionMember5UnionMember0ContentModelImageURL",
    "ContentUnionMember5Tool",
    "ContentUnionMember5ToolAPICall",
    "ContentUnionMember5ToolFunction",
    "ContentUnionMember5ToolIntegration",
    "ContentUnionMember5ToolSystem",
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


class ContentToolAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class ContentToolFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentToolIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class ContentToolSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class ContentTool(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    api_call: Optional[ContentToolAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[ContentToolFunction] = None
    """Function definition"""

    integration: Optional[ContentToolIntegration] = None
    """Integration definition"""

    system: Optional[ContentToolSystem] = None
    """System definition"""


class ContentChosenToolCallFunction(BaseModel):
    name: str


class ContentChosenToolCall(BaseModel):
    id: str

    type: Literal["function", "integration", "system", "api_call"]

    function: Optional[ContentChosenToolCallFunction] = None


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


class ContentUnionMember5ToolAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class ContentUnionMember5ToolFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentUnionMember5ToolIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class ContentUnionMember5ToolSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class ContentUnionMember5Tool(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    api_call: Optional[ContentUnionMember5ToolAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[ContentUnionMember5ToolFunction] = None
    """Function definition"""

    integration: Optional[ContentUnionMember5ToolIntegration] = None
    """Integration definition"""

    system: Optional[ContentUnionMember5ToolSystem] = None
    """System definition"""


class ContentUnionMember5ChosenToolCallFunction(BaseModel):
    name: str


class ContentUnionMember5ChosenToolCall(BaseModel):
    id: str

    type: Literal["function", "integration", "system", "api_call"]

    function: Optional[ContentUnionMember5ChosenToolCallFunction] = None


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

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
    "ContentToolOutput",
    "ContentToolOutputAPICall",
    "ContentToolOutputFunction",
    "ContentToolOutputIntegration",
    "ContentToolOutputIntegrationDummyIntegrationDef",
    "ContentToolOutputIntegrationBraveIntegrationDef",
    "ContentToolOutputIntegrationBraveIntegrationDefArguments",
    "ContentToolOutputIntegrationBraveIntegrationDefSetup",
    "ContentToolOutputIntegrationEmailIntegrationDef",
    "ContentToolOutputIntegrationEmailIntegrationDefArguments",
    "ContentToolOutputIntegrationEmailIntegrationDefSetup",
    "ContentToolOutputIntegrationSpiderIntegrationDef",
    "ContentToolOutputIntegrationSpiderIntegrationDefArguments",
    "ContentToolOutputIntegrationSpiderIntegrationDefSetup",
    "ContentToolOutputIntegrationWikipediaIntegrationDef",
    "ContentToolOutputIntegrationWikipediaIntegrationDefArguments",
    "ContentToolOutputIntegrationWeatherIntegrationDef",
    "ContentToolOutputIntegrationWeatherIntegrationDefArguments",
    "ContentToolOutputIntegrationWeatherIntegrationDefSetup",
    "ContentToolOutputSystem",
    "ContentChosenToolCall",
    "ContentChosenToolCallFunction",
    "ContentToolResponse",
    "ContentUnionMember5",
    "ContentUnionMember5UnionMember0",
    "ContentUnionMember5UnionMember0Content",
    "ContentUnionMember5UnionMember0ContentModel",
    "ContentUnionMember5UnionMember0ContentModelImageURL",
    "ContentUnionMember5ToolOutput",
    "ContentUnionMember5ToolOutputAPICall",
    "ContentUnionMember5ToolOutputFunction",
    "ContentUnionMember5ToolOutputIntegration",
    "ContentUnionMember5ToolOutputIntegrationDummyIntegrationDef",
    "ContentUnionMember5ToolOutputIntegrationBraveIntegrationDef",
    "ContentUnionMember5ToolOutputIntegrationBraveIntegrationDefArguments",
    "ContentUnionMember5ToolOutputIntegrationBraveIntegrationDefSetup",
    "ContentUnionMember5ToolOutputIntegrationEmailIntegrationDef",
    "ContentUnionMember5ToolOutputIntegrationEmailIntegrationDefArguments",
    "ContentUnionMember5ToolOutputIntegrationEmailIntegrationDefSetup",
    "ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDef",
    "ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDefArguments",
    "ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDefSetup",
    "ContentUnionMember5ToolOutputIntegrationWikipediaIntegrationDef",
    "ContentUnionMember5ToolOutputIntegrationWikipediaIntegrationDefArguments",
    "ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDef",
    "ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDefArguments",
    "ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDefSetup",
    "ContentUnionMember5ToolOutputSystem",
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


class ContentToolOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class ContentToolOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentToolOutputIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class ContentToolOutputIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class ContentToolOutputIntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolOutputIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[ContentToolOutputIntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[ContentToolOutputIntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class ContentToolOutputIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class ContentToolOutputIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ContentToolOutputIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[ContentToolOutputIntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[ContentToolOutputIntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class ContentToolOutputIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class ContentToolOutputIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class ContentToolOutputIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[ContentToolOutputIntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[ContentToolOutputIntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class ContentToolOutputIntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class ContentToolOutputIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[ContentToolOutputIntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class ContentToolOutputIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class ContentToolOutputIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class ContentToolOutputIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[ContentToolOutputIntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[ContentToolOutputIntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


ContentToolOutputIntegration: TypeAlias = Union[
    ContentToolOutputIntegrationDummyIntegrationDef,
    ContentToolOutputIntegrationBraveIntegrationDef,
    ContentToolOutputIntegrationEmailIntegrationDef,
    ContentToolOutputIntegrationSpiderIntegrationDef,
    ContentToolOutputIntegrationWikipediaIntegrationDef,
    ContentToolOutputIntegrationWeatherIntegrationDef,
    None,
]


class ContentToolOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class ContentToolOutput(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    api_call: Optional[ContentToolOutputAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[ContentToolOutputFunction] = None
    """Function definition"""

    integration: Optional[ContentToolOutputIntegration] = None
    """Brave integration definition"""

    system: Optional[ContentToolOutputSystem] = None
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


class ContentUnionMember5ToolOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class ContentUnionMember5ToolOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentUnionMember5ToolOutputIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class ContentUnionMember5ToolOutputIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class ContentUnionMember5ToolOutputIntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember5ToolOutputIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember5ToolOutputIntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[ContentUnionMember5ToolOutputIntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class ContentUnionMember5ToolOutputIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class ContentUnionMember5ToolOutputIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ContentUnionMember5ToolOutputIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember5ToolOutputIntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[ContentUnionMember5ToolOutputIntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class ContentUnionMember5ToolOutputIntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class ContentUnionMember5ToolOutputIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember5ToolOutputIntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


ContentUnionMember5ToolOutputIntegration: TypeAlias = Union[
    ContentUnionMember5ToolOutputIntegrationDummyIntegrationDef,
    ContentUnionMember5ToolOutputIntegrationBraveIntegrationDef,
    ContentUnionMember5ToolOutputIntegrationEmailIntegrationDef,
    ContentUnionMember5ToolOutputIntegrationSpiderIntegrationDef,
    ContentUnionMember5ToolOutputIntegrationWikipediaIntegrationDef,
    ContentUnionMember5ToolOutputIntegrationWeatherIntegrationDef,
    None,
]


class ContentUnionMember5ToolOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class ContentUnionMember5ToolOutput(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    api_call: Optional[ContentUnionMember5ToolOutputAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[ContentUnionMember5ToolOutputFunction] = None
    """Function definition"""

    integration: Optional[ContentUnionMember5ToolOutputIntegration] = None
    """Brave integration definition"""

    system: Optional[ContentUnionMember5ToolOutputSystem] = None
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
    ContentUnionMember5ToolOutput,
    ContentUnionMember5ChosenToolCall,
    str,
    ContentUnionMember5ToolResponse,
]

Content: TypeAlias = Union[
    List[ContentUnionMember0],
    ContentToolOutput,
    ContentChosenToolCall,
    str,
    ContentToolResponse,
    List[ContentUnionMember5],
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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.secret_ref import SecretRef
from .shared_params.system_def import SystemDef
from .chosen_bash20241022_param import ChosenBash20241022Param
from .chosen_function_call_param import ChosenFunctionCallParam
from .shared_params.function_def import FunctionDef
from .chosen_computer20241022_param import ChosenComputer20241022Param
from .shared_params.bash20241022_def import Bash20241022Def
from .shared_params.named_tool_choice import NamedToolChoice
from .chosen_text_editor20241022_param import ChosenTextEditor20241022Param
from .shared_params.computer20241022_def import Computer20241022Def
from .shared_params.arxiv_integration_def import ArxivIntegrationDef
from .shared_params.brave_integration_def import BraveIntegrationDef
from .shared_params.dummy_integration_def import DummyIntegrationDef
from .shared_params.email_integration_def import EmailIntegrationDef
from .shared_params.ffmpeg_integration_def import FfmpegIntegrationDef
from .shared_params.spider_integration_def import SpiderIntegrationDef
from .shared_params.algolia_integration_def import AlgoliaIntegrationDef
from .shared_params.mailgun_integration_def import MailgunIntegrationDef
from .shared_params.text_editor20241022_def import TextEditor20241022Def
from .shared_params.weather_integration_def import WeatherIntegrationDef
from .schema_completion_response_format_param import SchemaCompletionResponseFormatParam
from .shared_params.wikipedia_integration_def import WikipediaIntegrationDef
from .simple_completion_response_format_param import SimpleCompletionResponseFormatParam
from .shared_params.llama_parse_integration_def import LlamaParseIntegrationDef
from .shared_params.unstructured_integration_def import UnstructuredIntegrationDef
from .shared_params.remote_browser_integration_def import RemoteBrowserIntegrationDef
from .shared_params.cloudinary_edit_integration_def import CloudinaryEditIntegrationDef
from .shared_params.cloudinary_upload_integration_def import CloudinaryUploadIntegrationDef
from .shared_params.browserbase_context_integration_def import BrowserbaseContextIntegrationDef
from .shared_params.browserbase_extension_integration_def import BrowserbaseExtensionIntegrationDef
from .shared_params.browserbase_get_session_integration_def import BrowserbaseGetSessionIntegrationDef
from .shared_params.browserbase_list_sessions_integration_def import BrowserbaseListSessionsIntegrationDef
from .shared_params.browserbase_create_session_integration_def import BrowserbaseCreateSessionIntegrationDef
from .shared_params.browserbase_complete_session_integration_def import BrowserbaseCompleteSessionIntegrationDef
from .shared_params.browserbase_get_session_live_urls_integration_def import BrowserbaseGetSessionLiveURLsIntegrationDef

__all__ = [
    "SessionRenderParams",
    "Message",
    "MessageContentUnionMember2",
    "MessageContentUnionMember2AgentsAPIAutogenChatContent",
    "MessageContentUnionMember2ContentModel7",
    "MessageContentUnionMember2ContentModel7ImageURL",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInput",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember0",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1Source",
    "MessageToolCall",
    "ResponseFormat",
    "ToolChoice",
    "Tool",
    "ToolAPICall",
    "ToolAPICallParamsSchema",
    "ToolAPICallParamsSchemaProperties",
    "ToolIntegration",
]


class SessionRenderParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    agent: Optional[str]

    frequency_penalty: Optional[float]

    length_penalty: Optional[float]

    logit_bias: Optional[Dict[str, float]]

    max_tokens: Optional[int]

    metadata: Optional[object]

    min_p: Optional[float]

    model: Optional[str]

    presence_penalty: Optional[float]

    recall: bool

    repetition_penalty: Optional[float]

    response_format: Optional[ResponseFormat]

    save: bool

    seed: Optional[int]

    stop: List[str]

    stream: bool

    temperature: Optional[float]

    tool_choice: Optional[ToolChoice]

    tools: Optional[Iterable[Tool]]

    top_p: Optional[float]


class MessageContentUnionMember2AgentsAPIAutogenChatContent(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MessageContentUnionMember2ContentModel7ImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MessageContentUnionMember2ContentModel7(TypedDict, total=False):
    image_url: Required[MessageContentUnionMember2ContentModel7ImageURL]
    """The image URL"""

    type: Literal["image_url"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1Source(TypedDict, total=False):
    data: Required[str]

    media_type: Required[str]

    type: Literal["base64"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1(TypedDict, total=False):
    source: Required[MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1Source]

    type: Literal["image"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInput(TypedDict, total=False):
    content: Required[
        Union[
            Iterable[MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember0],
            Iterable[MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1],
        ]
    ]

    tool_use_id: Required[str]

    type: Literal["tool_result"]


MessageContentUnionMember2: TypeAlias = Union[
    MessageContentUnionMember2AgentsAPIAutogenChatContent,
    MessageContentUnionMember2ContentModel7,
    MessageContentUnionMember2AgentsAPIAutogenChatContentModelInput,
]

MessageToolCall: TypeAlias = Union[
    ChosenFunctionCallParam, ChosenComputer20241022Param, ChosenTextEditor20241022Param, ChosenBash20241022Param
]

_MessageReservedKeywords = TypedDict(
    "_MessageReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class Message(_MessageReservedKeywords, total=False):
    role: Required[Literal["user", "assistant", "system", "tool"]]

    content: Union[str, List[str], Iterable[MessageContentUnionMember2], None]

    name: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[MessageToolCall]]


ResponseFormat: TypeAlias = Union[SimpleCompletionResponseFormatParam, SchemaCompletionResponseFormatParam]

ToolChoice: TypeAlias = Union[Literal["auto", "none"], NamedToolChoice]


class ToolAPICallParamsSchemaProperties(TypedDict, total=False):
    type: Required[str]

    description: Optional[str]

    enum: Optional[List[str]]

    items: object


class ToolAPICallParamsSchema(TypedDict, total=False):
    properties: Required[Dict[str, ToolAPICallParamsSchemaProperties]]

    additional_properties: Annotated[Optional[bool], PropertyInfo(alias="additionalProperties")]

    required: List[str]

    type: str


class ToolAPICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    files: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    include_response_content: bool

    json: Optional[object]

    params: Union[str, object, None]

    params_schema: Optional[ToolAPICallParamsSchema]
    """JSON Schema for API call parameters"""

    schema: Optional[object]

    secrets: Optional[Dict[str, SecretRef]]

    timeout: Optional[int]


ToolIntegration: TypeAlias = Union[
    DummyIntegrationDef,
    BraveIntegrationDef,
    EmailIntegrationDef,
    SpiderIntegrationDef,
    WikipediaIntegrationDef,
    WeatherIntegrationDef,
    MailgunIntegrationDef,
    BrowserbaseContextIntegrationDef,
    BrowserbaseExtensionIntegrationDef,
    BrowserbaseListSessionsIntegrationDef,
    BrowserbaseCreateSessionIntegrationDef,
    BrowserbaseGetSessionIntegrationDef,
    BrowserbaseCompleteSessionIntegrationDef,
    BrowserbaseGetSessionLiveURLsIntegrationDef,
    RemoteBrowserIntegrationDef,
    LlamaParseIntegrationDef,
    FfmpegIntegrationDef,
    CloudinaryUploadIntegrationDef,
    CloudinaryEditIntegrationDef,
    ArxivIntegrationDef,
    UnstructuredIntegrationDef,
    AlgoliaIntegrationDef,
]


class Tool(TypedDict, total=False):
    name: Required[str]

    type: Required[
        Literal[
            "function",
            "integration",
            "system",
            "api_call",
            "computer_20241022",
            "text_editor_20241022",
            "bash_20241022",
        ]
    ]

    api_call: Optional[ToolAPICall]
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def]

    computer_20241022: Optional[Computer20241022Def]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[FunctionDef]
    """Function definition"""

    integration: Optional[ToolIntegration]
    """Brave integration definition"""

    system: Optional[SystemDef]
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def]

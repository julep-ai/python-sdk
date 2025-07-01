# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .secret_ref import SecretRef
from .system_def import SystemDef
from .function_def import FunctionDef
from .bash20241022_def import Bash20241022Def
from .named_tool_choice import NamedToolChoice
from .computer20241022_def import Computer20241022Def
from .arxiv_integration_def import ArxivIntegrationDef
from .brave_integration_def import BraveIntegrationDef
from .dummy_integration_def import DummyIntegrationDef
from .email_integration_def import EmailIntegrationDef
from .ffmpeg_integration_def import FfmpegIntegrationDef
from .spider_integration_def import SpiderIntegrationDef
from .algolia_integration_def import AlgoliaIntegrationDef
from .mailgun_integration_def import MailgunIntegrationDef
from .text_editor20241022_def import TextEditor20241022Def
from .weather_integration_def import WeatherIntegrationDef
from .wikipedia_integration_def import WikipediaIntegrationDef
from ..chosen_bash20241022_param import ChosenBash20241022Param
from ..chosen_function_call_param import ChosenFunctionCallParam
from .llama_parse_integration_def import LlamaParseIntegrationDef
from .unstructured_integration_def import UnstructuredIntegrationDef
from ..chosen_computer20241022_param import ChosenComputer20241022Param
from .remote_browser_integration_def import RemoteBrowserIntegrationDef
from .cloudinary_edit_integration_def import CloudinaryEditIntegrationDef
from ..chosen_text_editor20241022_param import ChosenTextEditor20241022Param
from .cloudinary_upload_integration_def import CloudinaryUploadIntegrationDef
from .browserbase_context_integration_def import BrowserbaseContextIntegrationDef
from .browserbase_extension_integration_def import BrowserbaseExtensionIntegrationDef
from .browserbase_get_session_integration_def import BrowserbaseGetSessionIntegrationDef
from .browserbase_list_sessions_integration_def import BrowserbaseListSessionsIntegrationDef
from .browserbase_create_session_integration_def import BrowserbaseCreateSessionIntegrationDef
from .browserbase_complete_session_integration_def import BrowserbaseCompleteSessionIntegrationDef
from .browserbase_get_session_live_urls_integration_def import BrowserbaseGetSessionLiveURLsIntegrationDef

__all__ = [
    "PromptStepInput",
    "PromptUnionMember0",
    "PromptUnionMember0ContentUnionMember1",
    "PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContent",
    "PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModel",
    "PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModelImageURL",
    "PromptUnionMember0ContentUnionMember1ContentModel1Input",
    "PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember0",
    "PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1",
    "PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1Source",
    "PromptUnionMember0ToolCall",
    "ToolChoice",
    "ToolsUnionMember1",
    "ToolsUnionMember1ToolRef",
    "ToolsUnionMember1ToolRefRef",
    "ToolsUnionMember1ToolRefRefToolRefByID",
    "ToolsUnionMember1ToolRefRefToolRefByName",
    "ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInput",
    "ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICall",
    "ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchema",
    "ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchemaProperties",
    "ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputIntegration",
]


class PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContent(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModelImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModel(TypedDict, total=False):
    image_url: Required[PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModelImageURL]
    """The image URL"""

    type: Literal["image_url"]


class PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1Source(TypedDict, total=False):
    data: Required[str]

    media_type: Required[str]

    type: Literal["base64"]


class PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1(TypedDict, total=False):
    source: Required[PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1Source]

    type: Literal["image"]


class PromptUnionMember0ContentUnionMember1ContentModel1Input(TypedDict, total=False):
    content: Required[
        Union[
            Iterable[PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember0],
            Iterable[PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1],
        ]
    ]

    tool_use_id: Required[str]

    type: Literal["tool_result"]


PromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContent,
    PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModel,
    PromptUnionMember0ContentUnionMember1ContentModel1Input,
]

PromptUnionMember0ToolCall: TypeAlias = Union[
    ChosenFunctionCallParam, ChosenComputer20241022Param, ChosenTextEditor20241022Param, ChosenBash20241022Param
]

_PromptUnionMember0ReservedKeywords = TypedDict(
    "_PromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class PromptUnionMember0(_PromptUnionMember0ReservedKeywords, total=False):
    content: Required[Union[List[str], Iterable[PromptUnionMember0ContentUnionMember1], str, None]]

    role: Required[Literal["user", "assistant", "system", "tool"]]

    name: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[PromptUnionMember0ToolCall]]


ToolChoice: TypeAlias = Union[Literal["auto", "none"], NamedToolChoice]


class ToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class ToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


ToolsUnionMember1ToolRefRef: TypeAlias = Union[
    ToolsUnionMember1ToolRefRefToolRefByID, ToolsUnionMember1ToolRefRefToolRefByName
]


class ToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[ToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchemaProperties(TypedDict, total=False):
    type: Required[str]

    description: Optional[str]

    enum: Optional[List[str]]

    items: object


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchema(TypedDict, total=False):
    properties: Required[
        Dict[str, ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchemaProperties]
    ]

    additional_properties: Annotated[Optional[bool], PropertyInfo(alias="additionalProperties")]

    required: List[str]

    type: str


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICall(TypedDict, total=False):
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

    params_schema: Optional[ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchema]
    """JSON Schema for API call parameters"""

    schema: Optional[object]

    secrets: Optional[Dict[str, SecretRef]]

    timeout: Optional[int]


ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputIntegration: TypeAlias = Union[
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


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInput(TypedDict, total=False):
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

    api_call: Optional[ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def]

    computer_20241022: Optional[Computer20241022Def]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[FunctionDef]
    """Function definition"""

    integration: Optional[ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputIntegration]
    """Brave integration definition"""

    system: Optional[SystemDef]
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def]


ToolsUnionMember1: TypeAlias = Union[
    ToolsUnionMember1ToolRef, ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInput
]


class PromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[PromptUnionMember0], str]]

    auto_run_tools: bool

    disable_cache: bool

    label: Optional[str]

    settings: Optional[object]

    tool_choice: Optional[ToolChoice]

    tools: Union[Literal["all"], Iterable[ToolsUnionMember1]]

    unwrap: bool

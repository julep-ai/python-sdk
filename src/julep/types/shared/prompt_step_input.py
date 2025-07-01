# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .secret_ref import SecretRef
from .system_def import SystemDef
from .function_def import FunctionDef
from .bash20241022_def import Bash20241022Def
from .named_tool_choice import NamedToolChoice
from ..chosen_bash20241022 import ChosenBash20241022
from .computer20241022_def import Computer20241022Def
from ..chosen_function_call import ChosenFunctionCall
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
from ..chosen_computer20241022 import ChosenComputer20241022
from .wikipedia_integration_def import WikipediaIntegrationDef
from ..chosen_text_editor20241022 import ChosenTextEditor20241022
from .llama_parse_integration_def import LlamaParseIntegrationDef
from .unstructured_integration_def import UnstructuredIntegrationDef
from .remote_browser_integration_def import RemoteBrowserIntegrationDef
from .cloudinary_edit_integration_def import CloudinaryEditIntegrationDef
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


class PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContent(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModel(BaseModel):
    image_url: PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


class PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember0(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1Source(BaseModel):
    data: str

    media_type: str

    type: Optional[Literal["base64"]] = None


class PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1(BaseModel):
    source: PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1Source

    type: Optional[Literal["image"]] = None


class PromptUnionMember0ContentUnionMember1ContentModel1Input(BaseModel):
    content: Union[
        List[PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember0],
        List[PromptUnionMember0ContentUnionMember1ContentModel1InputContentUnionMember1],
    ]

    tool_use_id: str

    type: Optional[Literal["tool_result"]] = None


PromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContent,
    PromptUnionMember0ContentUnionMember1AgentsAPIAutogenTasksContentModel,
    PromptUnionMember0ContentUnionMember1ContentModel1Input,
]

PromptUnionMember0ToolCall: TypeAlias = Union[
    ChosenFunctionCall, ChosenComputer20241022, ChosenTextEditor20241022, ChosenBash20241022
]


class PromptUnionMember0(BaseModel):
    content: Union[List[str], List[PromptUnionMember0ContentUnionMember1], str, None] = None

    role: Literal["user", "assistant", "system", "tool"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[PromptUnionMember0ToolCall]] = None


ToolChoice: TypeAlias = Union[Literal["auto", "none"], NamedToolChoice, None]


class ToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class ToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


ToolsUnionMember1ToolRefRef: TypeAlias = Union[
    ToolsUnionMember1ToolRefRefToolRefByID, ToolsUnionMember1ToolRefRefToolRefByName
]


class ToolsUnionMember1ToolRef(BaseModel):
    ref: ToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchemaProperties(BaseModel):
    type: str

    description: Optional[str] = None

    enum: Optional[List[str]] = None

    items: Optional[object] = None


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchema(BaseModel):
    properties: Dict[str, ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchemaProperties]

    additional_properties: Optional[bool] = FieldInfo(alias="additionalProperties", default=None)

    required: Optional[List[str]] = None

    type: Optional[str] = None


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    files: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    include_response_content: Optional[bool] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    params_schema: Optional[ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICallParamsSchema] = None
    """JSON Schema for API call parameters"""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    secrets: Optional[Dict[str, SecretRef]] = None

    timeout: Optional[int] = None


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
    None,
]


class ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInput(BaseModel):
    name: str

    type: Literal[
        "function", "integration", "system", "api_call", "computer_20241022", "text_editor_20241022", "bash_20241022"
    ]

    api_call: Optional[ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputAPICall] = None
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def] = None

    computer_20241022: Optional[Computer20241022Def] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[FunctionDef] = None
    """Function definition"""

    integration: Optional[ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInputIntegration] = None
    """Brave integration definition"""

    system: Optional[SystemDef] = None
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def] = None


ToolsUnionMember1: TypeAlias = Union[
    ToolsUnionMember1ToolRef, ToolsUnionMember1AgentsAPIAutogenToolsCreateToolRequestInput
]


class PromptStepInput(BaseModel):
    prompt: Union[List[PromptUnionMember0], str]

    auto_run_tools: Optional[bool] = None

    disable_cache: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

    settings: Optional[object] = None

    tool_choice: Optional[ToolChoice] = None

    tools: Union[Literal["all"], List[ToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None

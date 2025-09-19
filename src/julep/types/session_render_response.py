# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.secret_ref import SecretRef
from .shared.system_def import SystemDef
from .chosen_bash20241022 import ChosenBash20241022
from .shared.function_def import FunctionDef
from .chosen_function_call import ChosenFunctionCall
from .shared.doc_reference import DocReference
from .chosen_computer20241022 import ChosenComputer20241022
from .shared.bash20241022_def import Bash20241022Def
from .shared.named_tool_choice import NamedToolChoice
from .chosen_text_editor20241022 import ChosenTextEditor20241022
from .shared.computer20241022_def import Computer20241022Def
from .shared.arxiv_integration_def import ArxivIntegrationDef
from .shared.brave_integration_def import BraveIntegrationDef
from .shared.dummy_integration_def import DummyIntegrationDef
from .shared.email_integration_def import EmailIntegrationDef
from .shared.ffmpeg_integration_def import FfmpegIntegrationDef
from .shared.spider_integration_def import SpiderIntegrationDef
from .shared.algolia_integration_def import AlgoliaIntegrationDef
from .shared.mailgun_integration_def import MailgunIntegrationDef
from .shared.text_editor20241022_def import TextEditor20241022Def
from .shared.weather_integration_def import WeatherIntegrationDef
from .shared.wikipedia_integration_def import WikipediaIntegrationDef
from .shared.llama_parse_integration_def import LlamaParseIntegrationDef
from .shared.unstructured_integration_def import UnstructuredIntegrationDef
from .shared.remote_browser_integration_def import RemoteBrowserIntegrationDef
from .shared.cloudinary_edit_integration_def import CloudinaryEditIntegrationDef
from .shared.cloudinary_upload_integration_def import CloudinaryUploadIntegrationDef
from .shared.browserbase_context_integration_def import BrowserbaseContextIntegrationDef
from .shared.browserbase_extension_integration_def import BrowserbaseExtensionIntegrationDef
from .shared.browserbase_get_session_integration_def import BrowserbaseGetSessionIntegrationDef
from .shared.browserbase_list_sessions_integration_def import BrowserbaseListSessionsIntegrationDef
from .shared.browserbase_create_session_integration_def import BrowserbaseCreateSessionIntegrationDef
from .shared.browserbase_complete_session_integration_def import BrowserbaseCompleteSessionIntegrationDef
from .shared.browserbase_get_session_live_urls_integration_def import BrowserbaseGetSessionLiveURLsIntegrationDef

__all__ = [
    "SessionRenderResponse",
    "Message",
    "MessageContentUnionMember2",
    "MessageContentUnionMember2ContentOutput",
    "MessageContentUnionMember2ContentModel7",
    "MessageContentUnionMember2ContentModel7ImageURL",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutput",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember0",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1Source",
    "MessageToolCall",
    "ToolChoice",
    "Tool",
    "ToolAPICall",
    "ToolAPICallParamsSchema",
    "ToolAPICallParamsSchemaProperties",
    "ToolIntegration",
    "ToolIntegrationMcpIntegrationDef",
    "ToolIntegrationMcpIntegrationDefArguments",
    "ToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments",
    "ToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments",
    "ToolIntegrationMcpIntegrationDefSetup",
    "ToolIntegrationGoogleSheetsIntegrationDefOutput",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArguments",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData",
    "ToolIntegrationGoogleSheetsIntegrationDefOutputSetup",
]


class MessageContentUnionMember2ContentOutput(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MessageContentUnionMember2ContentModel7ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MessageContentUnionMember2ContentModel7(BaseModel):
    image_url: MessageContentUnionMember2ContentModel7ImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember0(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1Source(BaseModel):
    data: str

    media_type: str

    type: Optional[Literal["base64"]] = None


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1(BaseModel):
    source: MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1Source

    type: Optional[Literal["image"]] = None


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutput(BaseModel):
    content: Union[
        List[MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember0],
        List[MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1],
    ]

    tool_use_id: str

    type: Optional[Literal["tool_result"]] = None


MessageContentUnionMember2: TypeAlias = Union[
    MessageContentUnionMember2ContentOutput,
    MessageContentUnionMember2ContentModel7,
    MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutput,
]

MessageToolCall: TypeAlias = Union[
    ChosenFunctionCall, ChosenComputer20241022, ChosenTextEditor20241022, ChosenBash20241022
]


class Message(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]

    content: Union[str, List[str], List[MessageContentUnionMember2], None] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[MessageToolCall]] = None


ToolChoice: TypeAlias = Union[Literal["auto", "none"], NamedToolChoice, None]


class ToolAPICallParamsSchemaProperties(BaseModel):
    type: str

    description: Optional[str] = None

    enum: Optional[List[str]] = None

    items: Optional[object] = None


class ToolAPICallParamsSchema(BaseModel):
    properties: Dict[str, ToolAPICallParamsSchemaProperties]

    additional_properties: Optional[bool] = FieldInfo(alias="additionalProperties", default=None)

    required: Optional[List[str]] = None

    type: Optional[str] = None


class ToolAPICall(BaseModel):
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

    params_schema: Optional[ToolAPICallParamsSchema] = None
    """JSON Schema for API call parameters"""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    secrets: Optional[Dict[str, SecretRef]] = None

    timeout: Optional[int] = None


class ToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments(BaseModel):
    tool_name: str

    arguments: Optional[object] = None

    timeout_seconds: Optional[int] = None


class ToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments(BaseModel):
    dummy: Optional[str] = None


ToolIntegrationMcpIntegrationDefArguments: TypeAlias = Union[
    ToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments,
    ToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments,
    None,
]


class ToolIntegrationMcpIntegrationDefSetup(BaseModel):
    transport: Literal["sse", "http"]

    args: Optional[List[str]] = None

    command: Optional[str] = None

    cwd: Optional[str] = None

    env: Optional[Dict[str, str]] = None

    http_headers: Optional[Dict[str, str]] = None

    http_url: Optional[str] = None


class ToolIntegrationMcpIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationMcpIntegrationDefArguments] = None
    """Arguments to call a named tool on the MCP server"""

    method: Optional[str] = None

    provider: Optional[Literal["mcp"]] = None

    setup: Optional[ToolIntegrationMcpIntegrationDefSetup] = None
    """Setup parameters for MCP integration"""


class ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments(BaseModel):
    range: str

    spreadsheet_id: str

    date_time_render_option: Optional[Literal["SERIAL_NUMBER", "FORMATTED_STRING"]] = None

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None

    value_render_option: Optional[Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]] = None


class ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments(BaseModel):
    range: str

    spreadsheet_id: str

    values: List[List[object]]

    include_values_in_response: Optional[bool] = None

    insert_data_option: Optional[Literal["OVERWRITE", "INSERT_ROWS"]] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


class ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments(BaseModel):
    range: str

    spreadsheet_id: str

    values: List[List[object]]

    include_values_in_response: Optional[bool] = None

    insert_data_option: Optional[Literal["OVERWRITE", "INSERT_ROWS"]] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


class ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments(BaseModel):
    range: str

    spreadsheet_id: str


class ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments(BaseModel):
    ranges: List[str]

    spreadsheet_id: str

    date_time_render_option: Optional[Literal["SERIAL_NUMBER", "FORMATTED_STRING"]] = None

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None

    value_render_option: Optional[Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]] = None


class ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData(BaseModel):
    range: str

    values: List[List[object]]

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None


class ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments(BaseModel):
    data: List[ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData]

    spreadsheet_id: str

    include_values_in_response: Optional[bool] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


ToolIntegrationGoogleSheetsIntegrationDefOutputArguments: TypeAlias = Union[
    ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments,
    ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments,
    ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments,
    ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments,
    ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments,
    ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments,
    None,
]


class ToolIntegrationGoogleSheetsIntegrationDefOutputSetup(BaseModel):
    use_julep_service: bool

    default_retry_count: Optional[int] = None

    service_account_json: Optional[str] = None


class ToolIntegrationGoogleSheetsIntegrationDefOutput(BaseModel):
    arguments: Optional[ToolIntegrationGoogleSheetsIntegrationDefOutputArguments] = None
    """Arguments for reading values from a spreadsheet"""

    method: Optional[
        Literal["read_values", "write_values", "append_values", "clear_values", "batch_read", "batch_write"]
    ] = None

    provider: Optional[Literal["google_sheets"]] = None

    setup: Optional[ToolIntegrationGoogleSheetsIntegrationDefOutputSetup] = None
    """Setup parameters for Google Sheets integration"""


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
    ToolIntegrationMcpIntegrationDef,
    ToolIntegrationGoogleSheetsIntegrationDefOutput,
    None,
]


class Tool(BaseModel):
    name: str

    type: Literal[
        "function", "integration", "system", "api_call", "computer_20241022", "text_editor_20241022", "bash_20241022"
    ]

    api_call: Optional[ToolAPICall] = None
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def] = None

    computer_20241022: Optional[Computer20241022Def] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[FunctionDef] = None
    """Function definition"""

    integration: Optional[ToolIntegration] = None
    """Brave integration definition"""

    system: Optional[SystemDef] = None
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def] = None


class SessionRenderResponse(BaseModel):
    messages: List[Message]

    docs: Optional[List[DocReference]] = None

    tool_choice: Optional[ToolChoice] = None

    tools: Optional[List[Tool]] = None

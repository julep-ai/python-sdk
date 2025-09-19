# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.secret_ref import SecretRef
from .shared.system_def import SystemDef
from .chosen_bash20241022 import ChosenBash20241022
from .shared.function_def import FunctionDef
from .chosen_function_call import ChosenFunctionCall
from .chosen_computer20241022 import ChosenComputer20241022
from .shared.bash20241022_def import Bash20241022Def
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
    "Entry",
    "Content",
    "ContentUnionMember0",
    "ContentUnionMember0ContentOutput",
    "ContentUnionMember0AgentsAPIAutogenEntriesContentModel3",
    "ContentUnionMember0AgentsAPIAutogenEntriesContentModel3ImageURL",
    "ContentUnionMember0AgentsAPIAutogenEntriesContentModel",
    "ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember0",
    "ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember1",
    "ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember1Source",
    "ContentTool",
    "ContentToolAPICall",
    "ContentToolAPICallParamsSchema",
    "ContentToolAPICallParamsSchemaProperties",
    "ContentToolIntegration",
    "ContentToolIntegrationMcpIntegrationDef",
    "ContentToolIntegrationMcpIntegrationDefArguments",
    "ContentToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments",
    "ContentToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments",
    "ContentToolIntegrationMcpIntegrationDefSetup",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutput",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArguments",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData",
    "ContentToolIntegrationGoogleSheetsIntegrationDefOutputSetup",
    "ContentToolResponse",
    "ContentUnionMember8",
    "ContentUnionMember8UnionMember0",
    "ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel1",
    "ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel3",
    "ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel3ImageURL",
    "ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2",
    "ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember0",
    "ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember1",
    "ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember1Source",
    "ContentUnionMember8Tool",
    "ContentUnionMember8ToolAPICall",
    "ContentUnionMember8ToolAPICallParamsSchema",
    "ContentUnionMember8ToolAPICallParamsSchemaProperties",
    "ContentUnionMember8ToolIntegration",
    "ContentUnionMember8ToolIntegrationMcpIntegrationDef",
    "ContentUnionMember8ToolIntegrationMcpIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments",
    "ContentUnionMember8ToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments",
    "ContentUnionMember8ToolIntegrationMcpIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutput",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArguments",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData",
    "ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputSetup",
    "ContentUnionMember8ToolResponse",
    "ToolCall",
]


class ContentUnionMember0ContentOutput(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember0AgentsAPIAutogenEntriesContentModel3ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ContentUnionMember0AgentsAPIAutogenEntriesContentModel3(BaseModel):
    image_url: ContentUnionMember0AgentsAPIAutogenEntriesContentModel3ImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


class ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember0(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember1Source(BaseModel):
    data: str

    media_type: str

    type: Optional[Literal["base64"]] = None


class ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember1(BaseModel):
    source: ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember1Source

    type: Optional[Literal["image"]] = None


class ContentUnionMember0AgentsAPIAutogenEntriesContentModel(BaseModel):
    content: Union[
        List[ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember0],
        List[ContentUnionMember0AgentsAPIAutogenEntriesContentModelContentUnionMember1],
    ]

    tool_use_id: str

    type: Optional[Literal["tool_result"]] = None


ContentUnionMember0: TypeAlias = Union[
    ContentUnionMember0ContentOutput,
    ContentUnionMember0AgentsAPIAutogenEntriesContentModel3,
    ContentUnionMember0AgentsAPIAutogenEntriesContentModel,
]


class ContentToolAPICallParamsSchemaProperties(BaseModel):
    type: str

    description: Optional[str] = None

    enum: Optional[List[str]] = None

    items: Optional[object] = None


class ContentToolAPICallParamsSchema(BaseModel):
    properties: Dict[str, ContentToolAPICallParamsSchemaProperties]

    additional_properties: Optional[bool] = FieldInfo(alias="additionalProperties", default=None)

    required: Optional[List[str]] = None

    type: Optional[str] = None


class ContentToolAPICall(BaseModel):
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

    params_schema: Optional[ContentToolAPICallParamsSchema] = None
    """JSON Schema for API call parameters"""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    secrets: Optional[Dict[str, SecretRef]] = None

    timeout: Optional[int] = None


class ContentToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments(BaseModel):
    tool_name: str

    arguments: Optional[object] = None

    timeout_seconds: Optional[int] = None


class ContentToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments(BaseModel):
    dummy: Optional[str] = None


ContentToolIntegrationMcpIntegrationDefArguments: TypeAlias = Union[
    ContentToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments,
    ContentToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments,
    None,
]


class ContentToolIntegrationMcpIntegrationDefSetup(BaseModel):
    transport: Literal["sse", "http"]

    args: Optional[List[str]] = None

    command: Optional[str] = None

    cwd: Optional[str] = None

    env: Optional[Dict[str, str]] = None

    http_headers: Optional[Dict[str, str]] = None

    http_url: Optional[str] = None


class ContentToolIntegrationMcpIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationMcpIntegrationDefArguments] = None
    """Arguments to call a named tool on the MCP server"""

    method: Optional[str] = None

    provider: Optional[Literal["mcp"]] = None

    setup: Optional[ContentToolIntegrationMcpIntegrationDefSetup] = None
    """Setup parameters for MCP integration"""


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments(BaseModel):
    range: str

    spreadsheet_id: str

    date_time_render_option: Optional[Literal["SERIAL_NUMBER", "FORMATTED_STRING"]] = None

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None

    value_render_option: Optional[Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]] = None


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments(BaseModel):
    range: str

    spreadsheet_id: str

    values: List[List[object]]

    include_values_in_response: Optional[bool] = None

    insert_data_option: Optional[Literal["OVERWRITE", "INSERT_ROWS"]] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments(BaseModel):
    range: str

    spreadsheet_id: str

    values: List[List[object]]

    include_values_in_response: Optional[bool] = None

    insert_data_option: Optional[Literal["OVERWRITE", "INSERT_ROWS"]] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments(BaseModel):
    range: str

    spreadsheet_id: str


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments(BaseModel):
    ranges: List[str]

    spreadsheet_id: str

    date_time_render_option: Optional[Literal["SERIAL_NUMBER", "FORMATTED_STRING"]] = None

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None

    value_render_option: Optional[Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]] = None


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData(BaseModel):
    range: str

    values: List[List[object]]

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments(BaseModel):
    data: List[ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData]

    spreadsheet_id: str

    include_values_in_response: Optional[bool] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


ContentToolIntegrationGoogleSheetsIntegrationDefOutputArguments: TypeAlias = Union[
    ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments,
    ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments,
    ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments,
    ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments,
    ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments,
    ContentToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments,
    None,
]


class ContentToolIntegrationGoogleSheetsIntegrationDefOutputSetup(BaseModel):
    use_julep_service: bool

    default_retry_count: Optional[int] = None

    service_account_json: Optional[str] = None


class ContentToolIntegrationGoogleSheetsIntegrationDefOutput(BaseModel):
    arguments: Optional[ContentToolIntegrationGoogleSheetsIntegrationDefOutputArguments] = None
    """Arguments for reading values from a spreadsheet"""

    method: Optional[
        Literal["read_values", "write_values", "append_values", "clear_values", "batch_read", "batch_write"]
    ] = None

    provider: Optional[Literal["google_sheets"]] = None

    setup: Optional[ContentToolIntegrationGoogleSheetsIntegrationDefOutputSetup] = None
    """Setup parameters for Google Sheets integration"""


ContentToolIntegration: TypeAlias = Union[
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
    ContentToolIntegrationMcpIntegrationDef,
    ContentToolIntegrationGoogleSheetsIntegrationDefOutput,
    None,
]


class ContentTool(BaseModel):
    id: str

    created_at: datetime

    name: str

    type: Literal[
        "function", "integration", "system", "api_call", "computer_20241022", "text_editor_20241022", "bash_20241022"
    ]

    updated_at: datetime

    api_call: Optional[ContentToolAPICall] = None
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def] = None

    computer_20241022: Optional[Computer20241022Def] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[FunctionDef] = None
    """Function definition"""

    integration: Optional[ContentToolIntegration] = None
    """Brave integration definition"""

    system: Optional[SystemDef] = None
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def] = None


class ContentToolResponse(BaseModel):
    id: str

    output: object


class ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel1(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel3ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel3(BaseModel):
    image_url: ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel3ImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


class ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember0(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember1Source(BaseModel):
    data: str

    media_type: str

    type: Optional[Literal["base64"]] = None


class ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember1(BaseModel):
    source: ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember1Source

    type: Optional[Literal["image"]] = None


class ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2(BaseModel):
    content: Union[
        List[ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember0],
        List[ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2ContentUnionMember1],
    ]

    tool_use_id: str

    type: Optional[Literal["tool_result"]] = None


ContentUnionMember8UnionMember0: TypeAlias = Union[
    ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel1,
    ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel3,
    ContentUnionMember8UnionMember0AgentsAPIAutogenEntriesContentModel2,
]


class ContentUnionMember8ToolAPICallParamsSchemaProperties(BaseModel):
    type: str

    description: Optional[str] = None

    enum: Optional[List[str]] = None

    items: Optional[object] = None


class ContentUnionMember8ToolAPICallParamsSchema(BaseModel):
    properties: Dict[str, ContentUnionMember8ToolAPICallParamsSchemaProperties]

    additional_properties: Optional[bool] = FieldInfo(alias="additionalProperties", default=None)

    required: Optional[List[str]] = None

    type: Optional[str] = None


class ContentUnionMember8ToolAPICall(BaseModel):
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

    params_schema: Optional[ContentUnionMember8ToolAPICallParamsSchema] = None
    """JSON Schema for API call parameters"""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    secrets: Optional[Dict[str, SecretRef]] = None

    timeout: Optional[int] = None


class ContentUnionMember8ToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments(BaseModel):
    tool_name: str

    arguments: Optional[object] = None

    timeout_seconds: Optional[int] = None


class ContentUnionMember8ToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments(BaseModel):
    dummy: Optional[str] = None


ContentUnionMember8ToolIntegrationMcpIntegrationDefArguments: TypeAlias = Union[
    ContentUnionMember8ToolIntegrationMcpIntegrationDefArgumentsMcpCallToolArguments,
    ContentUnionMember8ToolIntegrationMcpIntegrationDefArgumentsMcpListToolsArguments,
    None,
]


class ContentUnionMember8ToolIntegrationMcpIntegrationDefSetup(BaseModel):
    transport: Literal["sse", "http"]

    args: Optional[List[str]] = None

    command: Optional[str] = None

    cwd: Optional[str] = None

    env: Optional[Dict[str, str]] = None

    http_headers: Optional[Dict[str, str]] = None

    http_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationMcpIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationMcpIntegrationDefArguments] = None
    """Arguments to call a named tool on the MCP server"""

    method: Optional[str] = None

    provider: Optional[Literal["mcp"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationMcpIntegrationDefSetup] = None
    """Setup parameters for MCP integration"""


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments(BaseModel):
    range: str

    spreadsheet_id: str

    date_time_render_option: Optional[Literal["SERIAL_NUMBER", "FORMATTED_STRING"]] = None

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None

    value_render_option: Optional[Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]] = None


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments(BaseModel):
    range: str

    spreadsheet_id: str

    values: List[List[object]]

    include_values_in_response: Optional[bool] = None

    insert_data_option: Optional[Literal["OVERWRITE", "INSERT_ROWS"]] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments(BaseModel):
    range: str

    spreadsheet_id: str

    values: List[List[object]]

    include_values_in_response: Optional[bool] = None

    insert_data_option: Optional[Literal["OVERWRITE", "INSERT_ROWS"]] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments(BaseModel):
    range: str

    spreadsheet_id: str


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments(
    BaseModel
):
    ranges: List[str]

    spreadsheet_id: str

    date_time_render_option: Optional[Literal["SERIAL_NUMBER", "FORMATTED_STRING"]] = None

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None

    value_render_option: Optional[Literal["FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"]] = None


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData(
    BaseModel
):
    range: str

    values: List[List[object]]

    major_dimension: Optional[Literal["ROWS", "COLUMNS"]] = None


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments(
    BaseModel
):
    data: List[
        ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArgumentsData
    ]

    spreadsheet_id: str

    include_values_in_response: Optional[bool] = None

    value_input_option: Optional[Literal["RAW", "USER_ENTERED"]] = None


ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArguments: TypeAlias = Union[
    ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsReadArguments,
    ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsWriteArguments,
    ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsAppendArguments,
    ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsClearArguments,
    ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchReadArguments,
    ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArgumentsGoogleSheetsBatchWriteArguments,
    None,
]


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputSetup(BaseModel):
    use_julep_service: bool

    default_retry_count: Optional[int] = None

    service_account_json: Optional[str] = None


class ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutput(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputArguments] = None
    """Arguments for reading values from a spreadsheet"""

    method: Optional[
        Literal["read_values", "write_values", "append_values", "clear_values", "batch_read", "batch_write"]
    ] = None

    provider: Optional[Literal["google_sheets"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutputSetup] = None
    """Setup parameters for Google Sheets integration"""


ContentUnionMember8ToolIntegration: TypeAlias = Union[
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
    ContentUnionMember8ToolIntegrationMcpIntegrationDef,
    ContentUnionMember8ToolIntegrationGoogleSheetsIntegrationDefOutput,
    None,
]


class ContentUnionMember8Tool(BaseModel):
    id: str

    created_at: datetime

    name: str

    type: Literal[
        "function", "integration", "system", "api_call", "computer_20241022", "text_editor_20241022", "bash_20241022"
    ]

    updated_at: datetime

    api_call: Optional[ContentUnionMember8ToolAPICall] = None
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def] = None

    computer_20241022: Optional[Computer20241022Def] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[FunctionDef] = None
    """Function definition"""

    integration: Optional[ContentUnionMember8ToolIntegration] = None
    """Brave integration definition"""

    system: Optional[SystemDef] = None
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def] = None


class ContentUnionMember8ToolResponse(BaseModel):
    id: str

    output: object


ContentUnionMember8: TypeAlias = Union[
    List[ContentUnionMember8UnionMember0],
    ContentUnionMember8Tool,
    ChosenFunctionCall,
    ChosenComputer20241022,
    ChosenTextEditor20241022,
    ChosenBash20241022,
    str,
    ContentUnionMember8ToolResponse,
]

Content: TypeAlias = Union[
    List[ContentUnionMember0],
    ContentTool,
    ChosenFunctionCall,
    ChosenComputer20241022,
    ChosenTextEditor20241022,
    ChosenBash20241022,
    str,
    ContentToolResponse,
    List[ContentUnionMember8],
]

ToolCall: TypeAlias = Union[ChosenFunctionCall, ChosenComputer20241022, ChosenTextEditor20241022, ChosenBash20241022]


class Entry(BaseModel):
    id: str

    content: Content

    created_at: datetime

    role: Literal["user", "assistant", "system", "tool"]

    source: Literal["api_request", "api_response", "tool_request", "tool_response", "internal", "summarizer", "meta"]

    timestamp: datetime

    token_count: int

    tokenizer: str

    model: Optional[str] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[ToolCall]] = None

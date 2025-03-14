# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .snippet import Snippet
from .._models import BaseModel

__all__ = [
    "SessionRenderResponse",
    "Message",
    "MessageContentUnionMember2",
    "MessageContentUnionMember2Content",
    "MessageContentUnionMember2ContentModel7",
    "MessageContentUnionMember2ContentModel7ImageURL",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutput",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember0",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutputContentUnionMember1Source",
    "MessageToolCall",
    "MessageToolCallChosenFunctionCall",
    "MessageToolCallChosenFunctionCallFunction",
    "MessageToolCallChosenFunctionCallBash20241022",
    "MessageToolCallChosenFunctionCallComputer20241022",
    "MessageToolCallChosenFunctionCallTextEditor20241022",
    "MessageToolCallChosenComputer20241022",
    "MessageToolCallChosenTextEditor20241022",
    "MessageToolCallChosenBash20241022",
    "Doc",
    "DocOwner",
    "ToolChoice",
    "ToolChoiceNamedToolChoice",
    "ToolChoiceNamedToolChoiceFunction",
    "Tool",
    "ToolAPICall",
    "ToolBash20241022",
    "ToolComputer20241022",
    "ToolFunction",
    "ToolIntegration",
    "ToolIntegrationDummyIntegrationDef",
    "ToolIntegrationBraveIntegrationDef",
    "ToolIntegrationBraveIntegrationDefArguments",
    "ToolIntegrationBraveIntegrationDefSetup",
    "ToolIntegrationEmailIntegrationDef",
    "ToolIntegrationEmailIntegrationDefArguments",
    "ToolIntegrationEmailIntegrationDefSetup",
    "ToolIntegrationSpiderIntegrationDef",
    "ToolIntegrationSpiderIntegrationDefArguments",
    "ToolIntegrationSpiderIntegrationDefSetup",
    "ToolIntegrationWikipediaIntegrationDef",
    "ToolIntegrationWikipediaIntegrationDefArguments",
    "ToolIntegrationWeatherIntegrationDef",
    "ToolIntegrationWeatherIntegrationDefArguments",
    "ToolIntegrationWeatherIntegrationDefSetup",
    "ToolIntegrationBrowserbaseContextIntegrationDef",
    "ToolIntegrationBrowserbaseContextIntegrationDefArguments",
    "ToolIntegrationBrowserbaseContextIntegrationDefSetup",
    "ToolIntegrationBrowserbaseExtensionIntegrationDef",
    "ToolIntegrationBrowserbaseExtensionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseExtensionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseListSessionsIntegrationDef",
    "ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "ToolIntegrationBrowserbaseCreateSessionIntegrationDef",
    "ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseGetSessionIntegrationDef",
    "ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseCompleteSessionIntegrationDef",
    "ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "ToolIntegrationRemoteBrowserIntegrationDef",
    "ToolIntegrationRemoteBrowserIntegrationDefSetup",
    "ToolIntegrationRemoteBrowserIntegrationDefArguments",
    "ToolIntegrationLlamaParseIntegrationDef",
    "ToolIntegrationLlamaParseIntegrationDefArguments",
    "ToolIntegrationLlamaParseIntegrationDefSetup",
    "ToolIntegrationFfmpegIntegrationDef",
    "ToolIntegrationFfmpegIntegrationDefArguments",
    "ToolIntegrationCloudinaryUploadIntegrationDef",
    "ToolIntegrationCloudinaryUploadIntegrationDefArguments",
    "ToolIntegrationCloudinaryUploadIntegrationDefSetup",
    "ToolIntegrationCloudinaryEditIntegrationDef",
    "ToolIntegrationCloudinaryEditIntegrationDefArguments",
    "ToolIntegrationCloudinaryEditIntegrationDefSetup",
    "ToolIntegrationArxivIntegrationDef",
    "ToolIntegrationArxivIntegrationDefArguments",
    "ToolIntegrationUnstructuredIntegrationDef",
    "ToolIntegrationUnstructuredIntegrationDefArguments",
    "ToolIntegrationUnstructuredIntegrationDefSetup",
    "ToolIntegrationAlgoliaIntegrationDef",
    "ToolIntegrationAlgoliaIntegrationDefArguments",
    "ToolIntegrationAlgoliaIntegrationDefSetup",
    "ToolSystem",
    "ToolTextEditor20241022",
]


class MessageContentUnionMember2Content(BaseModel):
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
    MessageContentUnionMember2Content,
    MessageContentUnionMember2ContentModel7,
    MessageContentUnionMember2AgentsAPIAutogenChatContentModelOutput,
]


class MessageToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class MessageToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class MessageToolCallChosenFunctionCallComputer20241022(BaseModel):
    action: Literal[
        "key",
        "type",
        "cursor_position",
        "mouse_move",
        "left_click",
        "right_click",
        "middle_click",
        "double_click",
        "screenshot",
    ]

    coordinate: Optional[List[int]] = None

    text: Optional[str] = None


class MessageToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class MessageToolCallChosenFunctionCall(BaseModel):
    function: MessageToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[MessageToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[MessageToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[MessageToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class MessageToolCallChosenComputer20241022(BaseModel):
    action: Literal[
        "key",
        "type",
        "cursor_position",
        "mouse_move",
        "left_click",
        "right_click",
        "middle_click",
        "double_click",
        "screenshot",
    ]

    coordinate: Optional[List[int]] = None

    text: Optional[str] = None


class MessageToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class MessageToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


MessageToolCall: TypeAlias = Union[
    MessageToolCallChosenFunctionCall,
    MessageToolCallChosenComputer20241022,
    MessageToolCallChosenTextEditor20241022,
    MessageToolCallChosenBash20241022,
]


class Message(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]

    content: Union[str, List[str], List[MessageContentUnionMember2], None] = None

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[MessageToolCall]] = None


class DocOwner(BaseModel):
    id: str

    role: Literal["user", "agent"]


class Doc(BaseModel):
    id: str

    owner: DocOwner

    snippet: Snippet

    distance: Optional[float] = None

    metadata: Optional[object] = None

    title: Optional[str] = None


class ToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ToolChoiceNamedToolChoice(BaseModel):
    function: Optional[ToolChoiceNamedToolChoiceFunction] = None


ToolChoice: TypeAlias = Union[Literal["auto", "none"], ToolChoiceNamedToolChoice, None]


class ToolAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    files: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    timeout: Optional[int] = None


class ToolBash20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None


class ToolComputer20241022(BaseModel):
    display_height_px: Optional[int] = None

    display_number: Optional[int] = None

    display_width_px: Optional[int] = None

    name: Optional[str] = None

    type: Optional[Literal["computer_20241022"]] = None


class ToolFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ToolIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class ToolIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class ToolIntegrationBraveIntegrationDefSetup(BaseModel):
    brave_api_key: str


class ToolIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[ToolIntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class ToolIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class ToolIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ToolIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[ToolIntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class ToolIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    content_type: Optional[Literal["application/json", "text/csv", "application/xml", "application/jsonl"]] = None

    params: Optional[object] = None


class ToolIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class ToolIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[Literal["crawl", "links", "screenshot", "search"]] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[ToolIntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class ToolIntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class ToolIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class ToolIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class ToolIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class ToolIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[ToolIntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


class ToolIntegrationBrowserbaseContextIntegrationDefArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")


class ToolIntegrationBrowserbaseContextIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ToolIntegrationBrowserbaseContextIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBrowserbaseContextIntegrationDefArguments] = None

    method: Optional[Literal["create_context"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ToolIntegrationBrowserbaseContextIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseExtensionIntegrationDefArguments(BaseModel):
    repository_name: str = FieldInfo(alias="repositoryName")

    ref: Optional[str] = None


class ToolIntegrationBrowserbaseExtensionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ToolIntegrationBrowserbaseExtensionIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBrowserbaseExtensionIntegrationDefArguments] = None

    method: Optional[Literal["install_extension_from_github"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ToolIntegrationBrowserbaseExtensionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments(BaseModel):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]] = None


class ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ToolIntegrationBrowserbaseListSessionsIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments] = None

    method: Optional[Literal["list_sessions"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments(BaseModel):
    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None


class ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ToolIntegrationBrowserbaseCreateSessionIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments] = None

    method: Optional[Literal["create_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments(BaseModel):
    id: str


class ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ToolIntegrationBrowserbaseGetSessionIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments] = None

    method: Optional[Literal["get_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None


class ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ToolIntegrationBrowserbaseCompleteSessionIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments] = None

    method: Optional[Literal["complete_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(BaseModel):
    id: str


class ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments] = None

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ToolIntegrationRemoteBrowserIntegrationDefSetup(BaseModel):
    connect_url: Optional[str] = None

    height: Optional[int] = None

    width: Optional[int] = None


class ToolIntegrationRemoteBrowserIntegrationDefArguments(BaseModel):
    action: Literal[
        "key",
        "type",
        "mouse_move",
        "left_click",
        "left_click_drag",
        "right_click",
        "middle_click",
        "double_click",
        "screenshot",
        "cursor_position",
        "navigate",
        "refresh",
    ]

    connect_url: Optional[str] = None

    coordinate: Optional[List[object]] = None

    text: Optional[str] = None


class ToolIntegrationRemoteBrowserIntegrationDef(BaseModel):
    setup: ToolIntegrationRemoteBrowserIntegrationDefSetup
    """The setup parameters for the remote browser"""

    arguments: Optional[ToolIntegrationRemoteBrowserIntegrationDefArguments] = None
    """The arguments for the remote browser"""

    method: Optional[Literal["perform_action"]] = None

    provider: Optional[Literal["remote_browser"]] = None


class ToolIntegrationLlamaParseIntegrationDefArguments(BaseModel):
    file: Union[str, List[str]]

    base64: Optional[bool] = None

    filename: Optional[str] = None

    params: Optional[object] = None


class ToolIntegrationLlamaParseIntegrationDefSetup(BaseModel):
    llamaparse_api_key: str

    params: Optional[object] = None


class ToolIntegrationLlamaParseIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationLlamaParseIntegrationDefArguments] = None
    """Arguments for LlamaParse integration"""

    method: Optional[str] = None

    provider: Optional[Literal["llama_parse"]] = None

    setup: Optional[ToolIntegrationLlamaParseIntegrationDefSetup] = None
    """Setup parameters for LlamaParse integration"""


class ToolIntegrationFfmpegIntegrationDefArguments(BaseModel):
    cmd: str

    file: Union[str, List[str], None] = None


class ToolIntegrationFfmpegIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationFfmpegIntegrationDefArguments] = None
    """Arguments for Ffmpeg CMD"""

    method: Optional[str] = None

    provider: Optional[Literal["ffmpeg"]] = None

    setup: Optional[object] = None


class ToolIntegrationCloudinaryUploadIntegrationDefArguments(BaseModel):
    file: str

    public_id: Optional[str] = None

    return_base64: Optional[bool] = None

    upload_params: Optional[object] = None


class ToolIntegrationCloudinaryUploadIntegrationDefSetup(BaseModel):
    cloudinary_api_key: str

    cloudinary_api_secret: str

    cloudinary_cloud_name: str

    params: Optional[object] = None


class ToolIntegrationCloudinaryUploadIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationCloudinaryUploadIntegrationDefArguments] = None
    """Arguments for Cloudinary media upload"""

    method: Optional[Literal["media_upload"]] = None

    provider: Optional[Literal["cloudinary"]] = None

    setup: Optional[ToolIntegrationCloudinaryUploadIntegrationDefSetup] = None
    """Setup parameters for Cloudinary integration"""


class ToolIntegrationCloudinaryEditIntegrationDefArguments(BaseModel):
    public_id: str

    transformation: List[object]

    return_base64: Optional[bool] = None


class ToolIntegrationCloudinaryEditIntegrationDefSetup(BaseModel):
    cloudinary_api_key: str

    cloudinary_api_secret: str

    cloudinary_cloud_name: str

    params: Optional[object] = None


class ToolIntegrationCloudinaryEditIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationCloudinaryEditIntegrationDefArguments] = None
    """Arguments for Cloudinary media edit"""

    method: Optional[Literal["media_edit"]] = None

    provider: Optional[Literal["cloudinary"]] = None

    setup: Optional[ToolIntegrationCloudinaryEditIntegrationDefSetup] = None
    """Setup parameters for Cloudinary integration"""


class ToolIntegrationArxivIntegrationDefArguments(BaseModel):
    query: str

    download_pdf: Optional[bool] = None

    id_list: Optional[List[str]] = None

    max_results: Optional[int] = None

    sort_by: Optional[Literal["relevance", "lastUpdatedDate", "submittedDate"]] = None

    sort_order: Optional[Literal["ascending", "descending"]] = None


class ToolIntegrationArxivIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationArxivIntegrationDefArguments] = None
    """Arguments for Arxiv Search"""

    method: Optional[str] = None

    provider: Optional[Literal["arxiv"]] = None

    setup: Optional[object] = None


class ToolIntegrationUnstructuredIntegrationDefArguments(BaseModel):
    file: str

    filename: Optional[str] = None

    partition_params: Optional[object] = None


class ToolIntegrationUnstructuredIntegrationDefSetup(BaseModel):
    unstructured_api_key: str

    retry_config: Optional[object] = None

    server: Optional[str] = None

    server_url: Optional[str] = None

    timeout_ms: Optional[int] = None

    url_params: Optional[object] = None


class ToolIntegrationUnstructuredIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationUnstructuredIntegrationDefArguments] = None
    """Arguments for Unstructured partition integration"""

    method: Optional[str] = None

    provider: Optional[Literal["unstructured"]] = None

    setup: Optional[ToolIntegrationUnstructuredIntegrationDefSetup] = None
    """Setup parameters for Unstructured integration"""


class ToolIntegrationAlgoliaIntegrationDefArguments(BaseModel):
    index_name: str

    query: str

    attributes_to_retrieve: Optional[object] = None

    hits_per_page: Optional[int] = None


class ToolIntegrationAlgoliaIntegrationDefSetup(BaseModel):
    algolia_api_key: str

    algolia_application_id: str


class ToolIntegrationAlgoliaIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationAlgoliaIntegrationDefArguments] = None
    """Arguments for Algolia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["algolia"]] = None

    setup: Optional[ToolIntegrationAlgoliaIntegrationDefSetup] = None
    """Integration definition for Algolia"""


ToolIntegration: TypeAlias = Union[
    ToolIntegrationDummyIntegrationDef,
    ToolIntegrationBraveIntegrationDef,
    ToolIntegrationEmailIntegrationDef,
    ToolIntegrationSpiderIntegrationDef,
    ToolIntegrationWikipediaIntegrationDef,
    ToolIntegrationWeatherIntegrationDef,
    ToolIntegrationBrowserbaseContextIntegrationDef,
    ToolIntegrationBrowserbaseExtensionIntegrationDef,
    ToolIntegrationBrowserbaseListSessionsIntegrationDef,
    ToolIntegrationBrowserbaseCreateSessionIntegrationDef,
    ToolIntegrationBrowserbaseGetSessionIntegrationDef,
    ToolIntegrationBrowserbaseCompleteSessionIntegrationDef,
    ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
    ToolIntegrationRemoteBrowserIntegrationDef,
    ToolIntegrationLlamaParseIntegrationDef,
    ToolIntegrationFfmpegIntegrationDef,
    ToolIntegrationCloudinaryUploadIntegrationDef,
    ToolIntegrationCloudinaryEditIntegrationDef,
    ToolIntegrationArxivIntegrationDef,
    ToolIntegrationUnstructuredIntegrationDef,
    ToolIntegrationAlgoliaIntegrationDef,
    None,
]


class ToolSystem(BaseModel):
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


class ToolTextEditor20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["text_editor_20241022"]] = None


class Tool(BaseModel):
    name: str

    type: Literal[
        "function", "integration", "system", "api_call", "computer_20241022", "text_editor_20241022", "bash_20241022"
    ]

    api_call: Optional[ToolAPICall] = None
    """API call definition"""

    bash_20241022: Optional[ToolBash20241022] = None

    computer_20241022: Optional[ToolComputer20241022] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[ToolFunction] = None
    """Function definition"""

    integration: Optional[ToolIntegration] = None
    """Brave integration definition"""

    system: Optional[ToolSystem] = None
    """System definition"""

    text_editor_20241022: Optional[ToolTextEditor20241022] = None


class SessionRenderResponse(BaseModel):
    messages: List[Message]

    docs: Optional[List[Doc]] = None

    tool_choice: Optional[ToolChoice] = None

    tools: Optional[List[Tool]] = None

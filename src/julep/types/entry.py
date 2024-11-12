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
    "ContentToolBash20241022",
    "ContentToolComputer20241022",
    "ContentToolFunction",
    "ContentToolIntegration",
    "ContentToolIntegrationDummyIntegrationDef",
    "ContentToolIntegrationBraveIntegrationDef",
    "ContentToolIntegrationBraveIntegrationDefArguments",
    "ContentToolIntegrationBraveIntegrationDefSetup",
    "ContentToolIntegrationEmailIntegrationDef",
    "ContentToolIntegrationEmailIntegrationDefArguments",
    "ContentToolIntegrationEmailIntegrationDefSetup",
    "ContentToolIntegrationSpiderIntegrationDef",
    "ContentToolIntegrationSpiderIntegrationDefArguments",
    "ContentToolIntegrationSpiderIntegrationDefSetup",
    "ContentToolIntegrationWikipediaIntegrationDef",
    "ContentToolIntegrationWikipediaIntegrationDefArguments",
    "ContentToolIntegrationWeatherIntegrationDef",
    "ContentToolIntegrationWeatherIntegrationDefArguments",
    "ContentToolIntegrationWeatherIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseContextIntegrationDef",
    "ContentToolIntegrationBrowserbaseContextIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseContextIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseExtensionIntegrationDef",
    "ContentToolIntegrationBrowserbaseExtensionIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseExtensionIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseListSessionsIntegrationDef",
    "ContentToolIntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseCreateSessionIntegrationDef",
    "ContentToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseGetSessionIntegrationDef",
    "ContentToolIntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDef",
    "ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDef",
    "ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefArguments",
    "ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefSetup",
    "ContentToolIntegrationRemoteBrowserIntegrationDef",
    "ContentToolIntegrationRemoteBrowserIntegrationDefSetup",
    "ContentToolIntegrationRemoteBrowserIntegrationDefArguments",
    "ContentToolIntegrationLlamaParseIntegrationDef",
    "ContentToolIntegrationLlamaParseIntegrationDefArguments",
    "ContentToolIntegrationLlamaParseIntegrationDefSetup",
    "ContentToolSystem",
    "ContentToolTextEditor20241022",
    "ContentChosenFunctionCall",
    "ContentChosenFunctionCallFunction",
    "ContentChosenFunctionCallBash20241022",
    "ContentChosenFunctionCallComputer20241022",
    "ContentChosenFunctionCallTextEditor20241022",
    "ContentChosenComputer20241022",
    "ContentChosenTextEditor20241022",
    "ContentChosenBash20241022",
    "ContentToolResponse",
    "ContentUnionMember8",
    "ContentUnionMember8UnionMember0",
    "ContentUnionMember8UnionMember0Content",
    "ContentUnionMember8UnionMember0ContentModel",
    "ContentUnionMember8UnionMember0ContentModelImageURL",
    "ContentUnionMember8Tool",
    "ContentUnionMember8ToolAPICall",
    "ContentUnionMember8ToolBash20241022",
    "ContentUnionMember8ToolComputer20241022",
    "ContentUnionMember8ToolFunction",
    "ContentUnionMember8ToolIntegration",
    "ContentUnionMember8ToolIntegrationDummyIntegrationDef",
    "ContentUnionMember8ToolIntegrationBraveIntegrationDef",
    "ContentUnionMember8ToolIntegrationBraveIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBraveIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationEmailIntegrationDef",
    "ContentUnionMember8ToolIntegrationEmailIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationEmailIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationSpiderIntegrationDef",
    "ContentUnionMember8ToolIntegrationSpiderIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationSpiderIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationWikipediaIntegrationDef",
    "ContentUnionMember8ToolIntegrationWikipediaIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationWeatherIntegrationDef",
    "ContentUnionMember8ToolIntegrationWeatherIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationWeatherIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDef",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDef",
    "ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDefSetup",
    "ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationLlamaParseIntegrationDef",
    "ContentUnionMember8ToolIntegrationLlamaParseIntegrationDefArguments",
    "ContentUnionMember8ToolIntegrationLlamaParseIntegrationDefSetup",
    "ContentUnionMember8ToolSystem",
    "ContentUnionMember8ToolTextEditor20241022",
    "ContentUnionMember8ChosenFunctionCall",
    "ContentUnionMember8ChosenFunctionCallFunction",
    "ContentUnionMember8ChosenFunctionCallBash20241022",
    "ContentUnionMember8ChosenFunctionCallComputer20241022",
    "ContentUnionMember8ChosenFunctionCallTextEditor20241022",
    "ContentUnionMember8ChosenComputer20241022",
    "ContentUnionMember8ChosenTextEditor20241022",
    "ContentUnionMember8ChosenBash20241022",
    "ContentUnionMember8ToolResponse",
    "ToolCall",
    "ToolCallChosenFunctionCall",
    "ToolCallChosenFunctionCallFunction",
    "ToolCallChosenFunctionCallBash20241022",
    "ToolCallChosenFunctionCallComputer20241022",
    "ToolCallChosenFunctionCallTextEditor20241022",
    "ToolCallChosenComputer20241022",
    "ToolCallChosenTextEditor20241022",
    "ToolCallChosenBash20241022",
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

    data: Optional[object] = None

    files: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    timeout: Optional[int] = None


class ContentToolBash20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None


class ContentToolComputer20241022(BaseModel):
    display_height_px: Optional[int] = None

    display_number: Optional[int] = None

    display_width_px: Optional[int] = None

    name: Optional[str] = None

    type: Optional[Literal["computer_20241022"]] = None


class ContentToolFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentToolIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class ContentToolIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class ContentToolIntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[ContentToolIntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class ContentToolIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class ContentToolIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ContentToolIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[ContentToolIntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class ContentToolIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class ContentToolIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class ContentToolIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[ContentToolIntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class ContentToolIntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class ContentToolIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class ContentToolIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class ContentToolIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class ContentToolIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[ContentToolIntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


class ContentToolIntegrationBrowserbaseContextIntegrationDefArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")


class ContentToolIntegrationBrowserbaseContextIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseContextIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseContextIntegrationDefArguments] = None

    method: Optional[Literal["create_context"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseContextIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationBrowserbaseExtensionIntegrationDefArguments(BaseModel):
    repository_name: str = FieldInfo(alias="repositoryName")

    ref: Optional[str] = None


class ContentToolIntegrationBrowserbaseExtensionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseExtensionIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseExtensionIntegrationDefArguments] = None

    method: Optional[Literal["install_extension_from_github"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseExtensionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationBrowserbaseListSessionsIntegrationDefArguments(BaseModel):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]] = None


class ContentToolIntegrationBrowserbaseListSessionsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseListSessionsIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseListSessionsIntegrationDefArguments] = None

    method: Optional[Literal["list_sessions"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseListSessionsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments(BaseModel):
    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None


class ContentToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseCreateSessionIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments] = None

    method: Optional[Literal["create_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationBrowserbaseGetSessionIntegrationDefArguments(BaseModel):
    id: str


class ContentToolIntegrationBrowserbaseGetSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseGetSessionIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseGetSessionIntegrationDefArguments] = None

    method: Optional[Literal["get_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseGetSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None


class ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments] = None

    method: Optional[Literal["complete_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(BaseModel):
    id: str


class ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments] = None

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefArguments(BaseModel):
    id: str


class ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefArguments] = None

    method: Optional[Literal["get_connect_url"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolIntegrationRemoteBrowserIntegrationDefSetup(BaseModel):
    connect_url: Optional[str] = None

    height: Optional[int] = None

    width: Optional[int] = None


class ContentToolIntegrationRemoteBrowserIntegrationDefArguments(BaseModel):
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


class ContentToolIntegrationRemoteBrowserIntegrationDef(BaseModel):
    setup: ContentToolIntegrationRemoteBrowserIntegrationDefSetup
    """The setup parameters for the remote browser"""

    arguments: Optional[ContentToolIntegrationRemoteBrowserIntegrationDefArguments] = None
    """The arguments for the remote browser"""

    method: Optional[Literal["perform_action"]] = None

    provider: Optional[Literal["remote_browser"]] = None


class ContentToolIntegrationLlamaParseIntegrationDefArguments(BaseModel):
    file: str

    filename: Optional[str] = None

    language: Optional[str] = None

    num_workers: Optional[int] = None

    result_format: Optional[Literal["text", "markdown"]] = None

    verbose: Optional[bool] = None


class ContentToolIntegrationLlamaParseIntegrationDefSetup(BaseModel):
    llamaparse_api_key: str


class ContentToolIntegrationLlamaParseIntegrationDef(BaseModel):
    arguments: Optional[ContentToolIntegrationLlamaParseIntegrationDefArguments] = None
    """Arguments for LlamaParse integration"""

    method: Optional[str] = None

    provider: Optional[Literal["llama_parse"]] = None

    setup: Optional[ContentToolIntegrationLlamaParseIntegrationDefSetup] = None
    """Setup parameters for LlamaParse integration"""


ContentToolIntegration: TypeAlias = Union[
    ContentToolIntegrationDummyIntegrationDef,
    ContentToolIntegrationBraveIntegrationDef,
    ContentToolIntegrationEmailIntegrationDef,
    ContentToolIntegrationSpiderIntegrationDef,
    ContentToolIntegrationWikipediaIntegrationDef,
    ContentToolIntegrationWeatherIntegrationDef,
    ContentToolIntegrationBrowserbaseContextIntegrationDef,
    ContentToolIntegrationBrowserbaseExtensionIntegrationDef,
    ContentToolIntegrationBrowserbaseListSessionsIntegrationDef,
    ContentToolIntegrationBrowserbaseCreateSessionIntegrationDef,
    ContentToolIntegrationBrowserbaseGetSessionIntegrationDef,
    ContentToolIntegrationBrowserbaseCompleteSessionIntegrationDef,
    ContentToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
    ContentToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDef,
    ContentToolIntegrationRemoteBrowserIntegrationDef,
    ContentToolIntegrationLlamaParseIntegrationDef,
    None,
]


class ContentToolSystem(BaseModel):
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


class ContentToolTextEditor20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["text_editor_20241022"]] = None


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

    bash_20241022: Optional[ContentToolBash20241022] = None

    computer_20241022: Optional[ContentToolComputer20241022] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[ContentToolFunction] = None
    """Function definition"""

    integration: Optional[ContentToolIntegration] = None
    """Brave integration definition"""

    system: Optional[ContentToolSystem] = None
    """System definition"""

    text_editor_20241022: Optional[ContentToolTextEditor20241022] = None


class ContentChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ContentChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ContentChosenFunctionCallComputer20241022(BaseModel):
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


class ContentChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ContentChosenFunctionCall(BaseModel):
    function: ContentChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ContentChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ContentChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ContentChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ContentChosenComputer20241022(BaseModel):
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


class ContentChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ContentChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ContentToolResponse(BaseModel):
    id: str

    output: object


class ContentUnionMember8UnionMember0Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ContentUnionMember8UnionMember0ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ContentUnionMember8UnionMember0ContentModel(BaseModel):
    image_url: ContentUnionMember8UnionMember0ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


ContentUnionMember8UnionMember0: TypeAlias = Union[
    ContentUnionMember8UnionMember0Content, ContentUnionMember8UnionMember0ContentModel
]


class ContentUnionMember8ToolAPICall(BaseModel):
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


class ContentUnionMember8ToolBash20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None


class ContentUnionMember8ToolComputer20241022(BaseModel):
    display_height_px: Optional[int] = None

    display_number: Optional[int] = None

    display_width_px: Optional[int] = None

    name: Optional[str] = None

    type: Optional[Literal["computer_20241022"]] = None


class ContentUnionMember8ToolFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentUnionMember8ToolIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class ContentUnionMember8ToolIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class ContentUnionMember8ToolIntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class ContentUnionMember8ToolIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class ContentUnionMember8ToolIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ContentUnionMember8ToolIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class ContentUnionMember8ToolIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class ContentUnionMember8ToolIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class ContentUnionMember8ToolIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class ContentUnionMember8ToolIntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class ContentUnionMember8ToolIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class ContentUnionMember8ToolIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class ContentUnionMember8ToolIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class ContentUnionMember8ToolIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


class ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDefArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")


class ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDefArguments] = None

    method: Optional[Literal["create_context"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDefArguments(BaseModel):
    repository_name: str = FieldInfo(alias="repositoryName")

    ref: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDefArguments] = None

    method: Optional[Literal["install_extension_from_github"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments(BaseModel):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]] = None


class ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments] = None

    method: Optional[Literal["list_sessions"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments(BaseModel):
    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None


class ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments] = None

    method: Optional[Literal["create_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments(BaseModel):
    id: str


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments] = None

    method: Optional[Literal["get_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None


class ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments] = None

    method: Optional[Literal["complete_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(BaseModel):
    id: str


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments] = None

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefArguments(BaseModel):
    id: str


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefArguments] = None

    method: Optional[Literal["get_connect_url"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDefSetup(BaseModel):
    connect_url: Optional[str] = None

    height: Optional[int] = None

    width: Optional[int] = None


class ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDefArguments(BaseModel):
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


class ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDef(BaseModel):
    setup: ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDefSetup
    """The setup parameters for the remote browser"""

    arguments: Optional[ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDefArguments] = None
    """The arguments for the remote browser"""

    method: Optional[Literal["perform_action"]] = None

    provider: Optional[Literal["remote_browser"]] = None


class ContentUnionMember8ToolIntegrationLlamaParseIntegrationDefArguments(BaseModel):
    file: str

    filename: Optional[str] = None

    language: Optional[str] = None

    num_workers: Optional[int] = None

    result_format: Optional[Literal["text", "markdown"]] = None

    verbose: Optional[bool] = None


class ContentUnionMember8ToolIntegrationLlamaParseIntegrationDefSetup(BaseModel):
    llamaparse_api_key: str


class ContentUnionMember8ToolIntegrationLlamaParseIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolIntegrationLlamaParseIntegrationDefArguments] = None
    """Arguments for LlamaParse integration"""

    method: Optional[str] = None

    provider: Optional[Literal["llama_parse"]] = None

    setup: Optional[ContentUnionMember8ToolIntegrationLlamaParseIntegrationDefSetup] = None
    """Setup parameters for LlamaParse integration"""


ContentUnionMember8ToolIntegration: TypeAlias = Union[
    ContentUnionMember8ToolIntegrationDummyIntegrationDef,
    ContentUnionMember8ToolIntegrationBraveIntegrationDef,
    ContentUnionMember8ToolIntegrationEmailIntegrationDef,
    ContentUnionMember8ToolIntegrationSpiderIntegrationDef,
    ContentUnionMember8ToolIntegrationWikipediaIntegrationDef,
    ContentUnionMember8ToolIntegrationWeatherIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseContextIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseExtensionIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseListSessionsIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseCreateSessionIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseGetSessionIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseCompleteSessionIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
    ContentUnionMember8ToolIntegrationBrowserbaseGetSessionConnectURLIntegrationDef,
    ContentUnionMember8ToolIntegrationRemoteBrowserIntegrationDef,
    ContentUnionMember8ToolIntegrationLlamaParseIntegrationDef,
    None,
]


class ContentUnionMember8ToolSystem(BaseModel):
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


class ContentUnionMember8ToolTextEditor20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["text_editor_20241022"]] = None


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

    bash_20241022: Optional[ContentUnionMember8ToolBash20241022] = None

    computer_20241022: Optional[ContentUnionMember8ToolComputer20241022] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[ContentUnionMember8ToolFunction] = None
    """Function definition"""

    integration: Optional[ContentUnionMember8ToolIntegration] = None
    """Brave integration definition"""

    system: Optional[ContentUnionMember8ToolSystem] = None
    """System definition"""

    text_editor_20241022: Optional[ContentUnionMember8ToolTextEditor20241022] = None


class ContentUnionMember8ChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ContentUnionMember8ChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ContentUnionMember8ChosenFunctionCallComputer20241022(BaseModel):
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


class ContentUnionMember8ChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ContentUnionMember8ChosenFunctionCall(BaseModel):
    function: ContentUnionMember8ChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ContentUnionMember8ChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ContentUnionMember8ChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ContentUnionMember8ChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ContentUnionMember8ChosenComputer20241022(BaseModel):
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


class ContentUnionMember8ChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ContentUnionMember8ChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ContentUnionMember8ToolResponse(BaseModel):
    id: str

    output: object


ContentUnionMember8: TypeAlias = Union[
    List[ContentUnionMember8UnionMember0],
    ContentUnionMember8Tool,
    ContentUnionMember8ChosenFunctionCall,
    ContentUnionMember8ChosenComputer20241022,
    ContentUnionMember8ChosenTextEditor20241022,
    ContentUnionMember8ChosenBash20241022,
    str,
    ContentUnionMember8ToolResponse,
]

Content: TypeAlias = Union[
    List[ContentUnionMember0],
    ContentTool,
    ContentChosenFunctionCall,
    ContentChosenComputer20241022,
    ContentChosenTextEditor20241022,
    ContentChosenBash20241022,
    str,
    ContentToolResponse,
    List[ContentUnionMember8],
]


class ToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ToolCallChosenFunctionCallComputer20241022(BaseModel):
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


class ToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ToolCallChosenFunctionCall(BaseModel):
    function: ToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ToolCallChosenComputer20241022(BaseModel):
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


class ToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


ToolCall: TypeAlias = Union[
    ToolCallChosenFunctionCall,
    ToolCallChosenComputer20241022,
    ToolCallChosenTextEditor20241022,
    ToolCallChosenBash20241022,
]


class Entry(BaseModel):
    id: str

    content: Content

    created_at: datetime

    role: Literal["user", "assistant", "system", "tool"]

    source: Literal["api_request", "api_response", "tool_response", "internal", "summarizer", "meta"]

    timestamp: float

    token_count: int

    tokenizer: str

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[ToolCall]] = None

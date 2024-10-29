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
    "ContentToolOutputBash20241022",
    "ContentToolOutputComputer20241022",
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
    "ContentToolOutputIntegrationBrowserbaseContextIntegrationDef",
    "ContentToolOutputIntegrationBrowserbaseContextIntegrationDefSetup",
    "ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDef",
    "ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDef",
    "ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDef",
    "ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDef",
    "ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefArguments",
    "ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefSetup",
    "ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "ContentToolOutputSystem",
    "ContentToolOutputTextEditor20241022",
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
    "ContentUnionMember8ToolOutput",
    "ContentUnionMember8ToolOutputAPICall",
    "ContentUnionMember8ToolOutputBash20241022",
    "ContentUnionMember8ToolOutputComputer20241022",
    "ContentUnionMember8ToolOutputFunction",
    "ContentUnionMember8ToolOutputIntegration",
    "ContentUnionMember8ToolOutputIntegrationDummyIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBraveIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBraveIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationBraveIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationEmailIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationEmailIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationEmailIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationWikipediaIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationWikipediaIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseContextIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseContextIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefSetup",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "ContentUnionMember8ToolOutputSystem",
    "ContentUnionMember8ToolOutputTextEditor20241022",
    "ContentUnionMember8ChosenFunctionCall",
    "ContentUnionMember8ChosenFunctionCallFunction",
    "ContentUnionMember8ChosenFunctionCallBash20241022",
    "ContentUnionMember8ChosenFunctionCallComputer20241022",
    "ContentUnionMember8ChosenFunctionCallTextEditor20241022",
    "ContentUnionMember8ChosenComputer20241022",
    "ContentUnionMember8ChosenTextEditor20241022",
    "ContentUnionMember8ChosenBash20241022",
    "ContentUnionMember8ToolResponse",
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


class ContentToolOutputBash20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None


class ContentToolOutputComputer20241022(BaseModel):
    display_height_px: Optional[int] = None

    display_number: Optional[int] = None

    display_width_px: Optional[int] = None

    name: Optional[str] = None

    type: Optional[Literal["computer_20241022"]] = None


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


class ContentToolOutputIntegrationBrowserbaseContextIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolOutputIntegrationBrowserbaseContextIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[Literal["create_context"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolOutputIntegrationBrowserbaseContextIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDefArguments(BaseModel):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]] = None


class ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDef(BaseModel):
    arguments: Optional[ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDefArguments] = None

    method: Optional[Literal["list_sessions"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")

    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None


class ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDef(BaseModel):
    arguments: ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefArguments

    method: Optional[Literal["create_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDefArguments(BaseModel):
    id: str


class ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDef(BaseModel):
    arguments: ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDefArguments

    method: Optional[Literal["get_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None


class ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDef(BaseModel):
    arguments: ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefArguments

    method: Optional[Literal["update_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(BaseModel):
    id: str


class ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(BaseModel):
    api_key: str


class ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


ContentToolOutputIntegration: TypeAlias = Union[
    ContentToolOutputIntegrationDummyIntegrationDef,
    ContentToolOutputIntegrationBraveIntegrationDef,
    ContentToolOutputIntegrationEmailIntegrationDef,
    ContentToolOutputIntegrationSpiderIntegrationDef,
    ContentToolOutputIntegrationWikipediaIntegrationDef,
    ContentToolOutputIntegrationWeatherIntegrationDef,
    ContentToolOutputIntegrationBrowserbaseContextIntegrationDef,
    ContentToolOutputIntegrationBrowserbaseListSessionsIntegrationDef,
    ContentToolOutputIntegrationBrowserbaseCreateSessionIntegrationDef,
    ContentToolOutputIntegrationBrowserbaseGetSessionIntegrationDef,
    ContentToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDef,
    ContentToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
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


class ContentToolOutputTextEditor20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["text_editor_20241022"]] = None


class ContentToolOutput(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    api_call: Optional[ContentToolOutputAPICall] = None
    """API call definition"""

    bash_20241022: Optional[ContentToolOutputBash20241022] = None

    computer_20241022: Optional[ContentToolOutputComputer20241022] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[ContentToolOutputFunction] = None
    """Function definition"""

    integration: Optional[ContentToolOutputIntegration] = None
    """Brave integration definition"""

    system: Optional[ContentToolOutputSystem] = None
    """System definition"""

    text_editor_20241022: Optional[ContentToolOutputTextEditor20241022] = None


class ContentChosenFunctionCallFunction(BaseModel):
    name: str


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


class ContentUnionMember8ToolOutputAPICall(BaseModel):
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


class ContentUnionMember8ToolOutputBash20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None


class ContentUnionMember8ToolOutputComputer20241022(BaseModel):
    display_height_px: Optional[int] = None

    display_number: Optional[int] = None

    display_width_px: Optional[int] = None

    name: Optional[str] = None

    type: Optional[Literal["computer_20241022"]] = None


class ContentUnionMember8ToolOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ContentUnionMember8ToolOutputIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class ContentUnionMember8ToolOutputIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class ContentUnionMember8ToolOutputIntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolOutputIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolOutputIntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class ContentUnionMember8ToolOutputIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class ContentUnionMember8ToolOutputIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ContentUnionMember8ToolOutputIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolOutputIntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class ContentUnionMember8ToolOutputIntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class ContentUnionMember8ToolOutputIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolOutputIntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


class ContentUnionMember8ToolOutputIntegrationBrowserbaseContextIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseContextIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[Literal["create_context"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationBrowserbaseContextIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDefArguments(BaseModel):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]] = None


class ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDef(BaseModel):
    arguments: Optional[ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDefArguments] = None

    method: Optional[Literal["list_sessions"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")

    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None


class ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDef(BaseModel):
    arguments: ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefArguments

    method: Optional[Literal["create_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDefArguments(BaseModel):
    id: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDef(BaseModel):
    arguments: ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDefArguments

    method: Optional[Literal["get_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None


class ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDef(BaseModel):
    arguments: ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefArguments

    method: Optional[Literal["update_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(BaseModel):
    id: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(BaseModel):
    api_key: str


class ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


ContentUnionMember8ToolOutputIntegration: TypeAlias = Union[
    ContentUnionMember8ToolOutputIntegrationDummyIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationBraveIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationEmailIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationSpiderIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationWikipediaIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationWeatherIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationBrowserbaseContextIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationBrowserbaseListSessionsIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationBrowserbaseCreateSessionIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationBrowserbaseUpdateSessionIntegrationDef,
    ContentUnionMember8ToolOutputIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
    None,
]


class ContentUnionMember8ToolOutputSystem(BaseModel):
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


class ContentUnionMember8ToolOutputTextEditor20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["text_editor_20241022"]] = None


class ContentUnionMember8ToolOutput(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    api_call: Optional[ContentUnionMember8ToolOutputAPICall] = None
    """API call definition"""

    bash_20241022: Optional[ContentUnionMember8ToolOutputBash20241022] = None

    computer_20241022: Optional[ContentUnionMember8ToolOutputComputer20241022] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[ContentUnionMember8ToolOutputFunction] = None
    """Function definition"""

    integration: Optional[ContentUnionMember8ToolOutputIntegration] = None
    """Brave integration definition"""

    system: Optional[ContentUnionMember8ToolOutputSystem] = None
    """System definition"""

    text_editor_20241022: Optional[ContentUnionMember8ToolOutputTextEditor20241022] = None


class ContentUnionMember8ChosenFunctionCallFunction(BaseModel):
    name: str


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
    ContentUnionMember8ToolOutput,
    ContentUnionMember8ChosenFunctionCall,
    ContentUnionMember8ChosenComputer20241022,
    ContentUnionMember8ChosenTextEditor20241022,
    ContentUnionMember8ChosenBash20241022,
    str,
    ContentUnionMember8ToolResponse,
]

Content: TypeAlias = Union[
    List[ContentUnionMember0],
    ContentToolOutput,
    ContentChosenFunctionCall,
    ContentChosenComputer20241022,
    ContentChosenTextEditor20241022,
    ContentChosenBash20241022,
    str,
    ContentToolResponse,
    List[ContentUnionMember8],
]


class Entry(BaseModel):
    id: str

    content: Content

    created_at: datetime

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    source: Literal["api_request", "api_response", "tool_response", "internal", "summarizer", "meta"]

    timestamp: float

    token_count: int

    tokenizer: str

    name: Optional[str] = None

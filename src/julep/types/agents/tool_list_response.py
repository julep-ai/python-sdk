# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ToolListResponse",
    "APICall",
    "Bash20241022",
    "Computer20241022",
    "Function",
    "Integration",
    "IntegrationDummyIntegrationDef",
    "IntegrationBraveIntegrationDef",
    "IntegrationBraveIntegrationDefArguments",
    "IntegrationBraveIntegrationDefSetup",
    "IntegrationEmailIntegrationDef",
    "IntegrationEmailIntegrationDefArguments",
    "IntegrationEmailIntegrationDefSetup",
    "IntegrationSpiderIntegrationDef",
    "IntegrationSpiderIntegrationDefArguments",
    "IntegrationSpiderIntegrationDefSetup",
    "IntegrationWikipediaIntegrationDef",
    "IntegrationWikipediaIntegrationDefArguments",
    "IntegrationWeatherIntegrationDef",
    "IntegrationWeatherIntegrationDefArguments",
    "IntegrationWeatherIntegrationDefSetup",
    "IntegrationBrowserbaseContextIntegrationDef",
    "IntegrationBrowserbaseContextIntegrationDefSetup",
    "IntegrationBrowserbaseListSessionsIntegrationDef",
    "IntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "IntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "IntegrationBrowserbaseCreateSessionIntegrationDef",
    "IntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "IntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "IntegrationBrowserbaseGetSessionIntegrationDef",
    "IntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "IntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "IntegrationBrowserbaseUpdateSessionIntegrationDef",
    "IntegrationBrowserbaseUpdateSessionIntegrationDefArguments",
    "IntegrationBrowserbaseUpdateSessionIntegrationDefSetup",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "System",
    "TextEditor20241022",
]


class APICall(BaseModel):
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


class Bash20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None


class Computer20241022(BaseModel):
    display_height_px: Optional[int] = None

    display_number: Optional[int] = None

    display_width_px: Optional[int] = None

    name: Optional[str] = None

    type: Optional[Literal["computer_20241022"]] = None


class Function(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class IntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class IntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class IntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class IntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[IntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class IntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class IntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class IntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[IntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[IntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class IntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class IntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class IntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[IntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[IntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class IntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class IntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[IntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class IntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class IntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class IntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[IntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[IntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


class IntegrationBrowserbaseContextIntegrationDefSetup(BaseModel):
    api_key: str


class IntegrationBrowserbaseContextIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[Literal["create_context"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseContextIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseListSessionsIntegrationDefArguments(BaseModel):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]] = None


class IntegrationBrowserbaseListSessionsIntegrationDefSetup(BaseModel):
    api_key: str


class IntegrationBrowserbaseListSessionsIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseListSessionsIntegrationDefArguments] = None

    method: Optional[Literal["list_sessions"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseListSessionsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCreateSessionIntegrationDefArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")

    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None


class IntegrationBrowserbaseCreateSessionIntegrationDefSetup(BaseModel):
    api_key: str


class IntegrationBrowserbaseCreateSessionIntegrationDef(BaseModel):
    arguments: IntegrationBrowserbaseCreateSessionIntegrationDefArguments

    method: Optional[Literal["create_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionIntegrationDefArguments(BaseModel):
    id: str


class IntegrationBrowserbaseGetSessionIntegrationDefSetup(BaseModel):
    api_key: str


class IntegrationBrowserbaseGetSessionIntegrationDef(BaseModel):
    arguments: IntegrationBrowserbaseGetSessionIntegrationDefArguments

    method: Optional[Literal["get_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseGetSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseUpdateSessionIntegrationDefArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None


class IntegrationBrowserbaseUpdateSessionIntegrationDefSetup(BaseModel):
    api_key: str


class IntegrationBrowserbaseUpdateSessionIntegrationDef(BaseModel):
    arguments: IntegrationBrowserbaseUpdateSessionIntegrationDefArguments

    method: Optional[Literal["update_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseUpdateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(BaseModel):
    id: str


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(BaseModel):
    api_key: str


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


Integration: TypeAlias = Union[
    IntegrationDummyIntegrationDef,
    IntegrationBraveIntegrationDef,
    IntegrationEmailIntegrationDef,
    IntegrationSpiderIntegrationDef,
    IntegrationWikipediaIntegrationDef,
    IntegrationWeatherIntegrationDef,
    IntegrationBrowserbaseContextIntegrationDef,
    IntegrationBrowserbaseListSessionsIntegrationDef,
    IntegrationBrowserbaseCreateSessionIntegrationDef,
    IntegrationBrowserbaseGetSessionIntegrationDef,
    IntegrationBrowserbaseUpdateSessionIntegrationDef,
    IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
    None,
]


class System(BaseModel):
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


class TextEditor20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["text_editor_20241022"]] = None


class ToolListResponse(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    api_call: Optional[APICall] = None
    """API call definition"""

    bash_20241022: Optional[Bash20241022] = None

    computer_20241022: Optional[Computer20241022] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[Function] = None
    """Function definition"""

    integration: Optional[Integration] = None
    """Brave integration definition"""

    system: Optional[System] = None
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022] = None

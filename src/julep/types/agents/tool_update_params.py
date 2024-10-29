# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ToolUpdateParams",
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


class ToolUpdateParams(TypedDict, total=False):
    agent_id: Required[str]

    name: Required[str]

    api_call: Optional[APICall]
    """API call definition"""

    bash_20241022: Optional[Bash20241022]

    computer_20241022: Optional[Computer20241022]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[Function]
    """Function definition"""

    integration: Optional[Integration]
    """Brave integration definition"""

    system: Optional[System]
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022]


class APICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class Bash20241022(TypedDict, total=False):
    name: str

    type: Literal["bash_20241022"]


class Computer20241022(TypedDict, total=False):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class Function(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class IntegrationDummyIntegrationDef(TypedDict, total=False):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class IntegrationBraveIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]


class IntegrationBraveIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class IntegrationBraveIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBraveIntegrationDefArguments]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[IntegrationBraveIntegrationDefSetup]
    """Integration definition for Brave Search"""


_IntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_IntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class IntegrationEmailIntegrationDefArguments(_IntegrationEmailIntegrationDefArgumentsReservedKeywords, total=False):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class IntegrationEmailIntegrationDefSetup(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class IntegrationEmailIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationEmailIntegrationDefArguments]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[IntegrationEmailIntegrationDefSetup]
    """Setup parameters for Email integration"""


class IntegrationSpiderIntegrationDefArguments(TypedDict, total=False):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class IntegrationSpiderIntegrationDefSetup(TypedDict, total=False):
    spider_api_key: Required[str]


class IntegrationSpiderIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationSpiderIntegrationDefArguments]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[IntegrationSpiderIntegrationDefSetup]
    """Setup parameters for Spider integration"""


class IntegrationWikipediaIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]

    load_max_docs: int


class IntegrationWikipediaIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationWikipediaIntegrationDefArguments]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class IntegrationWeatherIntegrationDefArguments(TypedDict, total=False):
    location: Required[str]


class IntegrationWeatherIntegrationDefSetup(TypedDict, total=False):
    openweathermap_api_key: Required[str]


class IntegrationWeatherIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationWeatherIntegrationDefArguments]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[IntegrationWeatherIntegrationDefSetup]
    """Integration definition for Weather"""


class IntegrationBrowserbaseContextIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class IntegrationBrowserbaseContextIntegrationDef(TypedDict, total=False):
    arguments: Optional[object]

    method: Literal["create_context"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseContextIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseListSessionsIntegrationDefArguments(TypedDict, total=False):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]]


class IntegrationBrowserbaseListSessionsIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class IntegrationBrowserbaseListSessionsIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseListSessionsIntegrationDefArguments]

    method: Literal["list_sessions"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseListSessionsIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCreateSessionIntegrationDefArguments(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    browser_settings: Annotated[Optional[object], PropertyInfo(alias="browserSettings")]

    extension_id: Annotated[Optional[str], PropertyInfo(alias="extensionId")]

    keep_alive: Annotated[Optional[bool], PropertyInfo(alias="keepAlive")]

    proxies: Union[bool, Iterable[object], None]

    timeout: Optional[int]


class IntegrationBrowserbaseCreateSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class IntegrationBrowserbaseCreateSessionIntegrationDef(TypedDict, total=False):
    arguments: Required[IntegrationBrowserbaseCreateSessionIntegrationDefArguments]

    method: Literal["create_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]


class IntegrationBrowserbaseGetSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class IntegrationBrowserbaseGetSessionIntegrationDef(TypedDict, total=False):
    arguments: Required[IntegrationBrowserbaseGetSessionIntegrationDefArguments]

    method: Literal["get_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseGetSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseUpdateSessionIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]

    status: Literal["REQUEST_RELEASE"]


class IntegrationBrowserbaseUpdateSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class IntegrationBrowserbaseUpdateSessionIntegrationDef(TypedDict, total=False):
    arguments: Required[IntegrationBrowserbaseUpdateSessionIntegrationDefArguments]

    method: Literal["update_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseUpdateSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(TypedDict, total=False):
    arguments: Required[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments]

    method: Literal["get_live_urls"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup]
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
]


class System(TypedDict, total=False):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class TextEditor20241022(TypedDict, total=False):
    name: str

    type: Literal["text_editor_20241022"]

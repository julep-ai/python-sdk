# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ToolPatchParams",
    "APICall",
    "Bash20241022",
    "Computer20241022",
    "Function",
    "Integration",
    "IntegrationDummyIntegrationDefUpdate",
    "IntegrationBraveIntegrationDefUpdate",
    "IntegrationBraveIntegrationDefUpdateArguments",
    "IntegrationBraveIntegrationDefUpdateSetup",
    "IntegrationEmailIntegrationDefUpdate",
    "IntegrationEmailIntegrationDefUpdateArguments",
    "IntegrationEmailIntegrationDefUpdateSetup",
    "IntegrationSpiderIntegrationDefUpdate",
    "IntegrationSpiderIntegrationDefUpdateArguments",
    "IntegrationSpiderIntegrationDefUpdateSetup",
    "IntegrationWikipediaIntegrationDefUpdate",
    "IntegrationWikipediaIntegrationDefUpdateArguments",
    "IntegrationWeatherIntegrationDefUpdate",
    "IntegrationWeatherIntegrationDefUpdateArguments",
    "IntegrationWeatherIntegrationDefUpdateSetup",
    "System",
    "TextEditor20241022",
]


class ToolPatchParams(TypedDict, total=False):
    agent_id: Required[str]

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

    name: Optional[str]

    system: Optional[System]
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022]


class APICall(TypedDict, total=False):
    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    params: Union[str, object, None]

    timeout: Optional[int]

    url: Optional[str]


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


class IntegrationDummyIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class IntegrationBraveIntegrationDefUpdateArguments(TypedDict, total=False):
    query: Optional[str]


class IntegrationBraveIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]


class IntegrationBraveIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBraveIntegrationDefUpdateArguments]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[IntegrationBraveIntegrationDefUpdateSetup]
    """Integration definition for Brave Search"""


_IntegrationEmailIntegrationDefUpdateArgumentsReservedKeywords = TypedDict(
    "_IntegrationEmailIntegrationDefUpdateArgumentsReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class IntegrationEmailIntegrationDefUpdateArguments(
    _IntegrationEmailIntegrationDefUpdateArgumentsReservedKeywords, total=False
):
    body: Optional[str]

    subject: Optional[str]

    to: Optional[str]


class IntegrationEmailIntegrationDefUpdateSetup(TypedDict, total=False):
    host: Optional[str]

    password: Optional[str]

    port: Optional[int]

    user: Optional[str]


class IntegrationEmailIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationEmailIntegrationDefUpdateArguments]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[IntegrationEmailIntegrationDefUpdateSetup]
    """Setup parameters for Email integration"""


class IntegrationSpiderIntegrationDefUpdateArguments(TypedDict, total=False):
    mode: Literal["scrape"]

    params: Optional[object]

    url: Optional[str]


class IntegrationSpiderIntegrationDefUpdateSetup(TypedDict, total=False):
    spider_api_key: Optional[str]


class IntegrationSpiderIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationSpiderIntegrationDefUpdateArguments]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[IntegrationSpiderIntegrationDefUpdateSetup]
    """Setup parameters for Spider integration"""


class IntegrationWikipediaIntegrationDefUpdateArguments(TypedDict, total=False):
    load_max_docs: int

    query: Optional[str]


class IntegrationWikipediaIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationWikipediaIntegrationDefUpdateArguments]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class IntegrationWeatherIntegrationDefUpdateArguments(TypedDict, total=False):
    location: Optional[str]


class IntegrationWeatherIntegrationDefUpdateSetup(TypedDict, total=False):
    openweathermap_api_key: Optional[str]


class IntegrationWeatherIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationWeatherIntegrationDefUpdateArguments]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[IntegrationWeatherIntegrationDefUpdateSetup]
    """Integration definition for Weather"""


Integration: TypeAlias = Union[
    IntegrationDummyIntegrationDefUpdate,
    IntegrationBraveIntegrationDefUpdate,
    IntegrationEmailIntegrationDefUpdate,
    IntegrationSpiderIntegrationDefUpdate,
    IntegrationWikipediaIntegrationDefUpdate,
    IntegrationWeatherIntegrationDefUpdate,
]


class System(TypedDict, total=False):
    arguments: Optional[object]

    operation: Optional[
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

    resource: Optional[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class TextEditor20241022(TypedDict, total=False):
    name: str

    type: Literal["text_editor_20241022"]

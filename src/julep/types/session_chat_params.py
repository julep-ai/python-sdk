# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .message_param import MessageParam

__all__ = [
    "SessionChatParams",
    "ResponseFormat",
    "ResponseFormatSimpleCompletionResponseFormat",
    "ResponseFormatSchemaCompletionResponseFormat",
    "ToolChoice",
    "ToolChoiceNamedToolChoice",
    "ToolChoiceNamedToolChoiceFunction",
    "Tool",
    "ToolAPICall",
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
    "ToolSystem",
]


class SessionChatParams(TypedDict, total=False):
    messages: Required[Iterable[MessageParam]]

    agent: Optional[str]

    frequency_penalty: Optional[float]

    length_penalty: Optional[float]

    logit_bias: Optional[Dict[str, float]]

    max_tokens: Optional[int]

    min_p: Optional[float]

    model: Optional[str]

    presence_penalty: Optional[float]

    recall: bool

    repetition_penalty: Optional[float]

    response_format: Optional[ResponseFormat]

    save: bool

    seed: Optional[int]

    stop: List[str]

    stream: bool

    temperature: Optional[float]

    tool_choice: Optional[ToolChoice]

    tools: Iterable[Tool]

    top_p: Optional[float]

    x_custom_api_key: Annotated[str, PropertyInfo(alias="X-Custom-Api-Key")]


class ResponseFormatSimpleCompletionResponseFormat(TypedDict, total=False):
    type: Literal["text", "json_object"]


class ResponseFormatSchemaCompletionResponseFormat(TypedDict, total=False):
    json_schema: Required[object]

    type: Literal["json_schema"]


ResponseFormat: TypeAlias = Union[
    ResponseFormatSimpleCompletionResponseFormat, ResponseFormatSchemaCompletionResponseFormat
]


class ToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class ToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[ToolChoiceNamedToolChoiceFunction]


ToolChoice: TypeAlias = Union[Literal["auto", "none"], ToolChoiceNamedToolChoice]


class ToolAPICall(TypedDict, total=False):
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


class ToolFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class ToolIntegrationDummyIntegrationDef(TypedDict, total=False):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class ToolIntegrationBraveIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]


class ToolIntegrationBraveIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class ToolIntegrationBraveIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBraveIntegrationDefArguments]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[ToolIntegrationBraveIntegrationDefSetup]
    """Integration definition for Brave Search"""


_ToolIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_ToolIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ToolIntegrationEmailIntegrationDefArguments(
    _ToolIntegrationEmailIntegrationDefArgumentsReservedKeywords, total=False
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class ToolIntegrationEmailIntegrationDefSetup(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class ToolIntegrationEmailIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationEmailIntegrationDefArguments]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[ToolIntegrationEmailIntegrationDefSetup]
    """Setup parameters for Email integration"""


class ToolIntegrationSpiderIntegrationDefArguments(TypedDict, total=False):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class ToolIntegrationSpiderIntegrationDefSetup(TypedDict, total=False):
    spider_api_key: Required[str]


class ToolIntegrationSpiderIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationSpiderIntegrationDefArguments]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[ToolIntegrationSpiderIntegrationDefSetup]
    """Setup parameters for Spider integration"""


class ToolIntegrationWikipediaIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]

    load_max_docs: int


class ToolIntegrationWikipediaIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationWikipediaIntegrationDefArguments]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class ToolIntegrationWeatherIntegrationDefArguments(TypedDict, total=False):
    location: Required[str]


class ToolIntegrationWeatherIntegrationDefSetup(TypedDict, total=False):
    openweathermap_api_key: Required[str]


class ToolIntegrationWeatherIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationWeatherIntegrationDefArguments]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[ToolIntegrationWeatherIntegrationDefSetup]
    """Integration definition for Weather"""


ToolIntegration: TypeAlias = Union[
    ToolIntegrationDummyIntegrationDef,
    ToolIntegrationBraveIntegrationDef,
    ToolIntegrationEmailIntegrationDef,
    ToolIntegrationSpiderIntegrationDef,
    ToolIntegrationWikipediaIntegrationDef,
    ToolIntegrationWeatherIntegrationDef,
]


class ToolSystem(TypedDict, total=False):
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


class Tool(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[ToolAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[ToolFunction]
    """Function definition"""

    integration: Optional[ToolIntegration]
    """Brave integration definition"""

    system: Optional[ToolSystem]
    """System definition"""

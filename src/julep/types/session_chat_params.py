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
    "ToolFunction",
    "ToolIntegration",
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
    type: Required[Literal["function", "integration", "system", "api_call"]]

    function: Optional[ToolChoiceNamedToolChoiceFunction]


ToolChoice: TypeAlias = Union[Literal["auto", "none"], ToolChoiceNamedToolChoice]


class ToolFunction(TypedDict, total=False):
    description: Optional[str]

    name: Optional[object]

    parameters: Optional[object]


class ToolIntegration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]
    ]

    arguments: Optional[object]

    description: Optional[str]

    method: Optional[str]

    setup: Optional[object]


class ToolSystem(TypedDict, total=False):
    call: Required[str]

    arguments: Optional[object]

    description: Optional[str]


class Tool(TypedDict, total=False):
    name: Required[str]

    function: Optional[ToolFunction]
    """Function definition"""

    integration: Optional[ToolIntegration]
    """Integration definition"""

    system: Optional[ToolSystem]
    """System definition"""

    type: Literal["function", "integration", "system", "api_call"]

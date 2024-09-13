# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .snippet import Snippet
from .._models import BaseModel

__all__ = [
    "ChatResponse",
    "Choice",
    "ChoiceSingleChatOutput",
    "ChoiceSingleChatOutputMessage",
    "ChoiceSingleChatOutputMessageContentUnionMember2",
    "ChoiceSingleChatOutputMessageContentUnionMember2Content",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModelImageURL",
    "ChoiceSingleChatOutputMessageToolCall",
    "ChoiceSingleChatOutputMessageToolCallChosenFunctionCall",
    "ChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction",
    "ChoiceSingleChatOutputMessageToolCallChosenIntegrationCall",
    "ChoiceSingleChatOutputMessageToolCallChosenSystemCall",
    "ChoiceSingleChatOutputMessageToolCallChosenAPICall",
    "ChoiceSingleChatOutputLogprobs",
    "ChoiceSingleChatOutputLogprobsContent",
    "ChoiceSingleChatOutputLogprobsContentTopLogprob",
    "ChoiceMultipleChatOutput",
    "ChoiceMultipleChatOutputMessage",
    "ChoiceMultipleChatOutputMessageContentUnionMember2",
    "ChoiceMultipleChatOutputMessageContentUnionMember2Content",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModelImageURL",
    "ChoiceMultipleChatOutputMessageToolCall",
    "ChoiceMultipleChatOutputMessageToolCallChosenFunctionCall",
    "ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction",
    "ChoiceMultipleChatOutputMessageToolCallChosenIntegrationCall",
    "ChoiceMultipleChatOutputMessageToolCallChosenSystemCall",
    "ChoiceMultipleChatOutputMessageToolCallChosenAPICall",
    "ChoiceMultipleChatOutputLogprobs",
    "ChoiceMultipleChatOutputLogprobsContent",
    "ChoiceMultipleChatOutputLogprobsContentTopLogprob",
    "Doc",
    "DocOwner",
    "Usage",
]


class ChoiceSingleChatOutputMessageContentUnionMember2Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModel(BaseModel):
    image_url: ChoiceSingleChatOutputMessageContentUnionMember2ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


ChoiceSingleChatOutputMessageContentUnionMember2: TypeAlias = Union[
    ChoiceSingleChatOutputMessageContentUnionMember2Content,
    ChoiceSingleChatOutputMessageContentUnionMember2ContentModel,
]


class ChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction(BaseModel):
    name: str


class ChoiceSingleChatOutputMessageToolCallChosenFunctionCall(BaseModel):
    id: str

    function: ChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction

    type: Optional[Literal["function"]] = None


class ChoiceSingleChatOutputMessageToolCallChosenIntegrationCall(BaseModel):
    id: str

    integration: object

    type: Optional[Literal["integration"]] = None


class ChoiceSingleChatOutputMessageToolCallChosenSystemCall(BaseModel):
    id: str

    system: object

    type: Optional[Literal["system"]] = None


class ChoiceSingleChatOutputMessageToolCallChosenAPICall(BaseModel):
    id: str

    api_call: object

    type: Optional[Literal["api_call"]] = None


ChoiceSingleChatOutputMessageToolCall: TypeAlias = Union[
    ChoiceSingleChatOutputMessageToolCallChosenFunctionCall,
    ChoiceSingleChatOutputMessageToolCallChosenIntegrationCall,
    ChoiceSingleChatOutputMessageToolCallChosenSystemCall,
    ChoiceSingleChatOutputMessageToolCallChosenAPICall,
]


class ChoiceSingleChatOutputMessage(BaseModel):
    content: Union[str, List[str], List[ChoiceSingleChatOutputMessageContentUnionMember2]]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_calls: Optional[List[ChoiceSingleChatOutputMessageToolCall]] = None


class ChoiceSingleChatOutputLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceSingleChatOutputLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceSingleChatOutputLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceSingleChatOutputLogprobs(BaseModel):
    content: Optional[List[ChoiceSingleChatOutputLogprobsContent]] = None


class ChoiceSingleChatOutput(BaseModel):
    index: int

    message: ChoiceSingleChatOutputMessage

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChoiceSingleChatOutputLogprobs] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel(BaseModel):
    image_url: ChoiceMultipleChatOutputMessageContentUnionMember2ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


ChoiceMultipleChatOutputMessageContentUnionMember2: TypeAlias = Union[
    ChoiceMultipleChatOutputMessageContentUnionMember2Content,
    ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel,
]


class ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction(BaseModel):
    name: str


class ChoiceMultipleChatOutputMessageToolCallChosenFunctionCall(BaseModel):
    id: str

    function: ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction

    type: Optional[Literal["function"]] = None


class ChoiceMultipleChatOutputMessageToolCallChosenIntegrationCall(BaseModel):
    id: str

    integration: object

    type: Optional[Literal["integration"]] = None


class ChoiceMultipleChatOutputMessageToolCallChosenSystemCall(BaseModel):
    id: str

    system: object

    type: Optional[Literal["system"]] = None


class ChoiceMultipleChatOutputMessageToolCallChosenAPICall(BaseModel):
    id: str

    api_call: object

    type: Optional[Literal["api_call"]] = None


ChoiceMultipleChatOutputMessageToolCall: TypeAlias = Union[
    ChoiceMultipleChatOutputMessageToolCallChosenFunctionCall,
    ChoiceMultipleChatOutputMessageToolCallChosenIntegrationCall,
    ChoiceMultipleChatOutputMessageToolCallChosenSystemCall,
    ChoiceMultipleChatOutputMessageToolCallChosenAPICall,
]


class ChoiceMultipleChatOutputMessage(BaseModel):
    content: Union[str, List[str], List[ChoiceMultipleChatOutputMessageContentUnionMember2]]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_calls: Optional[List[ChoiceMultipleChatOutputMessageToolCall]] = None


class ChoiceMultipleChatOutputLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceMultipleChatOutputLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceMultipleChatOutputLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceMultipleChatOutputLogprobs(BaseModel):
    content: Optional[List[ChoiceMultipleChatOutputLogprobsContent]] = None


class ChoiceMultipleChatOutput(BaseModel):
    index: int

    messages: List[ChoiceMultipleChatOutputMessage]

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChoiceMultipleChatOutputLogprobs] = None


Choice: TypeAlias = Union[ChoiceSingleChatOutput, ChoiceMultipleChatOutput]


class DocOwner(BaseModel):
    id: str

    role: Literal["user", "agent"]


class Doc(BaseModel):
    id: str

    owner: DocOwner

    snippets: List[Snippet]

    distance: Optional[float] = None

    title: Optional[str] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatResponse(BaseModel):
    id: str

    choices: List[Choice]

    created_at: datetime

    docs: Optional[List[Doc]] = None

    jobs: Optional[List[str]] = None

    usage: Optional[Usage] = None
    """Usage statistics for the completion request"""

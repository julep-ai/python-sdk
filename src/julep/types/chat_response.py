# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .log_prob_response import LogProbResponse
from .chosen_bash20241022 import ChosenBash20241022
from .chosen_function_call import ChosenFunctionCall
from .shared.doc_reference import DocReference
from .chosen_computer20241022 import ChosenComputer20241022
from .chosen_text_editor20241022 import ChosenTextEditor20241022

__all__ = [
    "ChatResponse",
    "Choice",
    "ChoiceSingleChatOutput",
    "ChoiceSingleChatOutputMessage",
    "ChoiceSingleChatOutputMessageContentUnionMember2",
    "ChoiceSingleChatOutputMessageContentUnionMember2AgentsAPIAutogenChatContentModel3",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7ImageURL",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember0",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1Source",
    "ChoiceSingleChatOutputMessageToolCall",
    "ChoiceSingleChatOutputToolCall",
    "ChoiceMultipleChatOutput",
    "ChoiceMultipleChatOutputMessage",
    "ChoiceMultipleChatOutputMessageContentUnionMember2",
    "ChoiceMultipleChatOutputMessageContentUnionMember2AgentsAPIAutogenChatContentModel3",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel7",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel7ImageURL",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember0",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1",
    "ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1Source",
    "ChoiceMultipleChatOutputMessageToolCall",
    "ChoiceMultipleChatOutputToolCall",
    "Usage",
]


class ChoiceSingleChatOutputMessageContentUnionMember2AgentsAPIAutogenChatContentModel3(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7(BaseModel):
    image_url: ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7ImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember0(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1Source(BaseModel):
    data: str

    media_type: str

    type: Optional[Literal["base64"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1(BaseModel):
    source: ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1Source

    type: Optional[Literal["image"]] = None


class ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4(BaseModel):
    content: Union[
        List[ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember0],
        List[ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1],
    ]

    tool_use_id: str

    type: Optional[Literal["tool_result"]] = None


ChoiceSingleChatOutputMessageContentUnionMember2: TypeAlias = Union[
    ChoiceSingleChatOutputMessageContentUnionMember2AgentsAPIAutogenChatContentModel3,
    ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7,
    ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4,
]

ChoiceSingleChatOutputMessageToolCall: TypeAlias = Union[
    ChosenFunctionCall, ChosenComputer20241022, ChosenTextEditor20241022, ChosenBash20241022
]


class ChoiceSingleChatOutputMessage(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]

    id: Optional[str] = None

    content: Union[str, List[str], List[ChoiceSingleChatOutputMessageContentUnionMember2], None] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[ChoiceSingleChatOutputMessageToolCall]] = None


ChoiceSingleChatOutputToolCall: TypeAlias = Union[
    ChosenFunctionCall, ChosenComputer20241022, ChosenTextEditor20241022, ChosenBash20241022
]


class ChoiceSingleChatOutput(BaseModel):
    index: int

    message: ChoiceSingleChatOutputMessage

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[LogProbResponse] = None

    tool_calls: Optional[List[ChoiceSingleChatOutputToolCall]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2AgentsAPIAutogenChatContentModel3(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel7ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel7(BaseModel):
    image_url: ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel7ImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember0(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1Source(BaseModel):
    data: str

    media_type: str

    type: Optional[Literal["base64"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1(BaseModel):
    source: ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1Source

    type: Optional[Literal["image"]] = None


class ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4(BaseModel):
    content: Union[
        List[ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember0],
        List[ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1],
    ]

    tool_use_id: str

    type: Optional[Literal["tool_result"]] = None


ChoiceMultipleChatOutputMessageContentUnionMember2: TypeAlias = Union[
    ChoiceMultipleChatOutputMessageContentUnionMember2AgentsAPIAutogenChatContentModel3,
    ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel7,
    ChoiceMultipleChatOutputMessageContentUnionMember2ContentModel4,
]

ChoiceMultipleChatOutputMessageToolCall: TypeAlias = Union[
    ChosenFunctionCall, ChosenComputer20241022, ChosenTextEditor20241022, ChosenBash20241022
]


class ChoiceMultipleChatOutputMessage(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]

    id: Optional[str] = None

    content: Union[str, List[str], List[ChoiceMultipleChatOutputMessageContentUnionMember2], None] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[ChoiceMultipleChatOutputMessageToolCall]] = None


ChoiceMultipleChatOutputToolCall: TypeAlias = Union[
    ChosenFunctionCall, ChosenComputer20241022, ChosenTextEditor20241022, ChosenBash20241022
]


class ChoiceMultipleChatOutput(BaseModel):
    index: int

    messages: List[ChoiceMultipleChatOutputMessage]

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[LogProbResponse] = None

    tool_calls: Optional[List[ChoiceMultipleChatOutputToolCall]] = None


Choice: TypeAlias = Union[ChoiceSingleChatOutput, ChoiceMultipleChatOutput]


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatResponse(BaseModel):
    id: str

    choices: List[Choice]

    created_at: datetime

    docs: Optional[List[DocReference]] = None

    jobs: Optional[List[str]] = None

    usage: Optional[Usage] = None
    """Usage statistics for the completion request"""

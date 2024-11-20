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
    "ChoiceSingleChatOutputMessageContentUnionMember2AgentsAPIAutogenChatContentModel3",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel7ImageURL",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember0",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1",
    "ChoiceSingleChatOutputMessageContentUnionMember2ContentModel4ContentUnionMember1Source",
    "ChoiceSingleChatOutputMessageToolCall",
    "ChoiceSingleChatOutputMessageToolCallChosenFunctionCall",
    "ChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction",
    "ChoiceSingleChatOutputMessageToolCallChosenFunctionCallBash20241022",
    "ChoiceSingleChatOutputMessageToolCallChosenFunctionCallComputer20241022",
    "ChoiceSingleChatOutputMessageToolCallChosenFunctionCallTextEditor20241022",
    "ChoiceSingleChatOutputMessageToolCallChosenComputer20241022",
    "ChoiceSingleChatOutputMessageToolCallChosenTextEditor20241022",
    "ChoiceSingleChatOutputMessageToolCallChosenBash20241022",
    "ChoiceSingleChatOutputLogprobs",
    "ChoiceSingleChatOutputLogprobsContent",
    "ChoiceSingleChatOutputLogprobsContentTopLogprob",
    "ChoiceSingleChatOutputToolCall",
    "ChoiceSingleChatOutputToolCallChosenFunctionCall",
    "ChoiceSingleChatOutputToolCallChosenFunctionCallFunction",
    "ChoiceSingleChatOutputToolCallChosenFunctionCallBash20241022",
    "ChoiceSingleChatOutputToolCallChosenFunctionCallComputer20241022",
    "ChoiceSingleChatOutputToolCallChosenFunctionCallTextEditor20241022",
    "ChoiceSingleChatOutputToolCallChosenComputer20241022",
    "ChoiceSingleChatOutputToolCallChosenTextEditor20241022",
    "ChoiceSingleChatOutputToolCallChosenBash20241022",
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
    "ChoiceMultipleChatOutputMessageToolCallChosenFunctionCall",
    "ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction",
    "ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallBash20241022",
    "ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallComputer20241022",
    "ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallTextEditor20241022",
    "ChoiceMultipleChatOutputMessageToolCallChosenComputer20241022",
    "ChoiceMultipleChatOutputMessageToolCallChosenTextEditor20241022",
    "ChoiceMultipleChatOutputMessageToolCallChosenBash20241022",
    "ChoiceMultipleChatOutputLogprobs",
    "ChoiceMultipleChatOutputLogprobsContent",
    "ChoiceMultipleChatOutputLogprobsContentTopLogprob",
    "ChoiceMultipleChatOutputToolCall",
    "ChoiceMultipleChatOutputToolCallChosenFunctionCall",
    "ChoiceMultipleChatOutputToolCallChosenFunctionCallFunction",
    "ChoiceMultipleChatOutputToolCallChosenFunctionCallBash20241022",
    "ChoiceMultipleChatOutputToolCallChosenFunctionCallComputer20241022",
    "ChoiceMultipleChatOutputToolCallChosenFunctionCallTextEditor20241022",
    "ChoiceMultipleChatOutputToolCallChosenComputer20241022",
    "ChoiceMultipleChatOutputToolCallChosenTextEditor20241022",
    "ChoiceMultipleChatOutputToolCallChosenBash20241022",
    "Doc",
    "DocOwner",
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


class ChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ChoiceSingleChatOutputMessageToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ChoiceSingleChatOutputMessageToolCallChosenFunctionCallComputer20241022(BaseModel):
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


class ChoiceSingleChatOutputMessageToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceSingleChatOutputMessageToolCallChosenFunctionCall(BaseModel):
    function: ChoiceSingleChatOutputMessageToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ChoiceSingleChatOutputMessageToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ChoiceSingleChatOutputMessageToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ChoiceSingleChatOutputMessageToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ChoiceSingleChatOutputMessageToolCallChosenComputer20241022(BaseModel):
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


class ChoiceSingleChatOutputMessageToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceSingleChatOutputMessageToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


ChoiceSingleChatOutputMessageToolCall: TypeAlias = Union[
    ChoiceSingleChatOutputMessageToolCallChosenFunctionCall,
    ChoiceSingleChatOutputMessageToolCallChosenComputer20241022,
    ChoiceSingleChatOutputMessageToolCallChosenTextEditor20241022,
    ChoiceSingleChatOutputMessageToolCallChosenBash20241022,
]


class ChoiceSingleChatOutputMessage(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]

    id: Optional[str] = None

    content: Union[str, List[str], List[ChoiceSingleChatOutputMessageContentUnionMember2], None] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

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


class ChoiceSingleChatOutputToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ChoiceSingleChatOutputToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ChoiceSingleChatOutputToolCallChosenFunctionCallComputer20241022(BaseModel):
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


class ChoiceSingleChatOutputToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceSingleChatOutputToolCallChosenFunctionCall(BaseModel):
    function: ChoiceSingleChatOutputToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ChoiceSingleChatOutputToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ChoiceSingleChatOutputToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ChoiceSingleChatOutputToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ChoiceSingleChatOutputToolCallChosenComputer20241022(BaseModel):
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


class ChoiceSingleChatOutputToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceSingleChatOutputToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


ChoiceSingleChatOutputToolCall: TypeAlias = Union[
    ChoiceSingleChatOutputToolCallChosenFunctionCall,
    ChoiceSingleChatOutputToolCallChosenComputer20241022,
    ChoiceSingleChatOutputToolCallChosenTextEditor20241022,
    ChoiceSingleChatOutputToolCallChosenBash20241022,
]


class ChoiceSingleChatOutput(BaseModel):
    index: int

    message: ChoiceSingleChatOutputMessage

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChoiceSingleChatOutputLogprobs] = None

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


class ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallComputer20241022(BaseModel):
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


class ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceMultipleChatOutputMessageToolCallChosenFunctionCall(BaseModel):
    function: ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ChoiceMultipleChatOutputMessageToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ChoiceMultipleChatOutputMessageToolCallChosenComputer20241022(BaseModel):
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


class ChoiceMultipleChatOutputMessageToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceMultipleChatOutputMessageToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


ChoiceMultipleChatOutputMessageToolCall: TypeAlias = Union[
    ChoiceMultipleChatOutputMessageToolCallChosenFunctionCall,
    ChoiceMultipleChatOutputMessageToolCallChosenComputer20241022,
    ChoiceMultipleChatOutputMessageToolCallChosenTextEditor20241022,
    ChoiceMultipleChatOutputMessageToolCallChosenBash20241022,
]


class ChoiceMultipleChatOutputMessage(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]

    id: Optional[str] = None

    content: Union[str, List[str], List[ChoiceMultipleChatOutputMessageContentUnionMember2], None] = None

    created_at: Optional[datetime] = None

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

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


class ChoiceMultipleChatOutputToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ChoiceMultipleChatOutputToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ChoiceMultipleChatOutputToolCallChosenFunctionCallComputer20241022(BaseModel):
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


class ChoiceMultipleChatOutputToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceMultipleChatOutputToolCallChosenFunctionCall(BaseModel):
    function: ChoiceMultipleChatOutputToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ChoiceMultipleChatOutputToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ChoiceMultipleChatOutputToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ChoiceMultipleChatOutputToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ChoiceMultipleChatOutputToolCallChosenComputer20241022(BaseModel):
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


class ChoiceMultipleChatOutputToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChoiceMultipleChatOutputToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


ChoiceMultipleChatOutputToolCall: TypeAlias = Union[
    ChoiceMultipleChatOutputToolCallChosenFunctionCall,
    ChoiceMultipleChatOutputToolCallChosenComputer20241022,
    ChoiceMultipleChatOutputToolCallChosenTextEditor20241022,
    ChoiceMultipleChatOutputToolCallChosenBash20241022,
]


class ChoiceMultipleChatOutput(BaseModel):
    index: int

    messages: List[ChoiceMultipleChatOutputMessage]

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChoiceMultipleChatOutputLogprobs] = None

    tool_calls: Optional[List[ChoiceMultipleChatOutputToolCall]] = None


Choice: TypeAlias = Union[ChoiceSingleChatOutput, ChoiceMultipleChatOutput]


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

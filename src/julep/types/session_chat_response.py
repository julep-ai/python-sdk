# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .snippet import Snippet
from .._models import BaseModel
from .chat_response import ChatResponse

__all__ = [
    "SessionChatResponse",
    "ChunkChatResponse",
    "ChunkChatResponseChoice",
    "ChunkChatResponseChoiceDelta",
    "ChunkChatResponseChoiceDeltaContentUnionMember2",
    "ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel1",
    "ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel7",
    "ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel7ImageURL",
    "ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2",
    "ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember0",
    "ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember1",
    "ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember1Source",
    "ChunkChatResponseChoiceDeltaToolCall",
    "ChunkChatResponseChoiceDeltaToolCallChosenFunctionCall",
    "ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallFunction",
    "ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallBash20241022",
    "ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallComputer20241022",
    "ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallTextEditor20241022",
    "ChunkChatResponseChoiceDeltaToolCallChosenComputer20241022",
    "ChunkChatResponseChoiceDeltaToolCallChosenTextEditor20241022",
    "ChunkChatResponseChoiceDeltaToolCallChosenBash20241022",
    "ChunkChatResponseChoiceLogprobs",
    "ChunkChatResponseChoiceLogprobsContent",
    "ChunkChatResponseChoiceLogprobsContentTopLogprob",
    "ChunkChatResponseChoiceToolCall",
    "ChunkChatResponseChoiceToolCallChosenFunctionCall",
    "ChunkChatResponseChoiceToolCallChosenFunctionCallFunction",
    "ChunkChatResponseChoiceToolCallChosenFunctionCallBash20241022",
    "ChunkChatResponseChoiceToolCallChosenFunctionCallComputer20241022",
    "ChunkChatResponseChoiceToolCallChosenFunctionCallTextEditor20241022",
    "ChunkChatResponseChoiceToolCallChosenComputer20241022",
    "ChunkChatResponseChoiceToolCallChosenTextEditor20241022",
    "ChunkChatResponseChoiceToolCallChosenBash20241022",
    "ChunkChatResponseDoc",
    "ChunkChatResponseDocOwner",
    "ChunkChatResponseUsage",
]


class ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel1(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel7ImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel7(BaseModel):
    image_url: ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel7ImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember0(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember1Source(
    BaseModel
):
    data: str

    media_type: str

    type: Optional[Literal["base64"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember1(BaseModel):
    source: ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember1Source

    type: Optional[Literal["image"]] = None


class ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2(BaseModel):
    content: Union[
        List[ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember0],
        List[ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2ContentUnionMember1],
    ]

    tool_use_id: str

    type: Optional[Literal["tool_result"]] = None


ChunkChatResponseChoiceDeltaContentUnionMember2: TypeAlias = Union[
    ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel1,
    ChunkChatResponseChoiceDeltaContentUnionMember2ContentModel7,
    ChunkChatResponseChoiceDeltaContentUnionMember2AgentsAPIAutogenChatContentModel2,
]


class ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallComputer20241022(BaseModel):
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


class ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChunkChatResponseChoiceDeltaToolCallChosenFunctionCall(BaseModel):
    function: ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ChunkChatResponseChoiceDeltaToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ChunkChatResponseChoiceDeltaToolCallChosenComputer20241022(BaseModel):
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


class ChunkChatResponseChoiceDeltaToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChunkChatResponseChoiceDeltaToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


ChunkChatResponseChoiceDeltaToolCall: TypeAlias = Union[
    ChunkChatResponseChoiceDeltaToolCallChosenFunctionCall,
    ChunkChatResponseChoiceDeltaToolCallChosenComputer20241022,
    ChunkChatResponseChoiceDeltaToolCallChosenTextEditor20241022,
    ChunkChatResponseChoiceDeltaToolCallChosenBash20241022,
]


class ChunkChatResponseChoiceDelta(BaseModel):
    role: Literal["user", "assistant", "system", "tool"]

    content: Union[str, List[str], List[ChunkChatResponseChoiceDeltaContentUnionMember2], None] = None

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None

    tool_call_id: Optional[str] = None

    tool_calls: Optional[List[ChunkChatResponseChoiceDeltaToolCall]] = None


class ChunkChatResponseChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChunkChatResponseChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChunkChatResponseChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChunkChatResponseChoiceLogprobs(BaseModel):
    content: Optional[List[ChunkChatResponseChoiceLogprobsContent]] = None


class ChunkChatResponseChoiceToolCallChosenFunctionCallFunction(BaseModel):
    name: str

    arguments: Optional[str] = None


class ChunkChatResponseChoiceToolCallChosenFunctionCallBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


class ChunkChatResponseChoiceToolCallChosenFunctionCallComputer20241022(BaseModel):
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


class ChunkChatResponseChoiceToolCallChosenFunctionCallTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChunkChatResponseChoiceToolCallChosenFunctionCall(BaseModel):
    function: ChunkChatResponseChoiceToolCallChosenFunctionCallFunction

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ChunkChatResponseChoiceToolCallChosenFunctionCallBash20241022] = None

    computer_20241022: Optional[ChunkChatResponseChoiceToolCallChosenFunctionCallComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ChunkChatResponseChoiceToolCallChosenFunctionCallTextEditor20241022] = None

    type: Optional[Literal["function"]] = None


class ChunkChatResponseChoiceToolCallChosenComputer20241022(BaseModel):
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


class ChunkChatResponseChoiceToolCallChosenTextEditor20241022(BaseModel):
    command: Literal["str_replace", "insert", "view", "undo_edit"]

    path: str

    file_text: Optional[str] = None

    insert_line: Optional[int] = None

    new_str: Optional[str] = None

    old_str: Optional[str] = None

    view_range: Optional[List[int]] = None


class ChunkChatResponseChoiceToolCallChosenBash20241022(BaseModel):
    command: Optional[str] = None

    restart: Optional[bool] = None


ChunkChatResponseChoiceToolCall: TypeAlias = Union[
    ChunkChatResponseChoiceToolCallChosenFunctionCall,
    ChunkChatResponseChoiceToolCallChosenComputer20241022,
    ChunkChatResponseChoiceToolCallChosenTextEditor20241022,
    ChunkChatResponseChoiceToolCallChosenBash20241022,
]


class ChunkChatResponseChoice(BaseModel):
    delta: ChunkChatResponseChoiceDelta
    """The message generated by the model"""

    index: int

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChunkChatResponseChoiceLogprobs] = None

    tool_calls: Optional[List[ChunkChatResponseChoiceToolCall]] = None


class ChunkChatResponseDocOwner(BaseModel):
    id: str

    role: Literal["user", "agent"]


class ChunkChatResponseDoc(BaseModel):
    id: str

    owner: ChunkChatResponseDocOwner

    snippet: Snippet

    distance: Optional[float] = None

    metadata: Optional[object] = None

    title: Optional[str] = None


class ChunkChatResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChunkChatResponse(BaseModel):
    id: str

    choices: List[ChunkChatResponseChoice]

    created_at: datetime

    docs: Optional[List[ChunkChatResponseDoc]] = None

    jobs: Optional[List[str]] = None

    usage: Optional[ChunkChatResponseUsage] = None
    """Usage statistics for the completion request"""


SessionChatResponse: TypeAlias = Union[ChunkChatResponse, ChatResponse]

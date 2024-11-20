# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "MessageParam",
    "ContentUnionMember2",
    "ContentUnionMember2Content",
    "ContentUnionMember2ContentModel7",
    "ContentUnionMember2ContentModel7ImageURL",
    "ContentUnionMember2AgentsAPIAutogenChatContentModel",
    "ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember0",
    "ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember1",
    "ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember1Source",
    "ToolCall",
    "ToolCallChosenFunctionCall",
    "ToolCallChosenFunctionCallFunction",
    "ToolCallChosenFunctionCallBash20241022",
    "ToolCallChosenFunctionCallComputer20241022",
    "ToolCallChosenFunctionCallTextEditor20241022",
    "ToolCallChosenComputer20241022",
    "ToolCallChosenTextEditor20241022",
    "ToolCallChosenBash20241022",
]


class ContentUnionMember2Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class ContentUnionMember2ContentModel7ImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class ContentUnionMember2ContentModel7(TypedDict, total=False):
    image_url: Required[ContentUnionMember2ContentModel7ImageURL]
    """The image URL"""

    type: Literal["image_url"]


class ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember1Source(TypedDict, total=False):
    data: Required[str]

    media_type: Required[str]

    type: Literal["base64"]


class ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember1(TypedDict, total=False):
    source: Required[ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember1Source]

    type: Literal["image"]


class ContentUnionMember2AgentsAPIAutogenChatContentModel(TypedDict, total=False):
    content: Required[
        Union[
            Iterable[ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember0],
            Iterable[ContentUnionMember2AgentsAPIAutogenChatContentModelContentUnionMember1],
        ]
    ]

    tool_use_id: Required[str]

    type: Literal["tool_result"]


ContentUnionMember2: TypeAlias = Union[
    ContentUnionMember2Content, ContentUnionMember2ContentModel7, ContentUnionMember2AgentsAPIAutogenChatContentModel
]


class ToolCallChosenFunctionCallFunction(TypedDict, total=False):
    name: Required[str]

    arguments: Optional[str]


class ToolCallChosenFunctionCallBash20241022(TypedDict, total=False):
    command: Optional[str]

    restart: bool


class ToolCallChosenFunctionCallComputer20241022(TypedDict, total=False):
    action: Required[
        Literal[
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
    ]

    coordinate: Optional[Iterable[int]]

    text: Optional[str]


class ToolCallChosenFunctionCallTextEditor20241022(TypedDict, total=False):
    command: Required[Literal["str_replace", "insert", "view", "undo_edit"]]

    path: Required[str]

    file_text: Optional[str]

    insert_line: Optional[int]

    new_str: Optional[str]

    old_str: Optional[str]

    view_range: Optional[Iterable[int]]


class ToolCallChosenFunctionCall(TypedDict, total=False):
    function: Required[ToolCallChosenFunctionCallFunction]

    api_call: Optional[object]

    bash_20241022: Optional[ToolCallChosenFunctionCallBash20241022]

    computer_20241022: Optional[ToolCallChosenFunctionCallComputer20241022]

    integration: Optional[object]

    system: Optional[object]

    text_editor_20241022: Optional[ToolCallChosenFunctionCallTextEditor20241022]

    type: Literal["function"]


class ToolCallChosenComputer20241022(TypedDict, total=False):
    action: Required[
        Literal[
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
    ]

    coordinate: Optional[Iterable[int]]

    text: Optional[str]


class ToolCallChosenTextEditor20241022(TypedDict, total=False):
    command: Required[Literal["str_replace", "insert", "view", "undo_edit"]]

    path: Required[str]

    file_text: Optional[str]

    insert_line: Optional[int]

    new_str: Optional[str]

    old_str: Optional[str]

    view_range: Optional[Iterable[int]]


class ToolCallChosenBash20241022(TypedDict, total=False):
    command: Optional[str]

    restart: bool


ToolCall: TypeAlias = Union[
    ToolCallChosenFunctionCall,
    ToolCallChosenComputer20241022,
    ToolCallChosenTextEditor20241022,
    ToolCallChosenBash20241022,
]

_MessageParamReservedKeywords = TypedDict(
    "_MessageParamReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MessageParam(_MessageParamReservedKeywords, total=False):
    role: Required[Literal["user", "assistant", "system", "tool"]]

    content: Union[str, List[str], Iterable[ContentUnionMember2], None]

    name: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[ToolCall]]

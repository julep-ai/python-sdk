# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .tool_param import ToolParam
from .chat_settings_param import ChatSettingsParam

__all__ = [
    "TaskCreateParams",
    "Main",
    "MainEvaluateStep",
    "MainToolCallStep",
    "MainPromptStepInput",
    "MainPromptStepInputPromptUnionMember0",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainPromptStepInputToolChoice",
    "MainPromptStepInputToolChoiceNamedToolChoice",
    "MainPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainPromptStepInputToolsUnionMember1",
    "MainPromptStepInputToolsUnionMember1ToolRef",
    "MainPromptStepInputToolsUnionMember1ToolRefRef",
    "MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainPromptStepInputToolsUnionMember1CreateToolRequest",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestAPICall",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestFunction",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestIntegration",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestSystem",
    "MainGetStep",
    "MainSetStep",
    "MainLogStep",
    "MainYieldStep",
    "MainReturnStep",
    "MainSleepStep",
    "MainSleepStepSleep",
    "MainErrorWorkflowStep",
    "MainWaitForInputStep",
    "MainWaitForInputStepWaitForInput",
    "MainIfElseWorkflowStepInput",
    "MainIfElseWorkflowStepInputThen",
    "MainIfElseWorkflowStepInputThenEvaluateStep",
    "MainIfElseWorkflowStepInputThenToolCallStep",
    "MainIfElseWorkflowStepInputThenPromptStepInput",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolChoice",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoice",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequest",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestAPICall",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestFunction",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestIntegration",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestSystem",
    "MainIfElseWorkflowStepInputThenGetStep",
    "MainIfElseWorkflowStepInputThenSetStep",
    "MainIfElseWorkflowStepInputThenLogStep",
    "MainIfElseWorkflowStepInputThenYieldStep",
    "MainIfElseWorkflowStepInputThenReturnStep",
    "MainIfElseWorkflowStepInputThenSleepStep",
    "MainIfElseWorkflowStepInputThenSleepStepSleep",
    "MainIfElseWorkflowStepInputThenErrorWorkflowStep",
    "MainIfElseWorkflowStepInputThenWaitForInputStep",
    "MainIfElseWorkflowStepInputThenWaitForInputStepWaitForInput",
    "MainIfElseWorkflowStepInputElse",
    "MainIfElseWorkflowStepInputElseEvaluateStep",
    "MainIfElseWorkflowStepInputElseToolCallStep",
    "MainIfElseWorkflowStepInputElsePromptStepInput",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolChoice",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoice",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequest",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestAPICall",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestFunction",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestIntegration",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestSystem",
    "MainIfElseWorkflowStepInputElseGetStep",
    "MainIfElseWorkflowStepInputElseSetStep",
    "MainIfElseWorkflowStepInputElseLogStep",
    "MainIfElseWorkflowStepInputElseYieldStep",
    "MainIfElseWorkflowStepInputElseReturnStep",
    "MainIfElseWorkflowStepInputElseSleepStep",
    "MainIfElseWorkflowStepInputElseSleepStepSleep",
    "MainIfElseWorkflowStepInputElseErrorWorkflowStep",
    "MainIfElseWorkflowStepInputElseWaitForInputStep",
    "MainIfElseWorkflowStepInputElseWaitForInputStepWaitForInput",
    "MainSwitchStepInput",
    "MainSwitchStepInputSwitch",
    "MainSwitchStepInputSwitchThen",
    "MainSwitchStepInputSwitchThenEvaluateStep",
    "MainSwitchStepInputSwitchThenToolCallStep",
    "MainSwitchStepInputSwitchThenPromptStepInput",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainSwitchStepInputSwitchThenPromptStepInputToolChoice",
    "MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoice",
    "MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequest",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestAPICall",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestFunction",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestIntegration",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestSystem",
    "MainSwitchStepInputSwitchThenGetStep",
    "MainSwitchStepInputSwitchThenSetStep",
    "MainSwitchStepInputSwitchThenLogStep",
    "MainSwitchStepInputSwitchThenYieldStep",
    "MainSwitchStepInputSwitchThenReturnStep",
    "MainSwitchStepInputSwitchThenSleepStep",
    "MainSwitchStepInputSwitchThenSleepStepSleep",
    "MainSwitchStepInputSwitchThenErrorWorkflowStep",
    "MainSwitchStepInputSwitchThenWaitForInputStep",
    "MainSwitchStepInputSwitchThenWaitForInputStepWaitForInput",
    "MainForeachStepInput",
    "MainForeachStepInputForeach",
    "MainForeachStepInputForeachDo",
    "MainForeachStepInputForeachDoWaitForInputStep",
    "MainForeachStepInputForeachDoWaitForInputStepWaitForInput",
    "MainForeachStepInputForeachDoEvaluateStep",
    "MainForeachStepInputForeachDoToolCallStep",
    "MainForeachStepInputForeachDoPromptStepInput",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainForeachStepInputForeachDoPromptStepInputToolChoice",
    "MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoice",
    "MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequest",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestAPICall",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestFunction",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestIntegration",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestSystem",
    "MainForeachStepInputForeachDoGetStep",
    "MainForeachStepInputForeachDoSetStep",
    "MainForeachStepInputForeachDoLogStep",
    "MainForeachStepInputForeachDoYieldStep",
    "MainParallelStepInput",
    "MainParallelStepInputParallel",
    "MainParallelStepInputParallelEvaluateStep",
    "MainParallelStepInputParallelToolCallStep",
    "MainParallelStepInputParallelPromptStepInput",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainParallelStepInputParallelPromptStepInputToolChoice",
    "MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoice",
    "MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequest",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestAPICall",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestFunction",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestIntegration",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestSystem",
    "MainParallelStepInputParallelGetStep",
    "MainParallelStepInputParallelSetStep",
    "MainParallelStepInputParallelLogStep",
    "MainParallelStepInputParallelYieldStep",
    "MainMainInput",
    "MainMainInputMap",
    "MainMainInputMapEvaluateStep",
    "MainMainInputMapToolCallStep",
    "MainMainInputMapPromptStepInput",
    "MainMainInputMapPromptStepInputPromptUnionMember0",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainMainInputMapPromptStepInputToolChoice",
    "MainMainInputMapPromptStepInputToolChoiceNamedToolChoice",
    "MainMainInputMapPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainMainInputMapPromptStepInputToolsUnionMember1",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRef",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRef",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequest",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestAPICall",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestFunction",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestIntegration",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestSystem",
    "MainMainInputMapGetStep",
    "MainMainInputMapSetStep",
    "MainMainInputMapLogStep",
    "MainMainInputMapYieldStep",
]


class TaskCreateParams(TypedDict, total=False):
    main: Required[Iterable[Main]]

    name: Required[str]

    description: str

    inherit_tools: bool

    input_schema: Optional[object]

    metadata: Optional[object]

    tools: Iterable[ToolParam]


class MainEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(TypedDict, total=False):
    image_url: Required[MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL]
    """The image URL"""

    type: Literal["image_url"]


MainPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainPromptStepInputPromptUnionMember0(_MainPromptStepInputPromptUnionMember0ReservedKeywords, total=False):
    content: Required[Union[List[str], Iterable[MainPromptStepInputPromptUnionMember0ContentUnionMember1], str]]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainPromptStepInputToolChoiceNamedToolChoiceFunction]


MainPromptStepInputToolChoice: TypeAlias = Union[Literal["auto", "none"], MainPromptStepInputToolChoiceNamedToolChoice]


class MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainPromptStepInputToolsUnionMember1CreateToolRequestAPICall(TypedDict, total=False):
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


class MainPromptStepInputToolsUnionMember1CreateToolRequestFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainPromptStepInputToolsUnionMember1CreateToolRequestIntegration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class MainPromptStepInputToolsUnionMember1CreateToolRequestSystem(TypedDict, total=False):
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


class MainPromptStepInputToolsUnionMember1CreateToolRequest(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestFunction]
    """Function definition"""

    integration: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestIntegration]
    """Integration definition"""

    system: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestSystem]
    """System definition"""


MainPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainPromptStepInputToolsUnionMember1ToolRef, MainPromptStepInputToolsUnionMember1CreateToolRequest
]


class MainPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainGetStep(TypedDict, total=False):
    get: Required[str]


class MainSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainLogStep(TypedDict, total=False):
    log: Required[str]


class MainYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainReturnStepReservedKeywords = TypedDict(
    "_MainReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainReturnStep(_MainReturnStepReservedKeywords, total=False):
    pass


class MainSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainSleepStep(TypedDict, total=False):
    sleep: Required[MainSleepStepSleep]


class MainErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainWaitForInputStepWaitForInput]


class MainIfElseWorkflowStepInputThenEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputThenToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1Content(
    TypedDict, total=False
):
    text: Required[str]

    type: Literal["text"]


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0(
    _MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str],
            Iterable[MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1],
            str,
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoiceFunction]


MainIfElseWorkflowStepInputThenPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoice
]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestAPICall(TypedDict, total=False):
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


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestIntegration(
    TypedDict, total=False
):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestSystem(TypedDict, total=False):
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


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequest(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestFunction]
    """Function definition"""

    integration: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestIntegration]
    """Integration definition"""

    system: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestSystem]
    """System definition"""


MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequest,
]


class MainIfElseWorkflowStepInputThenPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainIfElseWorkflowStepInputThenGetStep(TypedDict, total=False):
    get: Required[str]


class MainIfElseWorkflowStepInputThenSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputThenLogStep(TypedDict, total=False):
    log: Required[str]


class MainIfElseWorkflowStepInputThenYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainIfElseWorkflowStepInputThenReturnStepReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputThenReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainIfElseWorkflowStepInputThenReturnStep(
    _MainIfElseWorkflowStepInputThenReturnStepReservedKeywords, total=False
):
    pass


class MainIfElseWorkflowStepInputThenSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainIfElseWorkflowStepInputThenSleepStep(TypedDict, total=False):
    sleep: Required[MainIfElseWorkflowStepInputThenSleepStepSleep]


class MainIfElseWorkflowStepInputThenErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainIfElseWorkflowStepInputThenWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputThenWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainIfElseWorkflowStepInputThenWaitForInputStepWaitForInput]


MainIfElseWorkflowStepInputThen: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenEvaluateStep,
    MainIfElseWorkflowStepInputThenToolCallStep,
    MainIfElseWorkflowStepInputThenPromptStepInput,
    MainIfElseWorkflowStepInputThenGetStep,
    MainIfElseWorkflowStepInputThenSetStep,
    MainIfElseWorkflowStepInputThenLogStep,
    MainIfElseWorkflowStepInputThenYieldStep,
    MainIfElseWorkflowStepInputThenReturnStep,
    MainIfElseWorkflowStepInputThenSleepStep,
    MainIfElseWorkflowStepInputThenErrorWorkflowStep,
    MainIfElseWorkflowStepInputThenWaitForInputStep,
]


class MainIfElseWorkflowStepInputElseEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputElseToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1Content(
    TypedDict, total=False
):
    text: Required[str]

    type: Literal["text"]


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0(
    _MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str],
            Iterable[MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1],
            str,
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoiceFunction]


MainIfElseWorkflowStepInputElsePromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoice
]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestAPICall(TypedDict, total=False):
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


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestIntegration(
    TypedDict, total=False
):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestSystem(TypedDict, total=False):
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


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequest(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestFunction]
    """Function definition"""

    integration: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestIntegration]
    """Integration definition"""

    system: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestSystem]
    """System definition"""


MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequest,
]


class MainIfElseWorkflowStepInputElsePromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainIfElseWorkflowStepInputElseGetStep(TypedDict, total=False):
    get: Required[str]


class MainIfElseWorkflowStepInputElseSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputElseLogStep(TypedDict, total=False):
    log: Required[str]


class MainIfElseWorkflowStepInputElseYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainIfElseWorkflowStepInputElseReturnStepReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputElseReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainIfElseWorkflowStepInputElseReturnStep(
    _MainIfElseWorkflowStepInputElseReturnStepReservedKeywords, total=False
):
    pass


class MainIfElseWorkflowStepInputElseSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainIfElseWorkflowStepInputElseSleepStep(TypedDict, total=False):
    sleep: Required[MainIfElseWorkflowStepInputElseSleepStepSleep]


class MainIfElseWorkflowStepInputElseErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainIfElseWorkflowStepInputElseWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputElseWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainIfElseWorkflowStepInputElseWaitForInputStepWaitForInput]


MainIfElseWorkflowStepInputElse: TypeAlias = Union[
    MainIfElseWorkflowStepInputElseEvaluateStep,
    MainIfElseWorkflowStepInputElseToolCallStep,
    MainIfElseWorkflowStepInputElsePromptStepInput,
    MainIfElseWorkflowStepInputElseGetStep,
    MainIfElseWorkflowStepInputElseSetStep,
    MainIfElseWorkflowStepInputElseLogStep,
    MainIfElseWorkflowStepInputElseYieldStep,
    MainIfElseWorkflowStepInputElseReturnStep,
    MainIfElseWorkflowStepInputElseSleepStep,
    MainIfElseWorkflowStepInputElseErrorWorkflowStep,
    MainIfElseWorkflowStepInputElseWaitForInputStep,
]

_MainIfElseWorkflowStepInputReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputReservedKeywords",
    {
        "if": str,
        "else": Optional[MainIfElseWorkflowStepInputElse],
    },
    total=False,
)


class MainIfElseWorkflowStepInput(_MainIfElseWorkflowStepInputReservedKeywords, total=False):
    then: Required[MainIfElseWorkflowStepInputThen]


class MainSwitchStepInputSwitchThenEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainSwitchStepInputSwitchThenToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0(
    _MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str], Iterable[MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1], str
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoiceFunction]


MainSwitchStepInputSwitchThenPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoice
]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestAPICall(TypedDict, total=False):
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


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestIntegration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestSystem(TypedDict, total=False):
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


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequest(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestFunction]
    """Function definition"""

    integration: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestIntegration]
    """Integration definition"""

    system: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestSystem]
    """System definition"""


MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRef,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequest,
]


class MainSwitchStepInputSwitchThenPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainSwitchStepInputSwitchThenGetStep(TypedDict, total=False):
    get: Required[str]


class MainSwitchStepInputSwitchThenSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainSwitchStepInputSwitchThenLogStep(TypedDict, total=False):
    log: Required[str]


class MainSwitchStepInputSwitchThenYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainSwitchStepInputSwitchThenReturnStepReservedKeywords = TypedDict(
    "_MainSwitchStepInputSwitchThenReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainSwitchStepInputSwitchThenReturnStep(_MainSwitchStepInputSwitchThenReturnStepReservedKeywords, total=False):
    pass


class MainSwitchStepInputSwitchThenSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainSwitchStepInputSwitchThenSleepStep(TypedDict, total=False):
    sleep: Required[MainSwitchStepInputSwitchThenSleepStepSleep]


class MainSwitchStepInputSwitchThenErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainSwitchStepInputSwitchThenWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainSwitchStepInputSwitchThenWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainSwitchStepInputSwitchThenWaitForInputStepWaitForInput]


MainSwitchStepInputSwitchThen: TypeAlias = Union[
    MainSwitchStepInputSwitchThenEvaluateStep,
    MainSwitchStepInputSwitchThenToolCallStep,
    MainSwitchStepInputSwitchThenPromptStepInput,
    MainSwitchStepInputSwitchThenGetStep,
    MainSwitchStepInputSwitchThenSetStep,
    MainSwitchStepInputSwitchThenLogStep,
    MainSwitchStepInputSwitchThenYieldStep,
    MainSwitchStepInputSwitchThenReturnStep,
    MainSwitchStepInputSwitchThenSleepStep,
    MainSwitchStepInputSwitchThenErrorWorkflowStep,
    MainSwitchStepInputSwitchThenWaitForInputStep,
]


class MainSwitchStepInputSwitch(TypedDict, total=False):
    case: Required[Union[Literal["_"], str]]

    then: Required[MainSwitchStepInputSwitchThen]


class MainSwitchStepInput(TypedDict, total=False):
    switch: Required[Iterable[MainSwitchStepInputSwitch]]


class MainForeachStepInputForeachDoWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainForeachStepInputForeachDoWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainForeachStepInputForeachDoWaitForInputStepWaitForInput]


class MainForeachStepInputForeachDoEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainForeachStepInputForeachDoToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0(
    _MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str], Iterable[MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1], str
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoiceFunction]


MainForeachStepInputForeachDoPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoice
]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestAPICall(TypedDict, total=False):
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


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestIntegration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestSystem(TypedDict, total=False):
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


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequest(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestFunction]
    """Function definition"""

    integration: Optional[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestIntegration]
    """Integration definition"""

    system: Optional[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestSystem]
    """System definition"""


MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRef,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequest,
]


class MainForeachStepInputForeachDoPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainForeachStepInputForeachDoPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainForeachStepInputForeachDoGetStep(TypedDict, total=False):
    get: Required[str]


class MainForeachStepInputForeachDoSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainForeachStepInputForeachDoLogStep(TypedDict, total=False):
    log: Required[str]


class MainForeachStepInputForeachDoYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


MainForeachStepInputForeachDo: TypeAlias = Union[
    MainForeachStepInputForeachDoWaitForInputStep,
    MainForeachStepInputForeachDoEvaluateStep,
    MainForeachStepInputForeachDoToolCallStep,
    MainForeachStepInputForeachDoPromptStepInput,
    MainForeachStepInputForeachDoGetStep,
    MainForeachStepInputForeachDoSetStep,
    MainForeachStepInputForeachDoLogStep,
    MainForeachStepInputForeachDoYieldStep,
]

_MainForeachStepInputForeachReservedKeywords = TypedDict(
    "_MainForeachStepInputForeachReservedKeywords",
    {
        "in": str,
    },
    total=False,
)


class MainForeachStepInputForeach(_MainForeachStepInputForeachReservedKeywords, total=False):
    do: Required[MainForeachStepInputForeachDo]


class MainForeachStepInput(TypedDict, total=False):
    foreach: Required[MainForeachStepInputForeach]


class MainParallelStepInputParallelEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainParallelStepInputParallelToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainParallelStepInputParallelPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainParallelStepInputParallelPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0(
    _MainParallelStepInputParallelPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str], Iterable[MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1], str
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoiceFunction]


MainParallelStepInputParallelPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoice
]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestAPICall(TypedDict, total=False):
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


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestIntegration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestSystem(TypedDict, total=False):
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


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequest(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestFunction]
    """Function definition"""

    integration: Optional[MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestIntegration]
    """Integration definition"""

    system: Optional[MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestSystem]
    """System definition"""


MainParallelStepInputParallelPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRef,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequest,
]


class MainParallelStepInputParallelPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainParallelStepInputParallelPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainParallelStepInputParallelPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainParallelStepInputParallelPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainParallelStepInputParallelGetStep(TypedDict, total=False):
    get: Required[str]


class MainParallelStepInputParallelSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainParallelStepInputParallelLogStep(TypedDict, total=False):
    log: Required[str]


class MainParallelStepInputParallelYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


MainParallelStepInputParallel: TypeAlias = Union[
    MainParallelStepInputParallelEvaluateStep,
    MainParallelStepInputParallelToolCallStep,
    MainParallelStepInputParallelPromptStepInput,
    MainParallelStepInputParallelGetStep,
    MainParallelStepInputParallelSetStep,
    MainParallelStepInputParallelLogStep,
    MainParallelStepInputParallelYieldStep,
]


class MainParallelStepInput(TypedDict, total=False):
    parallel: Required[Iterable[MainParallelStepInputParallel]]


class MainMainInputMapEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainMainInputMapToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(TypedDict, total=False):
    image_url: Required[MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL]
    """The image URL"""

    type: Literal["image_url"]


MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainMainInputMapPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainMainInputMapPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainMainInputMapPromptStepInputPromptUnionMember0(
    _MainMainInputMapPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[List[str], Iterable[MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1], str]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainMainInputMapPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainMainInputMapPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainMainInputMapPromptStepInputToolChoiceNamedToolChoiceFunction]


MainMainInputMapPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainMainInputMapPromptStepInputToolChoiceNamedToolChoice
]


class MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainMainInputMapPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestAPICall(TypedDict, total=False):
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


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestIntegration(TypedDict, total=False):
    provider: Required[
        Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase", "email"], str]
    ]

    arguments: Optional[object]

    method: Optional[str]

    setup: Optional[object]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestSystem(TypedDict, total=False):
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


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequest(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestAPICall]
    """API call definition"""

    description: Optional[str]

    function: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestFunction]
    """Function definition"""

    integration: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestIntegration]
    """Integration definition"""

    system: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestSystem]
    """System definition"""


MainMainInputMapPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainMainInputMapPromptStepInputToolsUnionMember1ToolRef,
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequest,
]


class MainMainInputMapPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainMainInputMapPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainMainInputMapPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainMainInputMapPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainMainInputMapGetStep(TypedDict, total=False):
    get: Required[str]


class MainMainInputMapSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainMainInputMapLogStep(TypedDict, total=False):
    log: Required[str]


class MainMainInputMapYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


MainMainInputMap: TypeAlias = Union[
    MainMainInputMapEvaluateStep,
    MainMainInputMapToolCallStep,
    MainMainInputMapPromptStepInput,
    MainMainInputMapGetStep,
    MainMainInputMapSetStep,
    MainMainInputMapLogStep,
    MainMainInputMapYieldStep,
]


class MainMainInput(TypedDict, total=False):
    map: Required[MainMainInputMap]

    over: Required[str]

    initial: object

    parallelism: Optional[int]

    reduce: Optional[str]


Main: TypeAlias = Union[
    MainEvaluateStep,
    MainToolCallStep,
    MainPromptStepInput,
    MainGetStep,
    MainSetStep,
    MainLogStep,
    MainYieldStep,
    MainReturnStep,
    MainSleepStep,
    MainErrorWorkflowStep,
    MainWaitForInputStep,
    MainIfElseWorkflowStepInput,
    MainSwitchStepInput,
    MainForeachStepInput,
    MainParallelStepInput,
    MainMainInput,
]

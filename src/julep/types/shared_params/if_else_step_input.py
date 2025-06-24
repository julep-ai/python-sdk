# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from ..._compat import PYDANTIC_V2
from ..get_step_param import GetStepParam
from ..log_step_param import LogStepParam
from ..set_step_param import SetStepParam
from ..sleep_step_param import SleepStepParam
from ..yield_step_param import YieldStepParam
from .prompt_step_input import PromptStepInput
from ..return_step_param import ReturnStepParam
from ..evaluate_step_param import EvaluateStepParam
from ..tool_call_step_param import ToolCallStepParam
from ..error_workflow_step_param import ErrorWorkflowStepParam
from ..wait_for_input_step_param import WaitForInputStepParam

__all__ = [
    "IfElseStepInput",
    "Then",
    "ThenSwitchStepInput",
    "ThenSwitchStepInputSwitch",
    "ThenSwitchStepInputSwitchThen",
    "ThenForeachStepInput",
    "ThenForeachStepInputForeach",
    "ThenForeachStepInputForeachDo",
    "ThenParallelStepInput",
    "ThenParallelStepInputParallel",
    "ThenThenInput",
    "ThenThenInputMap",
    "Else",
    "ElseSwitchStepInput",
    "ElseSwitchStepInputSwitch",
    "ElseSwitchStepInputSwitchThen",
    "ElseForeachStepInput",
    "ElseForeachStepInputForeach",
    "ElseForeachStepInputForeachDo",
    "ElseParallelStepInput",
    "ElseParallelStepInputParallel",
    "ElseElseInput",
    "ElseElseInputMap",
]

ThenSwitchStepInputSwitchThen: TypeAlias = Union[
    EvaluateStepParam,
    ToolCallStepParam,
    PromptStepInput,
    GetStepParam,
    SetStepParam,
    LogStepParam,
    YieldStepParam,
    ReturnStepParam,
    SleepStepParam,
    ErrorWorkflowStepParam,
    WaitForInputStepParam,
]


class ThenSwitchStepInputSwitch(TypedDict, total=False):
    case: Required[Literal["_"]]

    then: Required[ThenSwitchStepInputSwitchThen]


class ThenSwitchStepInput(TypedDict, total=False):
    switch: Required[Iterable[ThenSwitchStepInputSwitch]]

    label: Optional[str]


ThenForeachStepInputForeachDo: TypeAlias = Union[
    WaitForInputStepParam,
    EvaluateStepParam,
    ToolCallStepParam,
    PromptStepInput,
    GetStepParam,
    SetStepParam,
    LogStepParam,
    YieldStepParam,
]

_ThenForeachStepInputForeachReservedKeywords = TypedDict(
    "_ThenForeachStepInputForeachReservedKeywords",
    {
        "in": str,
    },
    total=False,
)


class ThenForeachStepInputForeach(_ThenForeachStepInputForeachReservedKeywords, total=False):
    do: Required[ThenForeachStepInputForeachDo]


class ThenForeachStepInput(TypedDict, total=False):
    foreach: Required[ThenForeachStepInputForeach]

    label: Optional[str]


ThenParallelStepInputParallel: TypeAlias = Union[
    EvaluateStepParam, ToolCallStepParam, PromptStepInput, GetStepParam, SetStepParam, LogStepParam, YieldStepParam
]


class ThenParallelStepInput(TypedDict, total=False):
    parallel: Required[Iterable[ThenParallelStepInputParallel]]

    label: Optional[str]


ThenThenInputMap: TypeAlias = Union[
    EvaluateStepParam, ToolCallStepParam, PromptStepInput, GetStepParam, SetStepParam, LogStepParam, YieldStepParam
]


class ThenThenInput(TypedDict, total=False):
    map: Required[ThenThenInputMap]

    over: Required[str]

    initial: object

    label: Optional[str]

    parallelism: Optional[int]

    reduce: Optional[str]


if TYPE_CHECKING or PYDANTIC_V2:
    Then = TypeAliasType(
        "Then",
        Union[
            WaitForInputStepParam,
            EvaluateStepParam,
            ToolCallStepParam,
            PromptStepInput,
            GetStepParam,
            SetStepParam,
            LogStepParam,
            YieldStepParam,
            ReturnStepParam,
            SleepStepParam,
            ErrorWorkflowStepParam,
            "IfElseStepInput",
            ThenSwitchStepInput,
            ThenForeachStepInput,
            ThenParallelStepInput,
            ThenThenInput,
        ],
    )
else:
    Then: TypeAlias = Union[
        WaitForInputStepParam,
        EvaluateStepParam,
        ToolCallStepParam,
        PromptStepInput,
        GetStepParam,
        SetStepParam,
        LogStepParam,
        YieldStepParam,
        ReturnStepParam,
        SleepStepParam,
        ErrorWorkflowStepParam,
        "IfElseStepInput",
        ThenSwitchStepInput,
        ThenForeachStepInput,
        ThenParallelStepInput,
        ThenThenInput,
    ]

ElseSwitchStepInputSwitchThen: TypeAlias = Union[
    EvaluateStepParam,
    ToolCallStepParam,
    PromptStepInput,
    GetStepParam,
    SetStepParam,
    LogStepParam,
    YieldStepParam,
    ReturnStepParam,
    SleepStepParam,
    ErrorWorkflowStepParam,
    WaitForInputStepParam,
]


class ElseSwitchStepInputSwitch(TypedDict, total=False):
    case: Required[Literal["_"]]

    then: Required[ElseSwitchStepInputSwitchThen]


class ElseSwitchStepInput(TypedDict, total=False):
    switch: Required[Iterable[ElseSwitchStepInputSwitch]]

    label: Optional[str]


ElseForeachStepInputForeachDo: TypeAlias = Union[
    WaitForInputStepParam,
    EvaluateStepParam,
    ToolCallStepParam,
    PromptStepInput,
    GetStepParam,
    SetStepParam,
    LogStepParam,
    YieldStepParam,
]

_ElseForeachStepInputForeachReservedKeywords = TypedDict(
    "_ElseForeachStepInputForeachReservedKeywords",
    {
        "in": str,
    },
    total=False,
)


class ElseForeachStepInputForeach(_ElseForeachStepInputForeachReservedKeywords, total=False):
    do: Required[ElseForeachStepInputForeachDo]


class ElseForeachStepInput(TypedDict, total=False):
    foreach: Required[ElseForeachStepInputForeach]

    label: Optional[str]


ElseParallelStepInputParallel: TypeAlias = Union[
    EvaluateStepParam, ToolCallStepParam, PromptStepInput, GetStepParam, SetStepParam, LogStepParam, YieldStepParam
]


class ElseParallelStepInput(TypedDict, total=False):
    parallel: Required[Iterable[ElseParallelStepInputParallel]]

    label: Optional[str]


ElseElseInputMap: TypeAlias = Union[
    EvaluateStepParam, ToolCallStepParam, PromptStepInput, GetStepParam, SetStepParam, LogStepParam, YieldStepParam
]


class ElseElseInput(TypedDict, total=False):
    map: Required[ElseElseInputMap]

    over: Required[str]

    initial: object

    label: Optional[str]

    parallelism: Optional[int]

    reduce: Optional[str]


if TYPE_CHECKING or PYDANTIC_V2:
    Else = TypeAliasType(
        "Else",
        Union[
            WaitForInputStepParam,
            EvaluateStepParam,
            ToolCallStepParam,
            PromptStepInput,
            GetStepParam,
            SetStepParam,
            LogStepParam,
            YieldStepParam,
            ReturnStepParam,
            SleepStepParam,
            ErrorWorkflowStepParam,
            "IfElseStepInput",
            ElseSwitchStepInput,
            ElseForeachStepInput,
            ElseParallelStepInput,
            ElseElseInput,
        ],
    )
else:
    Else: TypeAlias = Union[
        WaitForInputStepParam,
        EvaluateStepParam,
        ToolCallStepParam,
        PromptStepInput,
        GetStepParam,
        SetStepParam,
        LogStepParam,
        YieldStepParam,
        ReturnStepParam,
        SleepStepParam,
        ErrorWorkflowStepParam,
        "IfElseStepInput",
        ElseSwitchStepInput,
        ElseForeachStepInput,
        ElseParallelStepInput,
        ElseElseInput,
    ]

_IfElseStepInputReservedKeywords = TypedDict(
    "_IfElseStepInputReservedKeywords",
    {
        "if": str,
        "else": Optional[Else],
    },
    total=False,
)


class IfElseStepInput(_IfElseStepInputReservedKeywords, total=False):
    then: Required[Then]
    """The steps to run if the condition is true"""

    label: Optional[str]

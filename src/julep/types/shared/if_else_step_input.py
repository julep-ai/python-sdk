# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel
from ..get_step import GetStep
from ..log_step import LogStep
from ..set_step import SetStep
from ..sleep_step import SleepStep
from ..yield_step import YieldStep
from ..return_step import ReturnStep
from ..evaluate_step import EvaluateStep
from ..tool_call_step import ToolCallStep
from .prompt_step_input import PromptStepInput
from ..error_workflow_step import ErrorWorkflowStep
from ..wait_for_input_step import WaitForInputStep

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
    EvaluateStep,
    ToolCallStep,
    PromptStepInput,
    GetStep,
    SetStep,
    LogStep,
    YieldStep,
    ReturnStep,
    SleepStep,
    ErrorWorkflowStep,
    WaitForInputStep,
]


class ThenSwitchStepInputSwitch(BaseModel):
    case: Literal["_"]

    then: ThenSwitchStepInputSwitchThen


class ThenSwitchStepInput(BaseModel):
    switch: List[ThenSwitchStepInputSwitch]

    kind: Optional[Literal["switch"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


ThenForeachStepInputForeachDo: TypeAlias = Union[
    WaitForInputStep, EvaluateStep, ToolCallStep, PromptStepInput, GetStep, SetStep, LogStep, YieldStep
]


class ThenForeachStepInputForeach(BaseModel):
    do: ThenForeachStepInputForeachDo

    in_: str = FieldInfo(alias="in")


class ThenForeachStepInput(BaseModel):
    foreach: ThenForeachStepInputForeach

    kind: Optional[Literal["foreach"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


ThenParallelStepInputParallel: TypeAlias = Union[
    EvaluateStep, ToolCallStep, PromptStepInput, GetStep, SetStep, LogStep, YieldStep
]


class ThenParallelStepInput(BaseModel):
    parallel: List[ThenParallelStepInputParallel]

    kind: Optional[Literal["parallel"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


ThenThenInputMap: TypeAlias = Union[EvaluateStep, ToolCallStep, PromptStepInput, GetStep, SetStep, LogStep, YieldStep]


class ThenThenInput(BaseModel):
    map: ThenThenInputMap

    over: str

    initial: Optional[object] = None

    kind: Optional[Literal["map_reduce"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

    parallelism: Optional[int] = None

    reduce: Optional[str] = None


if TYPE_CHECKING or PYDANTIC_V2:
    Then = TypeAliasType(
        "Then",
        Union[
            WaitForInputStep,
            EvaluateStep,
            ToolCallStep,
            PromptStepInput,
            GetStep,
            SetStep,
            LogStep,
            YieldStep,
            ReturnStep,
            SleepStep,
            ErrorWorkflowStep,
            "IfElseStepInput",
            ThenSwitchStepInput,
            ThenForeachStepInput,
            ThenParallelStepInput,
            ThenThenInput,
        ],
    )
else:
    Then: TypeAlias = Union[
        WaitForInputStep,
        EvaluateStep,
        ToolCallStep,
        PromptStepInput,
        GetStep,
        SetStep,
        LogStep,
        YieldStep,
        ReturnStep,
        SleepStep,
        ErrorWorkflowStep,
        "IfElseStepInput",
        ThenSwitchStepInput,
        ThenForeachStepInput,
        ThenParallelStepInput,
        ThenThenInput,
    ]

ElseSwitchStepInputSwitchThen: TypeAlias = Union[
    EvaluateStep,
    ToolCallStep,
    PromptStepInput,
    GetStep,
    SetStep,
    LogStep,
    YieldStep,
    ReturnStep,
    SleepStep,
    ErrorWorkflowStep,
    WaitForInputStep,
]


class ElseSwitchStepInputSwitch(BaseModel):
    case: Literal["_"]

    then: ElseSwitchStepInputSwitchThen


class ElseSwitchStepInput(BaseModel):
    switch: List[ElseSwitchStepInputSwitch]

    kind: Optional[Literal["switch"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


ElseForeachStepInputForeachDo: TypeAlias = Union[
    WaitForInputStep, EvaluateStep, ToolCallStep, PromptStepInput, GetStep, SetStep, LogStep, YieldStep
]


class ElseForeachStepInputForeach(BaseModel):
    do: ElseForeachStepInputForeachDo

    in_: str = FieldInfo(alias="in")


class ElseForeachStepInput(BaseModel):
    foreach: ElseForeachStepInputForeach

    kind: Optional[Literal["foreach"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


ElseParallelStepInputParallel: TypeAlias = Union[
    EvaluateStep, ToolCallStep, PromptStepInput, GetStep, SetStep, LogStep, YieldStep
]


class ElseParallelStepInput(BaseModel):
    parallel: List[ElseParallelStepInputParallel]

    kind: Optional[Literal["parallel"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


ElseElseInputMap: TypeAlias = Union[EvaluateStep, ToolCallStep, PromptStepInput, GetStep, SetStep, LogStep, YieldStep]


class ElseElseInput(BaseModel):
    map: ElseElseInputMap

    over: str

    initial: Optional[object] = None

    kind: Optional[Literal["map_reduce"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

    parallelism: Optional[int] = None

    reduce: Optional[str] = None


if TYPE_CHECKING or PYDANTIC_V2:
    Else = TypeAliasType(
        "Else",
        Union[
            WaitForInputStep,
            EvaluateStep,
            ToolCallStep,
            PromptStepInput,
            GetStep,
            SetStep,
            LogStep,
            YieldStep,
            ReturnStep,
            SleepStep,
            ErrorWorkflowStep,
            "IfElseStepInput",
            ElseSwitchStepInput,
            ElseForeachStepInput,
            ElseParallelStepInput,
            ElseElseInput,
            None,
        ],
    )
else:
    Else: TypeAlias = Union[
        WaitForInputStep,
        EvaluateStep,
        ToolCallStep,
        PromptStepInput,
        GetStep,
        SetStep,
        LogStep,
        YieldStep,
        ReturnStep,
        SleepStep,
        ErrorWorkflowStep,
        "IfElseStepInput",
        ElseSwitchStepInput,
        ElseForeachStepInput,
        ElseParallelStepInput,
        ElseElseInput,
        None,
    ]


class IfElseStepInput(BaseModel):
    if_: str = FieldInfo(alias="if")

    then: Then
    """The steps to run if the condition is true"""

    else_: Optional[Else] = FieldInfo(alias="else", default=None)
    """The steps to run if the condition is false"""

    kind: Optional[Literal["if_else"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


if PYDANTIC_V2:
    IfElseStepInput.model_rebuild()
    ThenSwitchStepInput.model_rebuild()
    ThenSwitchStepInputSwitch.model_rebuild()
    ThenForeachStepInput.model_rebuild()
    ThenForeachStepInputForeach.model_rebuild()
    ThenParallelStepInput.model_rebuild()
    ThenThenInput.model_rebuild()
    ElseSwitchStepInput.model_rebuild()
    ElseSwitchStepInputSwitch.model_rebuild()
    ElseForeachStepInput.model_rebuild()
    ElseForeachStepInputForeach.model_rebuild()
    ElseParallelStepInput.model_rebuild()
    ElseElseInput.model_rebuild()
else:
    IfElseStepInput.update_forward_refs()  # type: ignore
    ThenSwitchStepInput.update_forward_refs()  # type: ignore
    ThenSwitchStepInputSwitch.update_forward_refs()  # type: ignore
    ThenForeachStepInput.update_forward_refs()  # type: ignore
    ThenForeachStepInputForeach.update_forward_refs()  # type: ignore
    ThenParallelStepInput.update_forward_refs()  # type: ignore
    ThenThenInput.update_forward_refs()  # type: ignore
    ElseSwitchStepInput.update_forward_refs()  # type: ignore
    ElseSwitchStepInputSwitch.update_forward_refs()  # type: ignore
    ElseForeachStepInput.update_forward_refs()  # type: ignore
    ElseForeachStepInputForeach.update_forward_refs()  # type: ignore
    ElseParallelStepInput.update_forward_refs()  # type: ignore
    ElseElseInput.update_forward_refs()  # type: ignore

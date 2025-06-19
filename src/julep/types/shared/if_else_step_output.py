# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
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
from ..prompt_step_output import PromptStepOutput
from ..switch_step_output import SwitchStepOutput
from ..error_workflow_step import ErrorWorkflowStep
from ..foreach_step_output import ForeachStepOutput
from ..wait_for_input_step import WaitForInputStep
from ..parallel_step_output import ParallelStepOutput

__all__ = [
    "IfElseStepOutput",
    "Then",
    "ThenThenOutput",
    "ThenThenOutputMap",
    "Else",
    "ElseElseOutput",
    "ElseElseOutputMap",
]

ThenThenOutputMap: TypeAlias = Union[EvaluateStep, ToolCallStep, PromptStepOutput, GetStep, SetStep, LogStep, YieldStep]


class ThenThenOutput(BaseModel):
    map: ThenThenOutputMap

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
            PromptStepOutput,
            GetStep,
            SetStep,
            LogStep,
            YieldStep,
            ReturnStep,
            SleepStep,
            ErrorWorkflowStep,
            "IfElseStepOutput",
            SwitchStepOutput,
            ForeachStepOutput,
            ParallelStepOutput,
            ThenThenOutput,
        ],
    )
else:
    Then: TypeAlias = Union[
        WaitForInputStep,
        EvaluateStep,
        ToolCallStep,
        PromptStepOutput,
        GetStep,
        SetStep,
        LogStep,
        YieldStep,
        ReturnStep,
        SleepStep,
        ErrorWorkflowStep,
        "IfElseStepOutput",
        SwitchStepOutput,
        ForeachStepOutput,
        ParallelStepOutput,
        ThenThenOutput,
    ]

ElseElseOutputMap: TypeAlias = Union[EvaluateStep, ToolCallStep, PromptStepOutput, GetStep, SetStep, LogStep, YieldStep]


class ElseElseOutput(BaseModel):
    map: ElseElseOutputMap

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
            PromptStepOutput,
            GetStep,
            SetStep,
            LogStep,
            YieldStep,
            ReturnStep,
            SleepStep,
            ErrorWorkflowStep,
            "IfElseStepOutput",
            SwitchStepOutput,
            ForeachStepOutput,
            ParallelStepOutput,
            ElseElseOutput,
            None,
        ],
    )
else:
    Else: TypeAlias = Union[
        WaitForInputStep,
        EvaluateStep,
        ToolCallStep,
        PromptStepOutput,
        GetStep,
        SetStep,
        LogStep,
        YieldStep,
        ReturnStep,
        SleepStep,
        ErrorWorkflowStep,
        "IfElseStepOutput",
        SwitchStepOutput,
        ForeachStepOutput,
        ParallelStepOutput,
        ElseElseOutput,
        None,
    ]


class IfElseStepOutput(BaseModel):
    if_: str = FieldInfo(alias="if")

    then: Then
    """The steps to run if the condition is true"""

    else_: Optional[Else] = FieldInfo(alias="else", default=None)
    """The steps to run if the condition is false"""

    kind: Optional[Literal["if_else"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None


if PYDANTIC_V2:
    IfElseStepOutput.model_rebuild()
    ThenThenOutput.model_rebuild()
    ElseElseOutput.model_rebuild()
else:
    IfElseStepOutput.update_forward_refs()  # type: ignore
    ThenThenOutput.update_forward_refs()  # type: ignore
    ElseElseOutput.update_forward_refs()  # type: ignore

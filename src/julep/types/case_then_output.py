# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .get_step import GetStep
from .log_step import LogStep
from .set_step import SetStep
from .sleep_step import SleepStep
from .yield_step import YieldStep
from .return_step import ReturnStep
from .evaluate_step import EvaluateStep
from .tool_call_step import ToolCallStep
from .prompt_step_output import PromptStepOutput
from .error_workflow_step import ErrorWorkflowStep
from .wait_for_input_step import WaitForInputStep

__all__ = ["CaseThenOutput", "Then"]

Then: TypeAlias = Union[
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
    WaitForInputStep,
]


class CaseThenOutput(BaseModel):
    case: Literal["_"]

    then: Then

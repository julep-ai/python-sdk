# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .get_step import GetStep
from .log_step import LogStep
from .set_step import SetStep
from .yield_step import YieldStep
from .evaluate_step import EvaluateStep
from .tool_call_step import ToolCallStep
from .prompt_step_output import PromptStepOutput
from .wait_for_input_step import WaitForInputStep

__all__ = ["ForeachDoOutput", "Do"]

Do: TypeAlias = Union[
    WaitForInputStep, EvaluateStep, ToolCallStep, PromptStepOutput, GetStep, SetStep, LogStep, YieldStep
]


class ForeachDoOutput(BaseModel):
    do: Do

    in_: str = FieldInfo(alias="in")

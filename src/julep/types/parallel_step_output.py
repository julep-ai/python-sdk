# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .get_step import GetStep
from .log_step import LogStep
from .set_step import SetStep
from .yield_step import YieldStep
from .evaluate_step import EvaluateStep
from .tool_call_step import ToolCallStep
from .prompt_step_output import PromptStepOutput

__all__ = ["ParallelStepOutput", "Parallel"]

Parallel: TypeAlias = Union[EvaluateStep, ToolCallStep, PromptStepOutput, GetStep, SetStep, LogStep, YieldStep]


class ParallelStepOutput(BaseModel):
    parallel: List[Parallel]

    kind: Optional[Literal["parallel"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

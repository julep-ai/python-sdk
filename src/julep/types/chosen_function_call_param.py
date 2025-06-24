# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .chosen_bash20241022_param import ChosenBash20241022Param
from .chosen_computer20241022_param import ChosenComputer20241022Param
from .chosen_text_editor20241022_param import ChosenTextEditor20241022Param
from .shared_params.function_call_option import FunctionCallOption

__all__ = ["ChosenFunctionCallParam"]


class ChosenFunctionCallParam(TypedDict, total=False):
    function: Required[FunctionCallOption]

    api_call: object

    bash_20241022: Optional[ChosenBash20241022Param]

    computer_20241022: Optional[ChosenComputer20241022Param]

    integration: object

    system: object

    text_editor_20241022: Optional[ChosenTextEditor20241022Param]

    type: Literal["function"]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .chosen_bash20241022 import ChosenBash20241022
from .chosen_computer20241022 import ChosenComputer20241022
from .chosen_text_editor20241022 import ChosenTextEditor20241022
from .shared.function_call_option import FunctionCallOption

__all__ = ["ChosenFunctionCall"]


class ChosenFunctionCall(BaseModel):
    function: FunctionCallOption

    id: Optional[str] = None

    api_call: Optional[object] = None

    bash_20241022: Optional[ChosenBash20241022] = None

    computer_20241022: Optional[ChosenComputer20241022] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    text_editor_20241022: Optional[ChosenTextEditor20241022] = None

    type: Optional[Literal["function"]] = None

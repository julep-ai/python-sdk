# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .get_step import GetStep
from .log_step import LogStep
from .set_step import SetStep
from .sleep_step import SleepStep
from .yield_step import YieldStep
from .return_step import ReturnStep
from .evaluate_step import EvaluateStep
from .tool_call_step import ToolCallStep
from .shared.secret_ref import SecretRef
from .shared.system_def import SystemDef
from .prompt_step_output import PromptStepOutput
from .switch_step_output import SwitchStepOutput
from .error_workflow_step import ErrorWorkflowStep
from .foreach_step_output import ForeachStepOutput
from .shared.function_def import FunctionDef
from .wait_for_input_step import WaitForInputStep
from .parallel_step_output import ParallelStepOutput
from .shared.bash20241022_def import Bash20241022Def
from .shared.computer20241022_def import Computer20241022Def
from .shared.arxiv_integration_def import ArxivIntegrationDef
from .shared.brave_integration_def import BraveIntegrationDef
from .shared.dummy_integration_def import DummyIntegrationDef
from .shared.email_integration_def import EmailIntegrationDef
from .shared.ffmpeg_integration_def import FfmpegIntegrationDef
from .shared.spider_integration_def import SpiderIntegrationDef
from .shared.algolia_integration_def import AlgoliaIntegrationDef
from .shared.mailgun_integration_def import MailgunIntegrationDef
from .shared.text_editor20241022_def import TextEditor20241022Def
from .shared.weather_integration_def import WeatherIntegrationDef
from .shared.wikipedia_integration_def import WikipediaIntegrationDef
from .shared.llama_parse_integration_def import LlamaParseIntegrationDef
from .shared.unstructured_integration_def import UnstructuredIntegrationDef
from .shared.remote_browser_integration_def import RemoteBrowserIntegrationDef
from .shared.cloudinary_edit_integration_def import CloudinaryEditIntegrationDef
from .shared.cloudinary_upload_integration_def import CloudinaryUploadIntegrationDef
from .shared.browserbase_context_integration_def import BrowserbaseContextIntegrationDef
from .shared.browserbase_extension_integration_def import BrowserbaseExtensionIntegrationDef
from .shared.browserbase_get_session_integration_def import BrowserbaseGetSessionIntegrationDef
from .shared.browserbase_list_sessions_integration_def import BrowserbaseListSessionsIntegrationDef
from .shared.browserbase_create_session_integration_def import BrowserbaseCreateSessionIntegrationDef
from .shared.browserbase_complete_session_integration_def import BrowserbaseCompleteSessionIntegrationDef
from .shared.browserbase_get_session_live_urls_integration_def import BrowserbaseGetSessionLiveURLsIntegrationDef

__all__ = [
    "Task",
    "Main",
    "MainMainOutput",
    "MainMainOutputMap",
    "Tool",
    "ToolAPICall",
    "ToolAPICallParamsSchema",
    "ToolAPICallParamsSchemaProperties",
    "ToolIntegration",
]

MainMainOutputMap: TypeAlias = Union[EvaluateStep, ToolCallStep, PromptStepOutput, GetStep, SetStep, LogStep, YieldStep]


class MainMainOutput(BaseModel):
    map: MainMainOutputMap

    over: str

    initial: Optional[object] = None

    kind: Optional[Literal["map_reduce"]] = FieldInfo(alias="kind_", default=None)

    label: Optional[str] = None

    parallelism: Optional[int] = None

    reduce: Optional[str] = None


Main: TypeAlias = Union[
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
    "IfElseStepOutput",
    SwitchStepOutput,
    ForeachStepOutput,
    ParallelStepOutput,
    MainMainOutput,
]


class ToolAPICallParamsSchemaProperties(BaseModel):
    type: str

    description: Optional[str] = None

    enum: Optional[List[str]] = None

    items: Optional[object] = None


class ToolAPICallParamsSchema(BaseModel):
    properties: Dict[str, ToolAPICallParamsSchemaProperties]

    additional_properties: Optional[bool] = FieldInfo(alias="additionalProperties", default=None)

    required: Optional[List[str]] = None

    type: Optional[str] = None


class ToolAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    files: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    include_response_content: Optional[bool] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    params_schema: Optional[ToolAPICallParamsSchema] = None
    """JSON Schema for API call parameters"""

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    secrets: Optional[Dict[str, SecretRef]] = None

    timeout: Optional[int] = None


ToolIntegration: TypeAlias = Union[
    DummyIntegrationDef,
    BraveIntegrationDef,
    EmailIntegrationDef,
    SpiderIntegrationDef,
    WikipediaIntegrationDef,
    WeatherIntegrationDef,
    MailgunIntegrationDef,
    BrowserbaseContextIntegrationDef,
    BrowserbaseExtensionIntegrationDef,
    BrowserbaseListSessionsIntegrationDef,
    BrowserbaseCreateSessionIntegrationDef,
    BrowserbaseGetSessionIntegrationDef,
    BrowserbaseCompleteSessionIntegrationDef,
    BrowserbaseGetSessionLiveURLsIntegrationDef,
    RemoteBrowserIntegrationDef,
    LlamaParseIntegrationDef,
    FfmpegIntegrationDef,
    CloudinaryUploadIntegrationDef,
    CloudinaryEditIntegrationDef,
    ArxivIntegrationDef,
    UnstructuredIntegrationDef,
    AlgoliaIntegrationDef,
    None,
]


class Tool(BaseModel):
    name: str

    type: Literal[
        "function", "integration", "system", "api_call", "computer_20241022", "text_editor_20241022", "bash_20241022"
    ]

    api_call: Optional[ToolAPICall] = None
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def] = None

    computer_20241022: Optional[Computer20241022Def] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[FunctionDef] = None
    """Function definition"""

    inherited: Optional[bool] = None

    integration: Optional[ToolIntegration] = None
    """Brave integration definition"""

    system: Optional[SystemDef] = None
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def] = None


class Task(BaseModel):
    id: str

    created_at: datetime

    main: List[Main]

    name: str

    updated_at: datetime

    canonical_name: Optional[str] = None

    description: Optional[str] = None

    inherit_tools: Optional[bool] = None

    input_schema: Optional[object] = None

    metadata: Optional[object] = None

    tools: Optional[List[Tool]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


from .shared.if_else_step_output import IfElseStepOutput

if PYDANTIC_V2:
    Task.model_rebuild()
    MainMainOutput.model_rebuild()
    Tool.model_rebuild()
    ToolAPICall.model_rebuild()
    ToolAPICallParamsSchema.model_rebuild()
    ToolAPICallParamsSchemaProperties.model_rebuild()
else:
    Task.update_forward_refs()  # type: ignore
    MainMainOutput.update_forward_refs()  # type: ignore
    Tool.update_forward_refs()  # type: ignore
    ToolAPICall.update_forward_refs()  # type: ignore
    ToolAPICallParamsSchema.update_forward_refs()  # type: ignore
    ToolAPICallParamsSchemaProperties.update_forward_refs()  # type: ignore

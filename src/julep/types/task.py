# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .tool import Tool
from .._models import BaseModel
from .chat_settings import ChatSettings

__all__ = [
    "Task",
    "Main",
    "MainEvaluateStep",
    "MainToolCallStep",
    "MainPromptStepOutput",
    "MainPromptStepOutputPromptUnionMember0",
    "MainPromptStepOutputPromptUnionMember0ContentUnionMember1",
    "MainPromptStepOutputPromptUnionMember0ContentUnionMember1Content",
    "MainPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainPromptStepOutputToolChoice",
    "MainPromptStepOutputToolChoiceNamedToolChoice",
    "MainPromptStepOutputToolChoiceNamedToolChoiceFunction",
    "MainPromptStepOutputToolsUnionMember1",
    "MainPromptStepOutputToolsUnionMember1ToolRef",
    "MainPromptStepOutputToolsUnionMember1ToolRefRef",
    "MainPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID",
    "MainPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequest",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestAPICall",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestFunction",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestIntegration",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestSystem",
    "MainGetStep",
    "MainSetStep",
    "MainLogStep",
    "MainEmbedStep",
    "MainEmbedStepEmbed",
    "MainSearchStep",
    "MainSearchStepSearch",
    "MainSearchStepSearchVectorDocSearchRequest",
    "MainSearchStepSearchTextOnlyDocSearchRequest",
    "MainSearchStepSearchHybridDocSearchRequest",
    "MainYieldStep",
    "MainReturnStep",
    "MainSleepStep",
    "MainSleepStepSleep",
    "MainErrorWorkflowStep",
    "MainWaitForInputStep",
    "MainWaitForInputStepWaitForInput",
    "MainIfElseWorkflowStepOutput",
    "MainIfElseWorkflowStepOutputThen",
    "MainIfElseWorkflowStepOutputThenEvaluateStep",
    "MainIfElseWorkflowStepOutputThenToolCallStep",
    "MainIfElseWorkflowStepOutputThenPromptStepOutput",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1Content",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoice",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoiceNamedToolChoice",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoiceNamedToolChoiceFunction",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequest",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestAPICall",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestFunction",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestIntegration",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestSystem",
    "MainIfElseWorkflowStepOutputThenGetStep",
    "MainIfElseWorkflowStepOutputThenSetStep",
    "MainIfElseWorkflowStepOutputThenLogStep",
    "MainIfElseWorkflowStepOutputThenEmbedStep",
    "MainIfElseWorkflowStepOutputThenEmbedStepEmbed",
    "MainIfElseWorkflowStepOutputThenSearchStep",
    "MainIfElseWorkflowStepOutputThenSearchStepSearch",
    "MainIfElseWorkflowStepOutputThenSearchStepSearchVectorDocSearchRequest",
    "MainIfElseWorkflowStepOutputThenSearchStepSearchTextOnlyDocSearchRequest",
    "MainIfElseWorkflowStepOutputThenSearchStepSearchHybridDocSearchRequest",
    "MainIfElseWorkflowStepOutputThenYieldStep",
    "MainIfElseWorkflowStepOutputThenReturnStep",
    "MainIfElseWorkflowStepOutputThenSleepStep",
    "MainIfElseWorkflowStepOutputThenSleepStepSleep",
    "MainIfElseWorkflowStepOutputThenErrorWorkflowStep",
    "MainIfElseWorkflowStepOutputThenWaitForInputStep",
    "MainIfElseWorkflowStepOutputThenWaitForInputStepWaitForInput",
    "MainIfElseWorkflowStepOutputElse",
    "MainIfElseWorkflowStepOutputElseEvaluateStep",
    "MainIfElseWorkflowStepOutputElseToolCallStep",
    "MainIfElseWorkflowStepOutputElsePromptStepOutput",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1Content",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoice",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoiceNamedToolChoice",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoiceNamedToolChoiceFunction",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRefToolRefByID",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRefToolRefByName",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequest",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestAPICall",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestFunction",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestIntegration",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestSystem",
    "MainIfElseWorkflowStepOutputElseGetStep",
    "MainIfElseWorkflowStepOutputElseSetStep",
    "MainIfElseWorkflowStepOutputElseLogStep",
    "MainIfElseWorkflowStepOutputElseEmbedStep",
    "MainIfElseWorkflowStepOutputElseEmbedStepEmbed",
    "MainIfElseWorkflowStepOutputElseSearchStep",
    "MainIfElseWorkflowStepOutputElseSearchStepSearch",
    "MainIfElseWorkflowStepOutputElseSearchStepSearchVectorDocSearchRequest",
    "MainIfElseWorkflowStepOutputElseSearchStepSearchTextOnlyDocSearchRequest",
    "MainIfElseWorkflowStepOutputElseSearchStepSearchHybridDocSearchRequest",
    "MainIfElseWorkflowStepOutputElseYieldStep",
    "MainIfElseWorkflowStepOutputElseReturnStep",
    "MainIfElseWorkflowStepOutputElseSleepStep",
    "MainIfElseWorkflowStepOutputElseSleepStepSleep",
    "MainIfElseWorkflowStepOutputElseErrorWorkflowStep",
    "MainIfElseWorkflowStepOutputElseWaitForInputStep",
    "MainIfElseWorkflowStepOutputElseWaitForInputStepWaitForInput",
    "MainSwitchStepOutput",
    "MainSwitchStepOutputSwitch",
    "MainSwitchStepOutputSwitchThen",
    "MainSwitchStepOutputSwitchThenEvaluateStep",
    "MainSwitchStepOutputSwitchThenToolCallStep",
    "MainSwitchStepOutputSwitchThenPromptStepOutput",
    "MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0",
    "MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1",
    "MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1Content",
    "MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolChoice",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolChoiceNamedToolChoice",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolChoiceNamedToolChoiceFunction",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequest",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestAPICall",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestFunction",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestIntegration",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestSystem",
    "MainSwitchStepOutputSwitchThenGetStep",
    "MainSwitchStepOutputSwitchThenSetStep",
    "MainSwitchStepOutputSwitchThenLogStep",
    "MainSwitchStepOutputSwitchThenEmbedStep",
    "MainSwitchStepOutputSwitchThenEmbedStepEmbed",
    "MainSwitchStepOutputSwitchThenSearchStep",
    "MainSwitchStepOutputSwitchThenSearchStepSearch",
    "MainSwitchStepOutputSwitchThenSearchStepSearchVectorDocSearchRequest",
    "MainSwitchStepOutputSwitchThenSearchStepSearchTextOnlyDocSearchRequest",
    "MainSwitchStepOutputSwitchThenSearchStepSearchHybridDocSearchRequest",
    "MainSwitchStepOutputSwitchThenYieldStep",
    "MainSwitchStepOutputSwitchThenReturnStep",
    "MainSwitchStepOutputSwitchThenSleepStep",
    "MainSwitchStepOutputSwitchThenSleepStepSleep",
    "MainSwitchStepOutputSwitchThenErrorWorkflowStep",
    "MainSwitchStepOutputSwitchThenWaitForInputStep",
    "MainSwitchStepOutputSwitchThenWaitForInputStepWaitForInput",
    "MainForeachStepOutput",
    "MainForeachStepOutputForeach",
    "MainForeachStepOutputForeachDo",
    "MainForeachStepOutputForeachDoEvaluateStep",
    "MainForeachStepOutputForeachDoToolCallStep",
    "MainForeachStepOutputForeachDoPromptStepOutput",
    "MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0",
    "MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1",
    "MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1Content",
    "MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainForeachStepOutputForeachDoPromptStepOutputToolChoice",
    "MainForeachStepOutputForeachDoPromptStepOutputToolChoiceNamedToolChoice",
    "MainForeachStepOutputForeachDoPromptStepOutputToolChoiceNamedToolChoiceFunction",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequest",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestAPICall",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestFunction",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestIntegration",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestSystem",
    "MainForeachStepOutputForeachDoGetStep",
    "MainForeachStepOutputForeachDoSetStep",
    "MainForeachStepOutputForeachDoLogStep",
    "MainForeachStepOutputForeachDoEmbedStep",
    "MainForeachStepOutputForeachDoEmbedStepEmbed",
    "MainForeachStepOutputForeachDoSearchStep",
    "MainForeachStepOutputForeachDoSearchStepSearch",
    "MainForeachStepOutputForeachDoSearchStepSearchVectorDocSearchRequest",
    "MainForeachStepOutputForeachDoSearchStepSearchTextOnlyDocSearchRequest",
    "MainForeachStepOutputForeachDoSearchStepSearchHybridDocSearchRequest",
    "MainForeachStepOutputForeachDoYieldStep",
    "MainParallelStepOutput",
    "MainParallelStepOutputParallel",
    "MainParallelStepOutputParallelEvaluateStep",
    "MainParallelStepOutputParallelToolCallStep",
    "MainParallelStepOutputParallelPromptStepOutput",
    "MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0",
    "MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1",
    "MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1Content",
    "MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainParallelStepOutputParallelPromptStepOutputToolChoice",
    "MainParallelStepOutputParallelPromptStepOutputToolChoiceNamedToolChoice",
    "MainParallelStepOutputParallelPromptStepOutputToolChoiceNamedToolChoiceFunction",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequest",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestAPICall",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestFunction",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestIntegration",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestSystem",
    "MainParallelStepOutputParallelGetStep",
    "MainParallelStepOutputParallelSetStep",
    "MainParallelStepOutputParallelLogStep",
    "MainParallelStepOutputParallelEmbedStep",
    "MainParallelStepOutputParallelEmbedStepEmbed",
    "MainParallelStepOutputParallelSearchStep",
    "MainParallelStepOutputParallelSearchStepSearch",
    "MainParallelStepOutputParallelSearchStepSearchVectorDocSearchRequest",
    "MainParallelStepOutputParallelSearchStepSearchTextOnlyDocSearchRequest",
    "MainParallelStepOutputParallelSearchStepSearchHybridDocSearchRequest",
    "MainParallelStepOutputParallelYieldStep",
    "MainMainOutput",
    "MainMainOutputMap",
    "MainMainOutputMapEvaluateStep",
    "MainMainOutputMapToolCallStep",
    "MainMainOutputMapPromptStepOutput",
    "MainMainOutputMapPromptStepOutputPromptUnionMember0",
    "MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1",
    "MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1Content",
    "MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainMainOutputMapPromptStepOutputToolChoice",
    "MainMainOutputMapPromptStepOutputToolChoiceNamedToolChoice",
    "MainMainOutputMapPromptStepOutputToolChoiceNamedToolChoiceFunction",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequest",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestAPICall",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestFunction",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestIntegration",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestSystem",
    "MainMainOutputMapGetStep",
    "MainMainOutputMapSetStep",
    "MainMainOutputMapLogStep",
    "MainMainOutputMapEmbedStep",
    "MainMainOutputMapEmbedStepEmbed",
    "MainMainOutputMapSearchStep",
    "MainMainOutputMapSearchStepSearch",
    "MainMainOutputMapSearchStepSearchVectorDocSearchRequest",
    "MainMainOutputMapSearchStepSearchTextOnlyDocSearchRequest",
    "MainMainOutputMapSearchStepSearchHybridDocSearchRequest",
    "MainMainOutputMapYieldStep",
]


class MainEvaluateStep(BaseModel):
    evaluate: Dict[str, str]

    kind: Optional[Literal["evaluate"]] = FieldInfo(alias="kind_", default=None)


class MainToolCallStep(BaseModel):
    tool: str

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"], None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)


class MainPromptStepOutputPromptUnionMember0ContentUnionMember1Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MainPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MainPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel(BaseModel):
    image_url: MainPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MainPromptStepOutputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainPromptStepOutputPromptUnionMember0ContentUnionMember1Content,
    MainPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel,
]


class MainPromptStepOutputPromptUnionMember0(BaseModel):
    content: Union[List[str], List[MainPromptStepOutputPromptUnionMember0ContentUnionMember1], str]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class MainPromptStepOutputToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str


class MainPromptStepOutputToolChoiceNamedToolChoice(BaseModel):
    function: Optional[MainPromptStepOutputToolChoiceNamedToolChoiceFunction] = None


MainPromptStepOutputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainPromptStepOutputToolChoiceNamedToolChoice, None
]


class MainPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class MainPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


MainPromptStepOutputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID,
    MainPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainPromptStepOutputToolsUnionMember1ToolRef(BaseModel):
    ref: MainPromptStepOutputToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class MainPromptStepOutputToolsUnionMember1CreateToolRequestAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequest(BaseModel):
    name: str

    api_call: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestFunction] = None
    """Function definition"""

    integration: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestIntegration] = None
    """Integration definition"""

    system: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestSystem] = None
    """System definition"""


MainPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainPromptStepOutputToolsUnionMember1ToolRef, MainPromptStepOutputToolsUnionMember1CreateToolRequest
]


class MainPromptStepOutput(BaseModel):
    prompt: Union[List[MainPromptStepOutputPromptUnionMember0], str]

    forward_tool_results: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    settings: Optional[ChatSettings] = None

    tool_choice: Optional[MainPromptStepOutputToolChoice] = None

    tools: Union[Literal["all"], List[MainPromptStepOutputToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None


class MainGetStep(BaseModel):
    get: str

    kind: Optional[Literal["get"]] = FieldInfo(alias="kind_", default=None)


class MainSetStep(BaseModel):
    set: Dict[str, str]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)


class MainLogStep(BaseModel):
    log: str

    kind: Optional[Literal["log"]] = FieldInfo(alias="kind_", default=None)


class MainEmbedStepEmbed(BaseModel):
    text: Union[str, List[str]]


class MainEmbedStep(BaseModel):
    embed: MainEmbedStepEmbed

    kind: Optional[Literal["embed"]] = FieldInfo(alias="kind_", default=None)


class MainSearchStepSearchVectorDocSearchRequest(BaseModel):
    vector: List[float]

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainSearchStepSearchTextOnlyDocSearchRequest(BaseModel):
    text: str

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainSearchStepSearchHybridDocSearchRequest(BaseModel):
    text: str

    vector: List[float]

    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


MainSearchStepSearch: TypeAlias = Union[
    MainSearchStepSearchVectorDocSearchRequest,
    MainSearchStepSearchTextOnlyDocSearchRequest,
    MainSearchStepSearchHybridDocSearchRequest,
]


class MainSearchStep(BaseModel):
    search: MainSearchStepSearch

    kind: Optional[Literal["search"]] = FieldInfo(alias="kind_", default=None)


class MainYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


class MainReturnStep(BaseModel):
    return_: Dict[str, str] = FieldInfo(alias="return")

    kind: Optional[Literal["return"]] = FieldInfo(alias="kind_", default=None)


class MainSleepStepSleep(BaseModel):
    days: Optional[int] = None

    hours: Optional[int] = None

    minutes: Optional[int] = None

    seconds: Optional[int] = None


class MainSleepStep(BaseModel):
    sleep: MainSleepStepSleep

    kind: Optional[Literal["sleep"]] = FieldInfo(alias="kind_", default=None)


class MainErrorWorkflowStep(BaseModel):
    error: str

    kind: Optional[Literal["error"]] = FieldInfo(alias="kind_", default=None)


class MainWaitForInputStepWaitForInput(BaseModel):
    info: Dict[str, str]


class MainWaitForInputStep(BaseModel):
    wait_for_input: MainWaitForInputStepWaitForInput

    kind: Optional[Literal["wait_for_input"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenEvaluateStep(BaseModel):
    evaluate: Dict[str, str]

    kind: Optional[Literal["evaluate"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenToolCallStep(BaseModel):
    tool: str

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"], None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel(BaseModel):
    image_url: MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1Content,
    MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel,
]


class MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0(BaseModel):
    content: Union[
        List[str], List[MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0ContentUnionMember1], str
    ]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoiceNamedToolChoice(BaseModel):
    function: Optional[MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoiceNamedToolChoiceFunction] = None


MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoiceNamedToolChoice, None
]


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRef(BaseModel):
    ref: MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequest(BaseModel):
    name: str

    api_call: Optional[MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestFunction] = (
        None
    )
    """Function definition"""

    integration: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestIntegration
    ] = None
    """Integration definition"""

    system: Optional[MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestSystem] = None
    """System definition"""


MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequest,
]


class MainIfElseWorkflowStepOutputThenPromptStepOutput(BaseModel):
    prompt: Union[List[MainIfElseWorkflowStepOutputThenPromptStepOutputPromptUnionMember0], str]

    forward_tool_results: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    settings: Optional[ChatSettings] = None

    tool_choice: Optional[MainIfElseWorkflowStepOutputThenPromptStepOutputToolChoice] = None

    tools: Union[Literal["all"], List[MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None


class MainIfElseWorkflowStepOutputThenGetStep(BaseModel):
    get: str

    kind: Optional[Literal["get"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenSetStep(BaseModel):
    set: Dict[str, str]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenLogStep(BaseModel):
    log: str

    kind: Optional[Literal["log"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenEmbedStepEmbed(BaseModel):
    text: Union[str, List[str]]


class MainIfElseWorkflowStepOutputThenEmbedStep(BaseModel):
    embed: MainIfElseWorkflowStepOutputThenEmbedStepEmbed

    kind: Optional[Literal["embed"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenSearchStepSearchVectorDocSearchRequest(BaseModel):
    vector: List[float]

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainIfElseWorkflowStepOutputThenSearchStepSearchTextOnlyDocSearchRequest(BaseModel):
    text: str

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainIfElseWorkflowStepOutputThenSearchStepSearchHybridDocSearchRequest(BaseModel):
    text: str

    vector: List[float]

    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


MainIfElseWorkflowStepOutputThenSearchStepSearch: TypeAlias = Union[
    MainIfElseWorkflowStepOutputThenSearchStepSearchVectorDocSearchRequest,
    MainIfElseWorkflowStepOutputThenSearchStepSearchTextOnlyDocSearchRequest,
    MainIfElseWorkflowStepOutputThenSearchStepSearchHybridDocSearchRequest,
]


class MainIfElseWorkflowStepOutputThenSearchStep(BaseModel):
    search: MainIfElseWorkflowStepOutputThenSearchStepSearch

    kind: Optional[Literal["search"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenReturnStep(BaseModel):
    return_: Dict[str, str] = FieldInfo(alias="return")

    kind: Optional[Literal["return"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenSleepStepSleep(BaseModel):
    days: Optional[int] = None

    hours: Optional[int] = None

    minutes: Optional[int] = None

    seconds: Optional[int] = None


class MainIfElseWorkflowStepOutputThenSleepStep(BaseModel):
    sleep: MainIfElseWorkflowStepOutputThenSleepStepSleep

    kind: Optional[Literal["sleep"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenErrorWorkflowStep(BaseModel):
    error: str

    kind: Optional[Literal["error"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputThenWaitForInputStepWaitForInput(BaseModel):
    info: Dict[str, str]


class MainIfElseWorkflowStepOutputThenWaitForInputStep(BaseModel):
    wait_for_input: MainIfElseWorkflowStepOutputThenWaitForInputStepWaitForInput

    kind: Optional[Literal["wait_for_input"]] = FieldInfo(alias="kind_", default=None)


MainIfElseWorkflowStepOutputThen: TypeAlias = Union[
    MainIfElseWorkflowStepOutputThenEvaluateStep,
    MainIfElseWorkflowStepOutputThenToolCallStep,
    MainIfElseWorkflowStepOutputThenPromptStepOutput,
    MainIfElseWorkflowStepOutputThenGetStep,
    MainIfElseWorkflowStepOutputThenSetStep,
    MainIfElseWorkflowStepOutputThenLogStep,
    MainIfElseWorkflowStepOutputThenEmbedStep,
    MainIfElseWorkflowStepOutputThenSearchStep,
    MainIfElseWorkflowStepOutputThenYieldStep,
    MainIfElseWorkflowStepOutputThenReturnStep,
    MainIfElseWorkflowStepOutputThenSleepStep,
    MainIfElseWorkflowStepOutputThenErrorWorkflowStep,
    MainIfElseWorkflowStepOutputThenWaitForInputStep,
]


class MainIfElseWorkflowStepOutputElseEvaluateStep(BaseModel):
    evaluate: Dict[str, str]

    kind: Optional[Literal["evaluate"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseToolCallStep(BaseModel):
    tool: str

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"], None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel(BaseModel):
    image_url: MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1Content,
    MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel,
]


class MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0(BaseModel):
    content: Union[
        List[str], List[MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0ContentUnionMember1], str
    ]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoiceNamedToolChoice(BaseModel):
    function: Optional[MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoiceNamedToolChoiceFunction] = None


MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoiceNamedToolChoice, None
]


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRefToolRefByID,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRef(BaseModel):
    ref: MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequest(BaseModel):
    name: str

    api_call: Optional[MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestFunction] = (
        None
    )
    """Function definition"""

    integration: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestIntegration
    ] = None
    """Integration definition"""

    system: Optional[MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestSystem] = None
    """System definition"""


MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequest,
]


class MainIfElseWorkflowStepOutputElsePromptStepOutput(BaseModel):
    prompt: Union[List[MainIfElseWorkflowStepOutputElsePromptStepOutputPromptUnionMember0], str]

    forward_tool_results: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    settings: Optional[ChatSettings] = None

    tool_choice: Optional[MainIfElseWorkflowStepOutputElsePromptStepOutputToolChoice] = None

    tools: Union[Literal["all"], List[MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None


class MainIfElseWorkflowStepOutputElseGetStep(BaseModel):
    get: str

    kind: Optional[Literal["get"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseSetStep(BaseModel):
    set: Dict[str, str]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseLogStep(BaseModel):
    log: str

    kind: Optional[Literal["log"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseEmbedStepEmbed(BaseModel):
    text: Union[str, List[str]]


class MainIfElseWorkflowStepOutputElseEmbedStep(BaseModel):
    embed: MainIfElseWorkflowStepOutputElseEmbedStepEmbed

    kind: Optional[Literal["embed"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseSearchStepSearchVectorDocSearchRequest(BaseModel):
    vector: List[float]

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainIfElseWorkflowStepOutputElseSearchStepSearchTextOnlyDocSearchRequest(BaseModel):
    text: str

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainIfElseWorkflowStepOutputElseSearchStepSearchHybridDocSearchRequest(BaseModel):
    text: str

    vector: List[float]

    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


MainIfElseWorkflowStepOutputElseSearchStepSearch: TypeAlias = Union[
    MainIfElseWorkflowStepOutputElseSearchStepSearchVectorDocSearchRequest,
    MainIfElseWorkflowStepOutputElseSearchStepSearchTextOnlyDocSearchRequest,
    MainIfElseWorkflowStepOutputElseSearchStepSearchHybridDocSearchRequest,
]


class MainIfElseWorkflowStepOutputElseSearchStep(BaseModel):
    search: MainIfElseWorkflowStepOutputElseSearchStepSearch

    kind: Optional[Literal["search"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseReturnStep(BaseModel):
    return_: Dict[str, str] = FieldInfo(alias="return")

    kind: Optional[Literal["return"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseSleepStepSleep(BaseModel):
    days: Optional[int] = None

    hours: Optional[int] = None

    minutes: Optional[int] = None

    seconds: Optional[int] = None


class MainIfElseWorkflowStepOutputElseSleepStep(BaseModel):
    sleep: MainIfElseWorkflowStepOutputElseSleepStepSleep

    kind: Optional[Literal["sleep"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseErrorWorkflowStep(BaseModel):
    error: str

    kind: Optional[Literal["error"]] = FieldInfo(alias="kind_", default=None)


class MainIfElseWorkflowStepOutputElseWaitForInputStepWaitForInput(BaseModel):
    info: Dict[str, str]


class MainIfElseWorkflowStepOutputElseWaitForInputStep(BaseModel):
    wait_for_input: MainIfElseWorkflowStepOutputElseWaitForInputStepWaitForInput

    kind: Optional[Literal["wait_for_input"]] = FieldInfo(alias="kind_", default=None)


MainIfElseWorkflowStepOutputElse: TypeAlias = Union[
    MainIfElseWorkflowStepOutputElseEvaluateStep,
    MainIfElseWorkflowStepOutputElseToolCallStep,
    MainIfElseWorkflowStepOutputElsePromptStepOutput,
    MainIfElseWorkflowStepOutputElseGetStep,
    MainIfElseWorkflowStepOutputElseSetStep,
    MainIfElseWorkflowStepOutputElseLogStep,
    MainIfElseWorkflowStepOutputElseEmbedStep,
    MainIfElseWorkflowStepOutputElseSearchStep,
    MainIfElseWorkflowStepOutputElseYieldStep,
    MainIfElseWorkflowStepOutputElseReturnStep,
    MainIfElseWorkflowStepOutputElseSleepStep,
    MainIfElseWorkflowStepOutputElseErrorWorkflowStep,
    MainIfElseWorkflowStepOutputElseWaitForInputStep,
    None,
]


class MainIfElseWorkflowStepOutput(BaseModel):
    if_: str = FieldInfo(alias="if")

    then: MainIfElseWorkflowStepOutputThen

    else_: Optional[MainIfElseWorkflowStepOutputElse] = FieldInfo(alias="else", default=None)

    kind: Optional[Literal["if_else"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenEvaluateStep(BaseModel):
    evaluate: Dict[str, str]

    kind: Optional[Literal["evaluate"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenToolCallStep(BaseModel):
    tool: str

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"], None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel(BaseModel):
    image_url: MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1Content,
    MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel,
]


class MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0(BaseModel):
    content: Union[
        List[str], List[MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0ContentUnionMember1], str
    ]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolChoiceNamedToolChoice(BaseModel):
    function: Optional[MainSwitchStepOutputSwitchThenPromptStepOutputToolChoiceNamedToolChoiceFunction] = None


MainSwitchStepOutputSwitchThenPromptStepOutputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainSwitchStepOutputSwitchThenPromptStepOutputToolChoiceNamedToolChoice, None
]


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRef(BaseModel):
    ref: MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequest(BaseModel):
    name: str

    api_call: Optional[MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestFunction] = None
    """Function definition"""

    integration: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestIntegration
    ] = None
    """Integration definition"""

    system: Optional[MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestSystem] = None
    """System definition"""


MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRef,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequest,
]


class MainSwitchStepOutputSwitchThenPromptStepOutput(BaseModel):
    prompt: Union[List[MainSwitchStepOutputSwitchThenPromptStepOutputPromptUnionMember0], str]

    forward_tool_results: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    settings: Optional[ChatSettings] = None

    tool_choice: Optional[MainSwitchStepOutputSwitchThenPromptStepOutputToolChoice] = None

    tools: Union[Literal["all"], List[MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None


class MainSwitchStepOutputSwitchThenGetStep(BaseModel):
    get: str

    kind: Optional[Literal["get"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenSetStep(BaseModel):
    set: Dict[str, str]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenLogStep(BaseModel):
    log: str

    kind: Optional[Literal["log"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenEmbedStepEmbed(BaseModel):
    text: Union[str, List[str]]


class MainSwitchStepOutputSwitchThenEmbedStep(BaseModel):
    embed: MainSwitchStepOutputSwitchThenEmbedStepEmbed

    kind: Optional[Literal["embed"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenSearchStepSearchVectorDocSearchRequest(BaseModel):
    vector: List[float]

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainSwitchStepOutputSwitchThenSearchStepSearchTextOnlyDocSearchRequest(BaseModel):
    text: str

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainSwitchStepOutputSwitchThenSearchStepSearchHybridDocSearchRequest(BaseModel):
    text: str

    vector: List[float]

    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


MainSwitchStepOutputSwitchThenSearchStepSearch: TypeAlias = Union[
    MainSwitchStepOutputSwitchThenSearchStepSearchVectorDocSearchRequest,
    MainSwitchStepOutputSwitchThenSearchStepSearchTextOnlyDocSearchRequest,
    MainSwitchStepOutputSwitchThenSearchStepSearchHybridDocSearchRequest,
]


class MainSwitchStepOutputSwitchThenSearchStep(BaseModel):
    search: MainSwitchStepOutputSwitchThenSearchStepSearch

    kind: Optional[Literal["search"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenReturnStep(BaseModel):
    return_: Dict[str, str] = FieldInfo(alias="return")

    kind: Optional[Literal["return"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenSleepStepSleep(BaseModel):
    days: Optional[int] = None

    hours: Optional[int] = None

    minutes: Optional[int] = None

    seconds: Optional[int] = None


class MainSwitchStepOutputSwitchThenSleepStep(BaseModel):
    sleep: MainSwitchStepOutputSwitchThenSleepStepSleep

    kind: Optional[Literal["sleep"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenErrorWorkflowStep(BaseModel):
    error: str

    kind: Optional[Literal["error"]] = FieldInfo(alias="kind_", default=None)


class MainSwitchStepOutputSwitchThenWaitForInputStepWaitForInput(BaseModel):
    info: Dict[str, str]


class MainSwitchStepOutputSwitchThenWaitForInputStep(BaseModel):
    wait_for_input: MainSwitchStepOutputSwitchThenWaitForInputStepWaitForInput

    kind: Optional[Literal["wait_for_input"]] = FieldInfo(alias="kind_", default=None)


MainSwitchStepOutputSwitchThen: TypeAlias = Union[
    MainSwitchStepOutputSwitchThenEvaluateStep,
    MainSwitchStepOutputSwitchThenToolCallStep,
    MainSwitchStepOutputSwitchThenPromptStepOutput,
    MainSwitchStepOutputSwitchThenGetStep,
    MainSwitchStepOutputSwitchThenSetStep,
    MainSwitchStepOutputSwitchThenLogStep,
    MainSwitchStepOutputSwitchThenEmbedStep,
    MainSwitchStepOutputSwitchThenSearchStep,
    MainSwitchStepOutputSwitchThenYieldStep,
    MainSwitchStepOutputSwitchThenReturnStep,
    MainSwitchStepOutputSwitchThenSleepStep,
    MainSwitchStepOutputSwitchThenErrorWorkflowStep,
    MainSwitchStepOutputSwitchThenWaitForInputStep,
]


class MainSwitchStepOutputSwitch(BaseModel):
    case: Union[Literal["_"], str]

    then: MainSwitchStepOutputSwitchThen


class MainSwitchStepOutput(BaseModel):
    switch: List[MainSwitchStepOutputSwitch]

    kind: Optional[Literal["switch"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoEvaluateStep(BaseModel):
    evaluate: Dict[str, str]

    kind: Optional[Literal["evaluate"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoToolCallStep(BaseModel):
    tool: str

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"], None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel(BaseModel):
    image_url: MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1Content,
    MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel,
]


class MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0(BaseModel):
    content: Union[
        List[str], List[MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0ContentUnionMember1], str
    ]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str


class MainForeachStepOutputForeachDoPromptStepOutputToolChoiceNamedToolChoice(BaseModel):
    function: Optional[MainForeachStepOutputForeachDoPromptStepOutputToolChoiceNamedToolChoiceFunction] = None


MainForeachStepOutputForeachDoPromptStepOutputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainForeachStepOutputForeachDoPromptStepOutputToolChoiceNamedToolChoice, None
]


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRef(BaseModel):
    ref: MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequest(BaseModel):
    name: str

    api_call: Optional[MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestFunction] = None
    """Function definition"""

    integration: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestIntegration
    ] = None
    """Integration definition"""

    system: Optional[MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestSystem] = None
    """System definition"""


MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRef,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequest,
]


class MainForeachStepOutputForeachDoPromptStepOutput(BaseModel):
    prompt: Union[List[MainForeachStepOutputForeachDoPromptStepOutputPromptUnionMember0], str]

    forward_tool_results: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    settings: Optional[ChatSettings] = None

    tool_choice: Optional[MainForeachStepOutputForeachDoPromptStepOutputToolChoice] = None

    tools: Union[Literal["all"], List[MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None


class MainForeachStepOutputForeachDoGetStep(BaseModel):
    get: str

    kind: Optional[Literal["get"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoSetStep(BaseModel):
    set: Dict[str, str]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoLogStep(BaseModel):
    log: str

    kind: Optional[Literal["log"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoEmbedStepEmbed(BaseModel):
    text: Union[str, List[str]]


class MainForeachStepOutputForeachDoEmbedStep(BaseModel):
    embed: MainForeachStepOutputForeachDoEmbedStepEmbed

    kind: Optional[Literal["embed"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoSearchStepSearchVectorDocSearchRequest(BaseModel):
    vector: List[float]

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainForeachStepOutputForeachDoSearchStepSearchTextOnlyDocSearchRequest(BaseModel):
    text: str

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainForeachStepOutputForeachDoSearchStepSearchHybridDocSearchRequest(BaseModel):
    text: str

    vector: List[float]

    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


MainForeachStepOutputForeachDoSearchStepSearch: TypeAlias = Union[
    MainForeachStepOutputForeachDoSearchStepSearchVectorDocSearchRequest,
    MainForeachStepOutputForeachDoSearchStepSearchTextOnlyDocSearchRequest,
    MainForeachStepOutputForeachDoSearchStepSearchHybridDocSearchRequest,
]


class MainForeachStepOutputForeachDoSearchStep(BaseModel):
    search: MainForeachStepOutputForeachDoSearchStepSearch

    kind: Optional[Literal["search"]] = FieldInfo(alias="kind_", default=None)


class MainForeachStepOutputForeachDoYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


MainForeachStepOutputForeachDo: TypeAlias = Union[
    MainForeachStepOutputForeachDoEvaluateStep,
    MainForeachStepOutputForeachDoToolCallStep,
    MainForeachStepOutputForeachDoPromptStepOutput,
    MainForeachStepOutputForeachDoGetStep,
    MainForeachStepOutputForeachDoSetStep,
    MainForeachStepOutputForeachDoLogStep,
    MainForeachStepOutputForeachDoEmbedStep,
    MainForeachStepOutputForeachDoSearchStep,
    MainForeachStepOutputForeachDoYieldStep,
]


class MainForeachStepOutputForeach(BaseModel):
    do: MainForeachStepOutputForeachDo

    in_: str = FieldInfo(alias="in")


class MainForeachStepOutput(BaseModel):
    foreach: MainForeachStepOutputForeach

    kind: Optional[Literal["foreach"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelEvaluateStep(BaseModel):
    evaluate: Dict[str, str]

    kind: Optional[Literal["evaluate"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelToolCallStep(BaseModel):
    tool: str

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"], None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel(BaseModel):
    image_url: MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1Content,
    MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel,
]


class MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0(BaseModel):
    content: Union[
        List[str], List[MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0ContentUnionMember1], str
    ]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class MainParallelStepOutputParallelPromptStepOutputToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str


class MainParallelStepOutputParallelPromptStepOutputToolChoiceNamedToolChoice(BaseModel):
    function: Optional[MainParallelStepOutputParallelPromptStepOutputToolChoiceNamedToolChoiceFunction] = None


MainParallelStepOutputParallelPromptStepOutputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainParallelStepOutputParallelPromptStepOutputToolChoiceNamedToolChoice, None
]


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRef(BaseModel):
    ref: MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequest(BaseModel):
    name: str

    api_call: Optional[MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestFunction] = None
    """Function definition"""

    integration: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestIntegration
    ] = None
    """Integration definition"""

    system: Optional[MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestSystem] = None
    """System definition"""


MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRef,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequest,
]


class MainParallelStepOutputParallelPromptStepOutput(BaseModel):
    prompt: Union[List[MainParallelStepOutputParallelPromptStepOutputPromptUnionMember0], str]

    forward_tool_results: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    settings: Optional[ChatSettings] = None

    tool_choice: Optional[MainParallelStepOutputParallelPromptStepOutputToolChoice] = None

    tools: Union[Literal["all"], List[MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None


class MainParallelStepOutputParallelGetStep(BaseModel):
    get: str

    kind: Optional[Literal["get"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelSetStep(BaseModel):
    set: Dict[str, str]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelLogStep(BaseModel):
    log: str

    kind: Optional[Literal["log"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelEmbedStepEmbed(BaseModel):
    text: Union[str, List[str]]


class MainParallelStepOutputParallelEmbedStep(BaseModel):
    embed: MainParallelStepOutputParallelEmbedStepEmbed

    kind: Optional[Literal["embed"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelSearchStepSearchVectorDocSearchRequest(BaseModel):
    vector: List[float]

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainParallelStepOutputParallelSearchStepSearchTextOnlyDocSearchRequest(BaseModel):
    text: str

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainParallelStepOutputParallelSearchStepSearchHybridDocSearchRequest(BaseModel):
    text: str

    vector: List[float]

    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


MainParallelStepOutputParallelSearchStepSearch: TypeAlias = Union[
    MainParallelStepOutputParallelSearchStepSearchVectorDocSearchRequest,
    MainParallelStepOutputParallelSearchStepSearchTextOnlyDocSearchRequest,
    MainParallelStepOutputParallelSearchStepSearchHybridDocSearchRequest,
]


class MainParallelStepOutputParallelSearchStep(BaseModel):
    search: MainParallelStepOutputParallelSearchStepSearch

    kind: Optional[Literal["search"]] = FieldInfo(alias="kind_", default=None)


class MainParallelStepOutputParallelYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


MainParallelStepOutputParallel: TypeAlias = Union[
    MainParallelStepOutputParallelEvaluateStep,
    MainParallelStepOutputParallelToolCallStep,
    MainParallelStepOutputParallelPromptStepOutput,
    MainParallelStepOutputParallelGetStep,
    MainParallelStepOutputParallelSetStep,
    MainParallelStepOutputParallelLogStep,
    MainParallelStepOutputParallelEmbedStep,
    MainParallelStepOutputParallelSearchStep,
    MainParallelStepOutputParallelYieldStep,
]


class MainParallelStepOutput(BaseModel):
    parallel: List[MainParallelStepOutputParallel]

    kind: Optional[Literal["parallel"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapEvaluateStep(BaseModel):
    evaluate: Dict[str, str]

    kind: Optional[Literal["evaluate"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapToolCallStep(BaseModel):
    tool: str

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"], None] = None

    kind: Optional[Literal["tool_call"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1Content(BaseModel):
    text: str

    type: Optional[Literal["text"]] = None


class MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL(BaseModel):
    url: str

    detail: Optional[Literal["low", "high", "auto"]] = None


class MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel(BaseModel):
    image_url: MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    """The image URL"""

    type: Optional[Literal["image_url"]] = None


MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1Content,
    MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1ContentModel,
]


class MainMainOutputMapPromptStepOutputPromptUnionMember0(BaseModel):
    content: Union[List[str], List[MainMainOutputMapPromptStepOutputPromptUnionMember0ContentUnionMember1], str]

    role: Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]

    continue_: Optional[bool] = FieldInfo(alias="continue", default=None)

    name: Optional[str] = None


class MainMainOutputMapPromptStepOutputToolChoiceNamedToolChoiceFunction(BaseModel):
    name: str


class MainMainOutputMapPromptStepOutputToolChoiceNamedToolChoice(BaseModel):
    function: Optional[MainMainOutputMapPromptStepOutputToolChoiceNamedToolChoiceFunction] = None


MainMainOutputMapPromptStepOutputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainMainOutputMapPromptStepOutputToolChoiceNamedToolChoice, None
]


class MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID(BaseModel):
    id: Optional[str] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName(BaseModel):
    name: Optional[str] = None


MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRefToolRefByID,
    MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRef(BaseModel):
    ref: MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRefRef
    """Reference to a tool by id"""


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[Dict[str, str]] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestIntegration(BaseModel):
    provider: Union[Literal["dummy", "hacker_news", "weather", "wikipedia", "spider", "brave", "browserbase"], str]

    arguments: Optional[object] = None

    method: Optional[str] = None

    setup: Optional[object] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestSystem(BaseModel):
    call: str

    arguments: Optional[object] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequest(BaseModel):
    name: str

    api_call: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestFunction] = None
    """Function definition"""

    integration: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestIntegration] = None
    """Integration definition"""

    system: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestSystem] = None
    """System definition"""


MainMainOutputMapPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRef,
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequest,
]


class MainMainOutputMapPromptStepOutput(BaseModel):
    prompt: Union[List[MainMainOutputMapPromptStepOutputPromptUnionMember0], str]

    forward_tool_results: Optional[bool] = None

    kind: Optional[Literal["prompt"]] = FieldInfo(alias="kind_", default=None)

    settings: Optional[ChatSettings] = None

    tool_choice: Optional[MainMainOutputMapPromptStepOutputToolChoice] = None

    tools: Union[Literal["all"], List[MainMainOutputMapPromptStepOutputToolsUnionMember1], None] = None

    unwrap: Optional[bool] = None


class MainMainOutputMapGetStep(BaseModel):
    get: str

    kind: Optional[Literal["get"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapSetStep(BaseModel):
    set: Dict[str, str]

    kind: Optional[Literal["set"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapLogStep(BaseModel):
    log: str

    kind: Optional[Literal["log"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapEmbedStepEmbed(BaseModel):
    text: Union[str, List[str]]


class MainMainOutputMapEmbedStep(BaseModel):
    embed: MainMainOutputMapEmbedStepEmbed

    kind: Optional[Literal["embed"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapSearchStepSearchVectorDocSearchRequest(BaseModel):
    vector: List[float]

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainMainOutputMapSearchStepSearchTextOnlyDocSearchRequest(BaseModel):
    text: str

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


class MainMainOutputMapSearchStepSearchHybridDocSearchRequest(BaseModel):
    text: str

    vector: List[float]

    alpha: Optional[float] = None

    confidence: Optional[float] = None

    lang: Optional[Literal["en-US"]] = None

    limit: Optional[int] = None


MainMainOutputMapSearchStepSearch: TypeAlias = Union[
    MainMainOutputMapSearchStepSearchVectorDocSearchRequest,
    MainMainOutputMapSearchStepSearchTextOnlyDocSearchRequest,
    MainMainOutputMapSearchStepSearchHybridDocSearchRequest,
]


class MainMainOutputMapSearchStep(BaseModel):
    search: MainMainOutputMapSearchStepSearch

    kind: Optional[Literal["search"]] = FieldInfo(alias="kind_", default=None)


class MainMainOutputMapYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


MainMainOutputMap: TypeAlias = Union[
    MainMainOutputMapEvaluateStep,
    MainMainOutputMapToolCallStep,
    MainMainOutputMapPromptStepOutput,
    MainMainOutputMapGetStep,
    MainMainOutputMapSetStep,
    MainMainOutputMapLogStep,
    MainMainOutputMapEmbedStep,
    MainMainOutputMapSearchStep,
    MainMainOutputMapYieldStep,
]


class MainMainOutput(BaseModel):
    map: MainMainOutputMap

    over: str

    initial: Optional[object] = None

    kind: Optional[Literal["map_reduce"]] = FieldInfo(alias="kind_", default=None)

    parallelism: Optional[int] = None

    reduce: Optional[str] = None


Main: TypeAlias = Union[
    MainEvaluateStep,
    MainToolCallStep,
    MainPromptStepOutput,
    MainGetStep,
    MainSetStep,
    MainLogStep,
    MainEmbedStep,
    MainSearchStep,
    MainYieldStep,
    MainReturnStep,
    MainSleepStep,
    MainErrorWorkflowStep,
    MainWaitForInputStep,
    MainIfElseWorkflowStepOutput,
    MainSwitchStepOutput,
    MainForeachStepOutput,
    MainParallelStepOutput,
    MainMainOutput,
]


class Task(BaseModel):
    id: str

    created_at: datetime

    main: List[Main]

    name: str

    updated_at: datetime

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

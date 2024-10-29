# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

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
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutput",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup",
    "MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem",
    "MainGetStep",
    "MainSetStep",
    "MainLogStep",
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
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutput",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem",
    "MainIfElseWorkflowStepOutputThenGetStep",
    "MainIfElseWorkflowStepOutputThenSetStep",
    "MainIfElseWorkflowStepOutputThenLogStep",
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
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutput",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup",
    "MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem",
    "MainIfElseWorkflowStepOutputElseGetStep",
    "MainIfElseWorkflowStepOutputElseSetStep",
    "MainIfElseWorkflowStepOutputElseLogStep",
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
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutput",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup",
    "MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem",
    "MainSwitchStepOutputSwitchThenGetStep",
    "MainSwitchStepOutputSwitchThenSetStep",
    "MainSwitchStepOutputSwitchThenLogStep",
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
    "MainForeachStepOutputForeachDoWaitForInputStep",
    "MainForeachStepOutputForeachDoWaitForInputStepWaitForInput",
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
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutput",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup",
    "MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem",
    "MainForeachStepOutputForeachDoGetStep",
    "MainForeachStepOutputForeachDoSetStep",
    "MainForeachStepOutputForeachDoLogStep",
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
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutput",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup",
    "MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem",
    "MainParallelStepOutputParallelGetStep",
    "MainParallelStepOutputParallelSetStep",
    "MainParallelStepOutputParallelLogStep",
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
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutput",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup",
    "MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem",
    "MainMainOutputMapGetStep",
    "MainMainOutputMapSetStep",
    "MainMainOutputMapLogStep",
    "MainMainOutputMapYieldStep",
    "Tool",
    "ToolAPICall",
    "ToolFunction",
    "ToolIntegration",
    "ToolIntegrationDummyIntegrationDef",
    "ToolIntegrationBraveIntegrationDef",
    "ToolIntegrationBraveIntegrationDefArguments",
    "ToolIntegrationBraveIntegrationDefSetup",
    "ToolIntegrationEmailIntegrationDef",
    "ToolIntegrationEmailIntegrationDefArguments",
    "ToolIntegrationEmailIntegrationDefSetup",
    "ToolIntegrationSpiderIntegrationDef",
    "ToolIntegrationSpiderIntegrationDefArguments",
    "ToolIntegrationSpiderIntegrationDefSetup",
    "ToolIntegrationWikipediaIntegrationDef",
    "ToolIntegrationWikipediaIntegrationDefArguments",
    "ToolIntegrationWeatherIntegrationDef",
    "ToolIntegrationWeatherIntegrationDefArguments",
    "ToolIntegrationWeatherIntegrationDefSetup",
    "ToolSystem",
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


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[
        MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments
    ] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup] = (
        None
    )
    """Integration definition for Brave Search"""


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[
        MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments
    ] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup] = (
        None
    )
    """Setup parameters for Email integration"""


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[
        MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments
    ] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[
        MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup
    ] = None
    """Setup parameters for Spider integration"""


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments(
    BaseModel
):
    query: str

    load_max_docs: Optional[int] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[
        MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments
    ] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[
        MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments
    ] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[
        MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup
    ] = None
    """Integration definition for Weather"""


MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration: TypeAlias = Union[
    MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef,
    MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef,
    MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef,
    MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef,
    MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef,
    MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef,
    None,
]


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class MainPromptStepOutputToolsUnionMember1CreateToolRequestOutput(BaseModel):
    name: str

    api_call: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction] = None
    """Function definition"""

    integration: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration] = None
    """Brave integration definition"""

    system: Optional[MainPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem] = None
    """System definition"""


MainPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainPromptStepOutputToolsUnionMember1ToolRef, MainPromptStepOutputToolsUnionMember1CreateToolRequestOutput
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


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef(
    BaseModel
):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments(
    BaseModel
):
    query: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup(
    BaseModel
):
    api_key: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments
    ] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup
    ] = None
    """Integration definition for Brave Search"""


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments(
    BaseModel
):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup(
    BaseModel
):
    host: str

    password: str

    port: int

    user: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments
    ] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup
    ] = None
    """Setup parameters for Email integration"""


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments(
    BaseModel
):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup(
    BaseModel
):
    spider_api_key: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments
    ] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup
    ] = None
    """Setup parameters for Spider integration"""


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments(
    BaseModel
):
    query: str

    load_max_docs: Optional[int] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments
    ] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments(
    BaseModel
):
    location: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup(
    BaseModel
):
    openweathermap_api_key: str


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments
    ] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup
    ] = None
    """Integration definition for Weather"""


MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration: TypeAlias = Union[
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef,
    None,
]


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutput(BaseModel):
    name: str

    api_call: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall
    ] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction
    ] = None
    """Function definition"""

    integration: Optional[
        MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration
    ] = None
    """Brave integration definition"""

    system: Optional[MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem] = (
        None
    )
    """System definition"""


MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepOutputThenPromptStepOutputToolsUnionMember1CreateToolRequestOutput,
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


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef(
    BaseModel
):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments(
    BaseModel
):
    query: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup(
    BaseModel
):
    api_key: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments
    ] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup
    ] = None
    """Integration definition for Brave Search"""


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments(
    BaseModel
):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup(
    BaseModel
):
    host: str

    password: str

    port: int

    user: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments
    ] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup
    ] = None
    """Setup parameters for Email integration"""


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments(
    BaseModel
):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup(
    BaseModel
):
    spider_api_key: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments
    ] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup
    ] = None
    """Setup parameters for Spider integration"""


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments(
    BaseModel
):
    query: str

    load_max_docs: Optional[int] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments
    ] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments(
    BaseModel
):
    location: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup(
    BaseModel
):
    openweathermap_api_key: str


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments
    ] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup
    ] = None
    """Integration definition for Weather"""


MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration: TypeAlias = Union[
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef,
    None,
]


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutput(BaseModel):
    name: str

    api_call: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall
    ] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction
    ] = None
    """Function definition"""

    integration: Optional[
        MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration
    ] = None
    """Brave integration definition"""

    system: Optional[MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem] = (
        None
    )
    """System definition"""


MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepOutputElsePromptStepOutputToolsUnionMember1CreateToolRequestOutput,
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


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef(
    BaseModel
):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments(
    BaseModel
):
    query: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup(
    BaseModel
):
    api_key: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments
    ] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup
    ] = None
    """Integration definition for Brave Search"""


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments(
    BaseModel
):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup(
    BaseModel
):
    host: str

    password: str

    port: int

    user: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments
    ] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup
    ] = None
    """Setup parameters for Email integration"""


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments(
    BaseModel
):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup(
    BaseModel
):
    spider_api_key: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments
    ] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup
    ] = None
    """Setup parameters for Spider integration"""


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments(
    BaseModel
):
    query: str

    load_max_docs: Optional[int] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments
    ] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments(
    BaseModel
):
    location: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup(
    BaseModel
):
    openweathermap_api_key: str


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments
    ] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup
    ] = None
    """Integration definition for Weather"""


MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration: TypeAlias = Union[
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef,
    None,
]


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutput(BaseModel):
    name: str

    api_call: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall
    ] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction
    ] = None
    """Function definition"""

    integration: Optional[
        MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration
    ] = None
    """Brave integration definition"""

    system: Optional[MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem] = (
        None
    )
    """System definition"""


MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1ToolRef,
    MainSwitchStepOutputSwitchThenPromptStepOutputToolsUnionMember1CreateToolRequestOutput,
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


class MainForeachStepOutputForeachDoWaitForInputStepWaitForInput(BaseModel):
    info: Dict[str, str]


class MainForeachStepOutputForeachDoWaitForInputStep(BaseModel):
    wait_for_input: MainForeachStepOutputForeachDoWaitForInputStepWaitForInput

    kind: Optional[Literal["wait_for_input"]] = FieldInfo(alias="kind_", default=None)


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


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef(
    BaseModel
):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments(
    BaseModel
):
    query: str


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup(
    BaseModel
):
    api_key: str


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments
    ] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup
    ] = None
    """Integration definition for Brave Search"""


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments(
    BaseModel
):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup(
    BaseModel
):
    host: str

    password: str

    port: int

    user: str


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments
    ] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup
    ] = None
    """Setup parameters for Email integration"""


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments(
    BaseModel
):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup(
    BaseModel
):
    spider_api_key: str


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments
    ] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup
    ] = None
    """Setup parameters for Spider integration"""


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments(
    BaseModel
):
    query: str

    load_max_docs: Optional[int] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments
    ] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments(
    BaseModel
):
    location: str


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup(
    BaseModel
):
    openweathermap_api_key: str


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments
    ] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup
    ] = None
    """Integration definition for Weather"""


MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration: TypeAlias = Union[
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef,
    None,
]


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutput(BaseModel):
    name: str

    api_call: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall
    ] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction
    ] = None
    """Function definition"""

    integration: Optional[
        MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration
    ] = None
    """Brave integration definition"""

    system: Optional[MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem] = (
        None
    )
    """System definition"""


MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1ToolRef,
    MainForeachStepOutputForeachDoPromptStepOutputToolsUnionMember1CreateToolRequestOutput,
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


class MainForeachStepOutputForeachDoYieldStep(BaseModel):
    workflow: str

    arguments: Union[Dict[str, str], Literal["_"], None] = None

    kind: Optional[Literal["yield"]] = FieldInfo(alias="kind_", default=None)


MainForeachStepOutputForeachDo: TypeAlias = Union[
    MainForeachStepOutputForeachDoWaitForInputStep,
    MainForeachStepOutputForeachDoEvaluateStep,
    MainForeachStepOutputForeachDoToolCallStep,
    MainForeachStepOutputForeachDoPromptStepOutput,
    MainForeachStepOutputForeachDoGetStep,
    MainForeachStepOutputForeachDoSetStep,
    MainForeachStepOutputForeachDoLogStep,
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


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef(
    BaseModel
):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments(
    BaseModel
):
    query: str


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup(
    BaseModel
):
    api_key: str


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments
    ] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup
    ] = None
    """Integration definition for Brave Search"""


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments(
    BaseModel
):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup(
    BaseModel
):
    host: str

    password: str

    port: int

    user: str


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments
    ] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup
    ] = None
    """Setup parameters for Email integration"""


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments(
    BaseModel
):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup(
    BaseModel
):
    spider_api_key: str


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments
    ] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup
    ] = None
    """Setup parameters for Spider integration"""


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments(
    BaseModel
):
    query: str

    load_max_docs: Optional[int] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments
    ] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments(
    BaseModel
):
    location: str


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup(
    BaseModel
):
    openweathermap_api_key: str


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments
    ] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup
    ] = None
    """Integration definition for Weather"""


MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration: TypeAlias = Union[
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef,
    None,
]


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutput(BaseModel):
    name: str

    api_call: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall
    ] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction
    ] = None
    """Function definition"""

    integration: Optional[
        MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration
    ] = None
    """Brave integration definition"""

    system: Optional[MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem] = (
        None
    )
    """System definition"""


MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1ToolRef,
    MainParallelStepOutputParallelPromptStepOutputToolsUnionMember1CreateToolRequestOutput,
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


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef(
    BaseModel
):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments(
    BaseModel
):
    query: str


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup(
    BaseModel
):
    api_key: str


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefArguments
    ] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDefSetup
    ] = None
    """Integration definition for Brave Search"""


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments(
    BaseModel
):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup(
    BaseModel
):
    host: str

    password: str

    port: int

    user: str


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefArguments
    ] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDefSetup
    ] = None
    """Setup parameters for Email integration"""


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments(
    BaseModel
):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup(
    BaseModel
):
    spider_api_key: str


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefArguments
    ] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDefSetup
    ] = None
    """Setup parameters for Spider integration"""


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments(
    BaseModel
):
    query: str

    load_max_docs: Optional[int] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDefArguments
    ] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments(
    BaseModel
):
    location: str


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup(
    BaseModel
):
    openweathermap_api_key: str


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef(
    BaseModel
):
    arguments: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefArguments
    ] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[
        MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDefSetup
    ] = None
    """Integration definition for Weather"""


MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration: TypeAlias = Union[
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationDummyIntegrationDef,
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationBraveIntegrationDef,
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationEmailIntegrationDef,
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationSpiderIntegrationDef,
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWikipediaIntegrationDef,
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegrationWeatherIntegrationDef,
    None,
]


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutput(BaseModel):
    name: str

    api_call: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputFunction] = None
    """Function definition"""

    integration: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputIntegration] = None
    """Brave integration definition"""

    system: Optional[MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutputSystem] = None
    """System definition"""


MainMainOutputMapPromptStepOutputToolsUnionMember1: TypeAlias = Union[
    MainMainOutputMapPromptStepOutputToolsUnionMember1ToolRef,
    MainMainOutputMapPromptStepOutputToolsUnionMember1CreateToolRequestOutput,
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


class ToolAPICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    timeout: Optional[int] = None


class ToolFunction(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class ToolIntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class ToolIntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class ToolIntegrationBraveIntegrationDefSetup(BaseModel):
    api_key: str


class ToolIntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[ToolIntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class ToolIntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class ToolIntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class ToolIntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[ToolIntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class ToolIntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    mode: Optional[Literal["scrape"]] = None

    params: Optional[object] = None


class ToolIntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class ToolIntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[str] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[ToolIntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class ToolIntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class ToolIntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class ToolIntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class ToolIntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class ToolIntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[ToolIntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[ToolIntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


ToolIntegration: TypeAlias = Union[
    ToolIntegrationDummyIntegrationDef,
    ToolIntegrationBraveIntegrationDef,
    ToolIntegrationEmailIntegrationDef,
    ToolIntegrationSpiderIntegrationDef,
    ToolIntegrationWikipediaIntegrationDef,
    ToolIntegrationWeatherIntegrationDef,
    None,
]


class ToolSystem(BaseModel):
    operation: Literal[
        "create",
        "update",
        "patch",
        "create_or_update",
        "embed",
        "change_status",
        "search",
        "chat",
        "history",
        "delete",
        "get",
        "list",
    ]

    resource: Literal["agent", "user", "task", "execution", "doc", "session", "job"]

    arguments: Optional[object] = None

    resource_id: Optional[str] = None

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]] = None


class Tool(BaseModel):
    name: str

    api_call: Optional[ToolAPICall] = None
    """API call definition"""

    description: Optional[str] = None

    function: Optional[ToolFunction] = None
    """Function definition"""

    inherited: Optional[bool] = None

    integration: Optional[ToolIntegration] = None
    """Brave integration definition"""

    system: Optional[ToolSystem] = None
    """System definition"""


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

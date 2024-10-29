# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .chat_settings_param import ChatSettingsParam

__all__ = [
    "TaskCreateParams",
    "Main",
    "MainEvaluateStep",
    "MainToolCallStep",
    "MainPromptStepInput",
    "MainPromptStepInputPromptUnionMember0",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainPromptStepInputToolChoice",
    "MainPromptStepInputToolChoiceNamedToolChoice",
    "MainPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainPromptStepInputToolsUnionMember1",
    "MainPromptStepInputToolsUnionMember1ToolRef",
    "MainPromptStepInputToolsUnionMember1ToolRefRef",
    "MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInput",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputFunction",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputSystem",
    "MainPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022",
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
    "MainIfElseWorkflowStepInput",
    "MainIfElseWorkflowStepInputThen",
    "MainIfElseWorkflowStepInputThenEvaluateStep",
    "MainIfElseWorkflowStepInputThenToolCallStep",
    "MainIfElseWorkflowStepInputThenPromptStepInput",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolChoice",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoice",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInput",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputFunction",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputSystem",
    "MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022",
    "MainIfElseWorkflowStepInputThenGetStep",
    "MainIfElseWorkflowStepInputThenSetStep",
    "MainIfElseWorkflowStepInputThenLogStep",
    "MainIfElseWorkflowStepInputThenYieldStep",
    "MainIfElseWorkflowStepInputThenReturnStep",
    "MainIfElseWorkflowStepInputThenSleepStep",
    "MainIfElseWorkflowStepInputThenSleepStepSleep",
    "MainIfElseWorkflowStepInputThenErrorWorkflowStep",
    "MainIfElseWorkflowStepInputThenWaitForInputStep",
    "MainIfElseWorkflowStepInputThenWaitForInputStepWaitForInput",
    "MainIfElseWorkflowStepInputElse",
    "MainIfElseWorkflowStepInputElseEvaluateStep",
    "MainIfElseWorkflowStepInputElseToolCallStep",
    "MainIfElseWorkflowStepInputElsePromptStepInput",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolChoice",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoice",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInput",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputAPICall",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputFunction",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegration",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputSystem",
    "MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022",
    "MainIfElseWorkflowStepInputElseGetStep",
    "MainIfElseWorkflowStepInputElseSetStep",
    "MainIfElseWorkflowStepInputElseLogStep",
    "MainIfElseWorkflowStepInputElseYieldStep",
    "MainIfElseWorkflowStepInputElseReturnStep",
    "MainIfElseWorkflowStepInputElseSleepStep",
    "MainIfElseWorkflowStepInputElseSleepStepSleep",
    "MainIfElseWorkflowStepInputElseErrorWorkflowStep",
    "MainIfElseWorkflowStepInputElseWaitForInputStep",
    "MainIfElseWorkflowStepInputElseWaitForInputStepWaitForInput",
    "MainSwitchStepInput",
    "MainSwitchStepInputSwitch",
    "MainSwitchStepInputSwitchThen",
    "MainSwitchStepInputSwitchThenEvaluateStep",
    "MainSwitchStepInputSwitchThenToolCallStep",
    "MainSwitchStepInputSwitchThenPromptStepInput",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainSwitchStepInputSwitchThenPromptStepInputToolChoice",
    "MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoice",
    "MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInput",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputFunction",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputSystem",
    "MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022",
    "MainSwitchStepInputSwitchThenGetStep",
    "MainSwitchStepInputSwitchThenSetStep",
    "MainSwitchStepInputSwitchThenLogStep",
    "MainSwitchStepInputSwitchThenYieldStep",
    "MainSwitchStepInputSwitchThenReturnStep",
    "MainSwitchStepInputSwitchThenSleepStep",
    "MainSwitchStepInputSwitchThenSleepStepSleep",
    "MainSwitchStepInputSwitchThenErrorWorkflowStep",
    "MainSwitchStepInputSwitchThenWaitForInputStep",
    "MainSwitchStepInputSwitchThenWaitForInputStepWaitForInput",
    "MainForeachStepInput",
    "MainForeachStepInputForeach",
    "MainForeachStepInputForeachDo",
    "MainForeachStepInputForeachDoWaitForInputStep",
    "MainForeachStepInputForeachDoWaitForInputStepWaitForInput",
    "MainForeachStepInputForeachDoEvaluateStep",
    "MainForeachStepInputForeachDoToolCallStep",
    "MainForeachStepInputForeachDoPromptStepInput",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainForeachStepInputForeachDoPromptStepInputToolChoice",
    "MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoice",
    "MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInput",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputFunction",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputSystem",
    "MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022",
    "MainForeachStepInputForeachDoGetStep",
    "MainForeachStepInputForeachDoSetStep",
    "MainForeachStepInputForeachDoLogStep",
    "MainForeachStepInputForeachDoYieldStep",
    "MainParallelStepInput",
    "MainParallelStepInputParallel",
    "MainParallelStepInputParallelEvaluateStep",
    "MainParallelStepInputParallelToolCallStep",
    "MainParallelStepInputParallelPromptStepInput",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainParallelStepInputParallelPromptStepInputToolChoice",
    "MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoice",
    "MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInput",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputFunction",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputSystem",
    "MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022",
    "MainParallelStepInputParallelGetStep",
    "MainParallelStepInputParallelSetStep",
    "MainParallelStepInputParallelLogStep",
    "MainParallelStepInputParallelYieldStep",
    "MainMainInput",
    "MainMainInputMap",
    "MainMainInputMapEvaluateStep",
    "MainMainInputMapToolCallStep",
    "MainMainInputMapPromptStepInput",
    "MainMainInputMapPromptStepInputPromptUnionMember0",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1Content",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel",
    "MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL",
    "MainMainInputMapPromptStepInputToolChoice",
    "MainMainInputMapPromptStepInputToolChoiceNamedToolChoice",
    "MainMainInputMapPromptStepInputToolChoiceNamedToolChoiceFunction",
    "MainMainInputMapPromptStepInputToolsUnionMember1",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRef",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRef",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByID",
    "MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByName",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInput",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputFunction",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputSystem",
    "MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022",
    "MainMainInputMapGetStep",
    "MainMainInputMapSetStep",
    "MainMainInputMapLogStep",
    "MainMainInputMapYieldStep",
    "Tool",
    "ToolAPICall",
    "ToolBash20241022",
    "ToolComputer20241022",
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
    "ToolTextEditor20241022",
]


class TaskCreateParams(TypedDict, total=False):
    main: Required[Iterable[Main]]

    name: Required[str]

    description: str

    inherit_tools: bool

    input_schema: Optional[object]

    metadata: Optional[object]

    tools: Iterable[Tool]


class MainEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(TypedDict, total=False):
    image_url: Required[MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL]
    """The image URL"""

    type: Literal["image_url"]


MainPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainPromptStepInputPromptUnionMember0(_MainPromptStepInputPromptUnionMember0ReservedKeywords, total=False):
    content: Required[Union[List[str], Iterable[MainPromptStepInputPromptUnionMember0ContentUnionMember1], str]]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainPromptStepInputToolChoiceNamedToolChoiceFunction]


MainPromptStepInputToolChoice: TypeAlias = Union[Literal["auto", "none"], MainPromptStepInputToolChoiceNamedToolChoice]


class MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022(TypedDict, total=False):
    name: str

    type: Literal["bash_20241022"]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022(TypedDict, total=False):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef(TypedDict, total=False):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup(
    TypedDict, total=False
):
    api_key: Required[str]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef(TypedDict, total=False):
    arguments: Optional[
        MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments
    ]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup]
    """Integration definition for Brave Search"""


_MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments(
    _MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords,
    total=False,
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup(
    TypedDict, total=False
):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef(TypedDict, total=False):
    arguments: Optional[
        MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments
    ]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup]
    """Setup parameters for Email integration"""


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments(
    TypedDict, total=False
):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup(
    TypedDict, total=False
):
    spider_api_key: Required[str]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef(TypedDict, total=False):
    arguments: Optional[
        MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments
    ]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup]
    """Setup parameters for Spider integration"""


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]

    load_max_docs: int


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments
    ]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments(
    TypedDict, total=False
):
    location: Required[str]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup(
    TypedDict, total=False
):
    openweathermap_api_key: Required[str]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments
    ]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup]
    """Integration definition for Weather"""


MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration: TypeAlias = Union[
    MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef,
    MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef,
    MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef,
    MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef,
    MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef,
    MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef,
]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputSystem(TypedDict, total=False):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022(TypedDict, total=False):
    name: str

    type: Literal["text_editor_20241022"]


class MainPromptStepInputToolsUnionMember1CreateToolRequestInput(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022]

    computer_20241022: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputFunction]
    """Function definition"""

    integration: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration]
    """Brave integration definition"""

    system: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputSystem]
    """System definition"""

    text_editor_20241022: Optional[MainPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022]


MainPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainPromptStepInputToolsUnionMember1ToolRef, MainPromptStepInputToolsUnionMember1CreateToolRequestInput
]


class MainPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainGetStep(TypedDict, total=False):
    get: Required[str]


class MainSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainLogStep(TypedDict, total=False):
    log: Required[str]


class MainYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainReturnStepReservedKeywords = TypedDict(
    "_MainReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainReturnStep(_MainReturnStepReservedKeywords, total=False):
    pass


class MainSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainSleepStep(TypedDict, total=False):
    sleep: Required[MainSleepStepSleep]


class MainErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainWaitForInputStepWaitForInput]


class MainIfElseWorkflowStepInputThenEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputThenToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1Content(
    TypedDict, total=False
):
    text: Required[str]

    type: Literal["text"]


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0(
    _MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str],
            Iterable[MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0ContentUnionMember1],
            str,
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoiceFunction]


MainIfElseWorkflowStepInputThenPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainIfElseWorkflowStepInputThenPromptStepInputToolChoiceNamedToolChoice
]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall(
    TypedDict, total=False
):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["bash_20241022"]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022(
    TypedDict, total=False
):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputFunction(
    TypedDict, total=False
):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup(
    TypedDict, total=False
):
    api_key: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments
    ]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup
    ]
    """Integration definition for Brave Search"""


_MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments(
    _MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords,
    total=False,
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup(
    TypedDict, total=False
):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments
    ]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup
    ]
    """Setup parameters for Email integration"""


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments(
    TypedDict, total=False
):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup(
    TypedDict, total=False
):
    spider_api_key: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments
    ]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup
    ]
    """Setup parameters for Spider integration"""


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]

    load_max_docs: int


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments
    ]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments(
    TypedDict, total=False
):
    location: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup(
    TypedDict, total=False
):
    openweathermap_api_key: Required[str]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments
    ]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup
    ]
    """Integration definition for Weather"""


MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef,
]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputSystem(
    TypedDict, total=False
):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["text_editor_20241022"]


class MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInput(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022
    ]

    computer_20241022: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022
    ]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputFunction]
    """Function definition"""

    integration: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration
    ]
    """Brave integration definition"""

    system: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputSystem]
    """System definition"""

    text_editor_20241022: Optional[
        MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022
    ]


MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1CreateToolRequestInput,
]


class MainIfElseWorkflowStepInputThenPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainIfElseWorkflowStepInputThenPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainIfElseWorkflowStepInputThenPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainIfElseWorkflowStepInputThenPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainIfElseWorkflowStepInputThenGetStep(TypedDict, total=False):
    get: Required[str]


class MainIfElseWorkflowStepInputThenSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputThenLogStep(TypedDict, total=False):
    log: Required[str]


class MainIfElseWorkflowStepInputThenYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainIfElseWorkflowStepInputThenReturnStepReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputThenReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainIfElseWorkflowStepInputThenReturnStep(
    _MainIfElseWorkflowStepInputThenReturnStepReservedKeywords, total=False
):
    pass


class MainIfElseWorkflowStepInputThenSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainIfElseWorkflowStepInputThenSleepStep(TypedDict, total=False):
    sleep: Required[MainIfElseWorkflowStepInputThenSleepStepSleep]


class MainIfElseWorkflowStepInputThenErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainIfElseWorkflowStepInputThenWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputThenWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainIfElseWorkflowStepInputThenWaitForInputStepWaitForInput]


MainIfElseWorkflowStepInputThen: TypeAlias = Union[
    MainIfElseWorkflowStepInputThenEvaluateStep,
    MainIfElseWorkflowStepInputThenToolCallStep,
    MainIfElseWorkflowStepInputThenPromptStepInput,
    MainIfElseWorkflowStepInputThenGetStep,
    MainIfElseWorkflowStepInputThenSetStep,
    MainIfElseWorkflowStepInputThenLogStep,
    MainIfElseWorkflowStepInputThenYieldStep,
    MainIfElseWorkflowStepInputThenReturnStep,
    MainIfElseWorkflowStepInputThenSleepStep,
    MainIfElseWorkflowStepInputThenErrorWorkflowStep,
    MainIfElseWorkflowStepInputThenWaitForInputStep,
]


class MainIfElseWorkflowStepInputElseEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputElseToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1Content(
    TypedDict, total=False
):
    text: Required[str]

    type: Literal["text"]


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0(
    _MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str],
            Iterable[MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0ContentUnionMember1],
            str,
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoiceFunction]


MainIfElseWorkflowStepInputElsePromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainIfElseWorkflowStepInputElsePromptStepInputToolChoiceNamedToolChoice
]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputAPICall(
    TypedDict, total=False
):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["bash_20241022"]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022(
    TypedDict, total=False
):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputFunction(
    TypedDict, total=False
):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup(
    TypedDict, total=False
):
    api_key: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments
    ]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup
    ]
    """Integration definition for Brave Search"""


_MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments(
    _MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords,
    total=False,
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup(
    TypedDict, total=False
):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments
    ]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup
    ]
    """Setup parameters for Email integration"""


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments(
    TypedDict, total=False
):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup(
    TypedDict, total=False
):
    spider_api_key: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments
    ]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup
    ]
    """Setup parameters for Spider integration"""


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]

    load_max_docs: int


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments
    ]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments(
    TypedDict, total=False
):
    location: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup(
    TypedDict, total=False
):
    openweathermap_api_key: Required[str]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments
    ]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup
    ]
    """Integration definition for Weather"""


MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegration: TypeAlias = Union[
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef,
]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputSystem(
    TypedDict, total=False
):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["text_editor_20241022"]


class MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInput(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022
    ]

    computer_20241022: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022
    ]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputFunction]
    """Function definition"""

    integration: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputIntegration
    ]
    """Brave integration definition"""

    system: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputSystem]
    """System definition"""

    text_editor_20241022: Optional[
        MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022
    ]


MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1ToolRef,
    MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1CreateToolRequestInput,
]


class MainIfElseWorkflowStepInputElsePromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainIfElseWorkflowStepInputElsePromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainIfElseWorkflowStepInputElsePromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainIfElseWorkflowStepInputElsePromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainIfElseWorkflowStepInputElseGetStep(TypedDict, total=False):
    get: Required[str]


class MainIfElseWorkflowStepInputElseSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputElseLogStep(TypedDict, total=False):
    log: Required[str]


class MainIfElseWorkflowStepInputElseYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainIfElseWorkflowStepInputElseReturnStepReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputElseReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainIfElseWorkflowStepInputElseReturnStep(
    _MainIfElseWorkflowStepInputElseReturnStepReservedKeywords, total=False
):
    pass


class MainIfElseWorkflowStepInputElseSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainIfElseWorkflowStepInputElseSleepStep(TypedDict, total=False):
    sleep: Required[MainIfElseWorkflowStepInputElseSleepStepSleep]


class MainIfElseWorkflowStepInputElseErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainIfElseWorkflowStepInputElseWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainIfElseWorkflowStepInputElseWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainIfElseWorkflowStepInputElseWaitForInputStepWaitForInput]


MainIfElseWorkflowStepInputElse: TypeAlias = Union[
    MainIfElseWorkflowStepInputElseEvaluateStep,
    MainIfElseWorkflowStepInputElseToolCallStep,
    MainIfElseWorkflowStepInputElsePromptStepInput,
    MainIfElseWorkflowStepInputElseGetStep,
    MainIfElseWorkflowStepInputElseSetStep,
    MainIfElseWorkflowStepInputElseLogStep,
    MainIfElseWorkflowStepInputElseYieldStep,
    MainIfElseWorkflowStepInputElseReturnStep,
    MainIfElseWorkflowStepInputElseSleepStep,
    MainIfElseWorkflowStepInputElseErrorWorkflowStep,
    MainIfElseWorkflowStepInputElseWaitForInputStep,
]

_MainIfElseWorkflowStepInputReservedKeywords = TypedDict(
    "_MainIfElseWorkflowStepInputReservedKeywords",
    {
        "if": str,
        "else": Optional[MainIfElseWorkflowStepInputElse],
    },
    total=False,
)


class MainIfElseWorkflowStepInput(_MainIfElseWorkflowStepInputReservedKeywords, total=False):
    then: Required[MainIfElseWorkflowStepInputThen]


class MainSwitchStepInputSwitchThenEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainSwitchStepInputSwitchThenToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0(
    _MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str], Iterable[MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0ContentUnionMember1], str
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoiceFunction]


MainSwitchStepInputSwitchThenPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainSwitchStepInputSwitchThenPromptStepInputToolChoiceNamedToolChoice
]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall(
    TypedDict, total=False
):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["bash_20241022"]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022(
    TypedDict, total=False
):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputFunction(
    TypedDict, total=False
):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup(
    TypedDict, total=False
):
    api_key: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments
    ]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup
    ]
    """Integration definition for Brave Search"""


_MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments(
    _MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords,
    total=False,
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup(
    TypedDict, total=False
):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments
    ]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup
    ]
    """Setup parameters for Email integration"""


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments(
    TypedDict, total=False
):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup(
    TypedDict, total=False
):
    spider_api_key: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments
    ]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup
    ]
    """Setup parameters for Spider integration"""


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]

    load_max_docs: int


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments
    ]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments(
    TypedDict, total=False
):
    location: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup(
    TypedDict, total=False
):
    openweathermap_api_key: Required[str]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments
    ]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup
    ]
    """Integration definition for Weather"""


MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration: TypeAlias = Union[
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef,
]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputSystem(TypedDict, total=False):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["text_editor_20241022"]


class MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInput(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022
    ]

    computer_20241022: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022
    ]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputFunction]
    """Function definition"""

    integration: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration
    ]
    """Brave integration definition"""

    system: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputSystem]
    """System definition"""

    text_editor_20241022: Optional[
        MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022
    ]


MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1ToolRef,
    MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1CreateToolRequestInput,
]


class MainSwitchStepInputSwitchThenPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainSwitchStepInputSwitchThenPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainSwitchStepInputSwitchThenPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainSwitchStepInputSwitchThenPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainSwitchStepInputSwitchThenGetStep(TypedDict, total=False):
    get: Required[str]


class MainSwitchStepInputSwitchThenSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainSwitchStepInputSwitchThenLogStep(TypedDict, total=False):
    log: Required[str]


class MainSwitchStepInputSwitchThenYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


_MainSwitchStepInputSwitchThenReturnStepReservedKeywords = TypedDict(
    "_MainSwitchStepInputSwitchThenReturnStepReservedKeywords",
    {
        "return": Dict[str, str],
    },
    total=False,
)


class MainSwitchStepInputSwitchThenReturnStep(_MainSwitchStepInputSwitchThenReturnStepReservedKeywords, total=False):
    pass


class MainSwitchStepInputSwitchThenSleepStepSleep(TypedDict, total=False):
    days: int

    hours: int

    minutes: int

    seconds: int


class MainSwitchStepInputSwitchThenSleepStep(TypedDict, total=False):
    sleep: Required[MainSwitchStepInputSwitchThenSleepStepSleep]


class MainSwitchStepInputSwitchThenErrorWorkflowStep(TypedDict, total=False):
    error: Required[str]


class MainSwitchStepInputSwitchThenWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainSwitchStepInputSwitchThenWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainSwitchStepInputSwitchThenWaitForInputStepWaitForInput]


MainSwitchStepInputSwitchThen: TypeAlias = Union[
    MainSwitchStepInputSwitchThenEvaluateStep,
    MainSwitchStepInputSwitchThenToolCallStep,
    MainSwitchStepInputSwitchThenPromptStepInput,
    MainSwitchStepInputSwitchThenGetStep,
    MainSwitchStepInputSwitchThenSetStep,
    MainSwitchStepInputSwitchThenLogStep,
    MainSwitchStepInputSwitchThenYieldStep,
    MainSwitchStepInputSwitchThenReturnStep,
    MainSwitchStepInputSwitchThenSleepStep,
    MainSwitchStepInputSwitchThenErrorWorkflowStep,
    MainSwitchStepInputSwitchThenWaitForInputStep,
]


class MainSwitchStepInputSwitch(TypedDict, total=False):
    case: Required[Union[Literal["_"], str]]

    then: Required[MainSwitchStepInputSwitchThen]


class MainSwitchStepInput(TypedDict, total=False):
    switch: Required[Iterable[MainSwitchStepInputSwitch]]


class MainForeachStepInputForeachDoWaitForInputStepWaitForInput(TypedDict, total=False):
    info: Required[Dict[str, str]]


class MainForeachStepInputForeachDoWaitForInputStep(TypedDict, total=False):
    wait_for_input: Required[MainForeachStepInputForeachDoWaitForInputStepWaitForInput]


class MainForeachStepInputForeachDoEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainForeachStepInputForeachDoToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0(
    _MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str], Iterable[MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0ContentUnionMember1], str
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoiceFunction]


MainForeachStepInputForeachDoPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainForeachStepInputForeachDoPromptStepInputToolChoiceNamedToolChoice
]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall(
    TypedDict, total=False
):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["bash_20241022"]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022(
    TypedDict, total=False
):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputFunction(
    TypedDict, total=False
):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup(
    TypedDict, total=False
):
    api_key: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments
    ]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup
    ]
    """Integration definition for Brave Search"""


_MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments(
    _MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords,
    total=False,
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup(
    TypedDict, total=False
):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments
    ]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup
    ]
    """Setup parameters for Email integration"""


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments(
    TypedDict, total=False
):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup(
    TypedDict, total=False
):
    spider_api_key: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments
    ]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup
    ]
    """Setup parameters for Spider integration"""


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]

    load_max_docs: int


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments
    ]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments(
    TypedDict, total=False
):
    location: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup(
    TypedDict, total=False
):
    openweathermap_api_key: Required[str]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments
    ]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup
    ]
    """Integration definition for Weather"""


MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration: TypeAlias = Union[
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef,
]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputSystem(TypedDict, total=False):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["text_editor_20241022"]


class MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInput(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022
    ]

    computer_20241022: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022
    ]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputFunction]
    """Function definition"""

    integration: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration
    ]
    """Brave integration definition"""

    system: Optional[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputSystem]
    """System definition"""

    text_editor_20241022: Optional[
        MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022
    ]


MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1ToolRef,
    MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1CreateToolRequestInput,
]


class MainForeachStepInputForeachDoPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainForeachStepInputForeachDoPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainForeachStepInputForeachDoPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainForeachStepInputForeachDoPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainForeachStepInputForeachDoGetStep(TypedDict, total=False):
    get: Required[str]


class MainForeachStepInputForeachDoSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainForeachStepInputForeachDoLogStep(TypedDict, total=False):
    log: Required[str]


class MainForeachStepInputForeachDoYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


MainForeachStepInputForeachDo: TypeAlias = Union[
    MainForeachStepInputForeachDoWaitForInputStep,
    MainForeachStepInputForeachDoEvaluateStep,
    MainForeachStepInputForeachDoToolCallStep,
    MainForeachStepInputForeachDoPromptStepInput,
    MainForeachStepInputForeachDoGetStep,
    MainForeachStepInputForeachDoSetStep,
    MainForeachStepInputForeachDoLogStep,
    MainForeachStepInputForeachDoYieldStep,
]

_MainForeachStepInputForeachReservedKeywords = TypedDict(
    "_MainForeachStepInputForeachReservedKeywords",
    {
        "in": str,
    },
    total=False,
)


class MainForeachStepInputForeach(_MainForeachStepInputForeachReservedKeywords, total=False):
    do: Required[MainForeachStepInputForeachDo]


class MainForeachStepInput(TypedDict, total=False):
    foreach: Required[MainForeachStepInputForeach]


class MainParallelStepInputParallelEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainParallelStepInputParallelToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(
    TypedDict, total=False
):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(
    TypedDict, total=False
):
    image_url: Required[
        MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL
    ]
    """The image URL"""

    type: Literal["image_url"]


MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainParallelStepInputParallelPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainParallelStepInputParallelPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainParallelStepInputParallelPromptStepInputPromptUnionMember0(
    _MainParallelStepInputParallelPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[
            List[str], Iterable[MainParallelStepInputParallelPromptStepInputPromptUnionMember0ContentUnionMember1], str
        ]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoiceFunction]


MainParallelStepInputParallelPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainParallelStepInputParallelPromptStepInputToolChoiceNamedToolChoice
]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall(
    TypedDict, total=False
):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["bash_20241022"]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022(
    TypedDict, total=False
):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputFunction(
    TypedDict, total=False
):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup(
    TypedDict, total=False
):
    api_key: Required[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments
    ]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup
    ]
    """Integration definition for Brave Search"""


_MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments(
    _MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords,
    total=False,
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup(
    TypedDict, total=False
):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments
    ]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup
    ]
    """Setup parameters for Email integration"""


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments(
    TypedDict, total=False
):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup(
    TypedDict, total=False
):
    spider_api_key: Required[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments
    ]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup
    ]
    """Setup parameters for Spider integration"""


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]

    load_max_docs: int


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments
    ]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments(
    TypedDict, total=False
):
    location: Required[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup(
    TypedDict, total=False
):
    openweathermap_api_key: Required[str]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments
    ]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup
    ]
    """Integration definition for Weather"""


MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration: TypeAlias = Union[
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef,
]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputSystem(TypedDict, total=False):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022(
    TypedDict, total=False
):
    name: str

    type: Literal["text_editor_20241022"]


class MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInput(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022
    ]

    computer_20241022: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022
    ]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputFunction]
    """Function definition"""

    integration: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration
    ]
    """Brave integration definition"""

    system: Optional[MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputSystem]
    """System definition"""

    text_editor_20241022: Optional[
        MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022
    ]


MainParallelStepInputParallelPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1ToolRef,
    MainParallelStepInputParallelPromptStepInputToolsUnionMember1CreateToolRequestInput,
]


class MainParallelStepInputParallelPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainParallelStepInputParallelPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainParallelStepInputParallelPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainParallelStepInputParallelPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainParallelStepInputParallelGetStep(TypedDict, total=False):
    get: Required[str]


class MainParallelStepInputParallelSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainParallelStepInputParallelLogStep(TypedDict, total=False):
    log: Required[str]


class MainParallelStepInputParallelYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


MainParallelStepInputParallel: TypeAlias = Union[
    MainParallelStepInputParallelEvaluateStep,
    MainParallelStepInputParallelToolCallStep,
    MainParallelStepInputParallelPromptStepInput,
    MainParallelStepInputParallelGetStep,
    MainParallelStepInputParallelSetStep,
    MainParallelStepInputParallelLogStep,
    MainParallelStepInputParallelYieldStep,
]


class MainParallelStepInput(TypedDict, total=False):
    parallel: Required[Iterable[MainParallelStepInputParallel]]


class MainMainInputMapEvaluateStep(TypedDict, total=False):
    evaluate: Required[Dict[str, str]]


class MainMainInputMapToolCallStep(TypedDict, total=False):
    tool: Required[str]

    arguments: Union[Dict[str, Union[Dict[str, str], str]], Literal["_"]]


class MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel(TypedDict, total=False):
    image_url: Required[MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModelImageURL]
    """The image URL"""

    type: Literal["image_url"]


MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1: TypeAlias = Union[
    MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1Content,
    MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1ContentModel,
]

_MainMainInputMapPromptStepInputPromptUnionMember0ReservedKeywords = TypedDict(
    "_MainMainInputMapPromptStepInputPromptUnionMember0ReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class MainMainInputMapPromptStepInputPromptUnionMember0(
    _MainMainInputMapPromptStepInputPromptUnionMember0ReservedKeywords, total=False
):
    content: Required[
        Union[List[str], Iterable[MainMainInputMapPromptStepInputPromptUnionMember0ContentUnionMember1], str]
    ]

    role: Required[Literal["user", "assistant", "system", "function", "function_response", "function_call", "auto"]]

    name: Optional[str]


class MainMainInputMapPromptStepInputToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]


class MainMainInputMapPromptStepInputToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[MainMainInputMapPromptStepInputToolChoiceNamedToolChoiceFunction]


MainMainInputMapPromptStepInputToolChoice: TypeAlias = Union[
    Literal["auto", "none"], MainMainInputMapPromptStepInputToolChoiceNamedToolChoice
]


class MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByID(TypedDict, total=False):
    id: Optional[str]


class MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByName(TypedDict, total=False):
    name: Optional[str]


MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRef: TypeAlias = Union[
    MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByID,
    MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRefToolRefByName,
]


class MainMainInputMapPromptStepInputToolsUnionMember1ToolRef(TypedDict, total=False):
    ref: Required[MainMainInputMapPromptStepInputToolsUnionMember1ToolRefRef]
    """Reference to a tool by id"""


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022(TypedDict, total=False):
    name: str

    type: Literal["bash_20241022"]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022(TypedDict, total=False):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup(
    TypedDict, total=False
):
    api_key: Required[str]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefArguments
    ]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDefSetup
    ]
    """Integration definition for Brave Search"""


_MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments(
    _MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArgumentsReservedKeywords,
    total=False,
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup(
    TypedDict, total=False
):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefArguments
    ]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDefSetup
    ]
    """Setup parameters for Email integration"""


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments(
    TypedDict, total=False
):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup(
    TypedDict, total=False
):
    spider_api_key: Required[str]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefArguments
    ]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDefSetup
    ]
    """Setup parameters for Spider integration"""


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments(
    TypedDict, total=False
):
    query: Required[str]

    load_max_docs: int


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDefArguments
    ]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments(
    TypedDict, total=False
):
    location: Required[str]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup(
    TypedDict, total=False
):
    openweathermap_api_key: Required[str]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef(
    TypedDict, total=False
):
    arguments: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefArguments
    ]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDefSetup
    ]
    """Integration definition for Weather"""


MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration: TypeAlias = Union[
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationDummyIntegrationDef,
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationBraveIntegrationDef,
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationEmailIntegrationDef,
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationSpiderIntegrationDef,
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWikipediaIntegrationDef,
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegrationWeatherIntegrationDef,
]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputSystem(TypedDict, total=False):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022(TypedDict, total=False):
    name: str

    type: Literal["text_editor_20241022"]


class MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInput(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputAPICall]
    """API call definition"""

    bash_20241022: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputBash20241022]

    computer_20241022: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputComputer20241022]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputFunction]
    """Function definition"""

    integration: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputIntegration]
    """Brave integration definition"""

    system: Optional[MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputSystem]
    """System definition"""

    text_editor_20241022: Optional[
        MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInputTextEditor20241022
    ]


MainMainInputMapPromptStepInputToolsUnionMember1: TypeAlias = Union[
    MainMainInputMapPromptStepInputToolsUnionMember1ToolRef,
    MainMainInputMapPromptStepInputToolsUnionMember1CreateToolRequestInput,
]


class MainMainInputMapPromptStepInput(TypedDict, total=False):
    prompt: Required[Union[Iterable[MainMainInputMapPromptStepInputPromptUnionMember0], str]]

    forward_tool_results: Optional[bool]

    settings: Optional[ChatSettingsParam]

    tool_choice: Optional[MainMainInputMapPromptStepInputToolChoice]

    tools: Union[Literal["all"], Iterable[MainMainInputMapPromptStepInputToolsUnionMember1]]

    unwrap: bool


class MainMainInputMapGetStep(TypedDict, total=False):
    get: Required[str]


class MainMainInputMapSetStep(TypedDict, total=False):
    set: Required[Dict[str, str]]


class MainMainInputMapLogStep(TypedDict, total=False):
    log: Required[str]


class MainMainInputMapYieldStep(TypedDict, total=False):
    workflow: Required[str]

    arguments: Union[Dict[str, str], Literal["_"]]


MainMainInputMap: TypeAlias = Union[
    MainMainInputMapEvaluateStep,
    MainMainInputMapToolCallStep,
    MainMainInputMapPromptStepInput,
    MainMainInputMapGetStep,
    MainMainInputMapSetStep,
    MainMainInputMapLogStep,
    MainMainInputMapYieldStep,
]


class MainMainInput(TypedDict, total=False):
    map: Required[MainMainInputMap]

    over: Required[str]

    initial: object

    parallelism: Optional[int]

    reduce: Optional[str]


Main: TypeAlias = Union[
    MainEvaluateStep,
    MainToolCallStep,
    MainPromptStepInput,
    MainGetStep,
    MainSetStep,
    MainLogStep,
    MainYieldStep,
    MainReturnStep,
    MainSleepStep,
    MainErrorWorkflowStep,
    MainWaitForInputStep,
    MainIfElseWorkflowStepInput,
    MainSwitchStepInput,
    MainForeachStepInput,
    MainParallelStepInput,
    MainMainInput,
]


class ToolAPICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    timeout: Optional[int]


class ToolBash20241022(TypedDict, total=False):
    name: str

    type: Literal["bash_20241022"]


class ToolComputer20241022(TypedDict, total=False):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class ToolFunction(TypedDict, total=False):
    description: Optional[object]

    name: Optional[object]

    parameters: Optional[object]


class ToolIntegrationDummyIntegrationDef(TypedDict, total=False):
    arguments: Optional[object]

    method: Optional[str]

    provider: Literal["dummy"]

    setup: Optional[object]


class ToolIntegrationBraveIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]


class ToolIntegrationBraveIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]


class ToolIntegrationBraveIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBraveIntegrationDefArguments]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[ToolIntegrationBraveIntegrationDefSetup]
    """Integration definition for Brave Search"""


_ToolIntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_ToolIntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class ToolIntegrationEmailIntegrationDefArguments(
    _ToolIntegrationEmailIntegrationDefArgumentsReservedKeywords, total=False
):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class ToolIntegrationEmailIntegrationDefSetup(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class ToolIntegrationEmailIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationEmailIntegrationDefArguments]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[ToolIntegrationEmailIntegrationDefSetup]
    """Setup parameters for Email integration"""


class ToolIntegrationSpiderIntegrationDefArguments(TypedDict, total=False):
    url: Required[str]

    mode: Literal["scrape"]

    params: Optional[object]


class ToolIntegrationSpiderIntegrationDefSetup(TypedDict, total=False):
    spider_api_key: Required[str]


class ToolIntegrationSpiderIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationSpiderIntegrationDefArguments]
    """Arguments for Spider integration"""

    method: Optional[str]

    provider: Literal["spider"]

    setup: Optional[ToolIntegrationSpiderIntegrationDefSetup]
    """Setup parameters for Spider integration"""


class ToolIntegrationWikipediaIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]

    load_max_docs: int


class ToolIntegrationWikipediaIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationWikipediaIntegrationDefArguments]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: Optional[object]


class ToolIntegrationWeatherIntegrationDefArguments(TypedDict, total=False):
    location: Required[str]


class ToolIntegrationWeatherIntegrationDefSetup(TypedDict, total=False):
    openweathermap_api_key: Required[str]


class ToolIntegrationWeatherIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationWeatherIntegrationDefArguments]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[ToolIntegrationWeatherIntegrationDefSetup]
    """Integration definition for Weather"""


ToolIntegration: TypeAlias = Union[
    ToolIntegrationDummyIntegrationDef,
    ToolIntegrationBraveIntegrationDef,
    ToolIntegrationEmailIntegrationDef,
    ToolIntegrationSpiderIntegrationDef,
    ToolIntegrationWikipediaIntegrationDef,
    ToolIntegrationWeatherIntegrationDef,
]


class ToolSystem(TypedDict, total=False):
    operation: Required[
        Literal[
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
    ]

    resource: Required[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    arguments: Optional[object]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class ToolTextEditor20241022(TypedDict, total=False):
    name: str

    type: Literal["text_editor_20241022"]


class Tool(TypedDict, total=False):
    name: Required[str]

    api_call: Optional[ToolAPICall]
    """API call definition"""

    bash_20241022: Optional[ToolBash20241022]

    computer_20241022: Optional[ToolComputer20241022]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[ToolFunction]
    """Function definition"""

    integration: Optional[ToolIntegration]
    """Brave integration definition"""

    system: Optional[ToolSystem]
    """System definition"""

    text_editor_20241022: Optional[ToolTextEditor20241022]

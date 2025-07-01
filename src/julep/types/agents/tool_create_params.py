# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.secret_ref import SecretRef
from ..shared_params.system_def import SystemDef
from ..shared_params.function_def import FunctionDef
from ..shared_params.bash20241022_def import Bash20241022Def
from ..shared_params.computer20241022_def import Computer20241022Def
from ..shared_params.arxiv_integration_def import ArxivIntegrationDef
from ..shared_params.brave_integration_def import BraveIntegrationDef
from ..shared_params.dummy_integration_def import DummyIntegrationDef
from ..shared_params.email_integration_def import EmailIntegrationDef
from ..shared_params.ffmpeg_integration_def import FfmpegIntegrationDef
from ..shared_params.spider_integration_def import SpiderIntegrationDef
from ..shared_params.algolia_integration_def import AlgoliaIntegrationDef
from ..shared_params.mailgun_integration_def import MailgunIntegrationDef
from ..shared_params.text_editor20241022_def import TextEditor20241022Def
from ..shared_params.weather_integration_def import WeatherIntegrationDef
from ..shared_params.wikipedia_integration_def import WikipediaIntegrationDef
from ..shared_params.llama_parse_integration_def import LlamaParseIntegrationDef
from ..shared_params.unstructured_integration_def import UnstructuredIntegrationDef
from ..shared_params.remote_browser_integration_def import RemoteBrowserIntegrationDef
from ..shared_params.cloudinary_edit_integration_def import CloudinaryEditIntegrationDef
from ..shared_params.cloudinary_upload_integration_def import CloudinaryUploadIntegrationDef
from ..shared_params.browserbase_context_integration_def import BrowserbaseContextIntegrationDef
from ..shared_params.browserbase_extension_integration_def import BrowserbaseExtensionIntegrationDef
from ..shared_params.browserbase_get_session_integration_def import BrowserbaseGetSessionIntegrationDef
from ..shared_params.browserbase_list_sessions_integration_def import BrowserbaseListSessionsIntegrationDef
from ..shared_params.browserbase_create_session_integration_def import BrowserbaseCreateSessionIntegrationDef
from ..shared_params.browserbase_complete_session_integration_def import BrowserbaseCompleteSessionIntegrationDef
from ..shared_params.browserbase_get_session_live_urls_integration_def import (
    BrowserbaseGetSessionLiveURLsIntegrationDef,
)

__all__ = ["ToolCreateParams", "APICall", "APICallParamsSchema", "APICallParamsSchemaProperties", "Integration"]


class ToolCreateParams(TypedDict, total=False):
    name: Required[str]

    type: Required[
        Literal[
            "function",
            "integration",
            "system",
            "api_call",
            "computer_20241022",
            "text_editor_20241022",
            "bash_20241022",
        ]
    ]

    api_call: Optional[APICall]
    """API call definition"""

    bash_20241022: Optional[Bash20241022Def]

    computer_20241022: Optional[Computer20241022Def]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[FunctionDef]
    """Function definition"""

    integration: Optional[Integration]
    """Brave integration definition"""

    system: Optional[SystemDef]
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022Def]


class APICallParamsSchemaProperties(TypedDict, total=False):
    type: Required[str]

    description: Optional[str]

    enum: Optional[List[str]]

    items: object


class APICallParamsSchema(TypedDict, total=False):
    properties: Required[Dict[str, APICallParamsSchemaProperties]]

    additional_properties: Annotated[Optional[bool], PropertyInfo(alias="additionalProperties")]

    required: List[str]

    type: str


class APICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    files: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    include_response_content: bool

    json: Optional[object]

    params: Union[str, object, None]

    params_schema: Optional[APICallParamsSchema]
    """JSON Schema for API call parameters"""

    schema: Optional[object]

    secrets: Optional[Dict[str, SecretRef]]

    timeout: Optional[int]


Integration: TypeAlias = Union[
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
]

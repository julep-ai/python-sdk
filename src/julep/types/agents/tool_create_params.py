# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.system_def import SystemDef
from ..shared_params.api_call_def import APICallDef
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

__all__ = ["ToolCreateParams", "Integration"]


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

    api_call: Optional[APICallDef]
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

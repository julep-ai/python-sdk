# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ToolUpdateParams",
    "APICall",
    "Bash20241022",
    "Computer20241022",
    "Function",
    "Integration",
    "IntegrationDummyIntegrationDefUpdate",
    "IntegrationBraveIntegrationDefUpdate",
    "IntegrationBraveIntegrationDefUpdateArguments",
    "IntegrationBraveIntegrationDefUpdateSetup",
    "IntegrationEmailIntegrationDefUpdate",
    "IntegrationEmailIntegrationDefUpdateArguments",
    "IntegrationEmailIntegrationDefUpdateSetup",
    "IntegrationSpiderIntegrationDefUpdate",
    "IntegrationSpiderIntegrationDefUpdateArguments",
    "IntegrationSpiderIntegrationDefUpdateSetup",
    "IntegrationWikipediaIntegrationDefUpdate",
    "IntegrationWikipediaIntegrationDefUpdateArguments",
    "IntegrationWeatherIntegrationDefUpdate",
    "IntegrationWeatherIntegrationDefUpdateArguments",
    "IntegrationWeatherIntegrationDefUpdateSetup",
    "IntegrationBrowserbaseContextIntegrationDefUpdate",
    "IntegrationBrowserbaseContextIntegrationDefUpdateArguments",
    "IntegrationBrowserbaseContextIntegrationDefUpdateSetup",
    "IntegrationBrowserbaseExtensionIntegrationDefUpdate",
    "IntegrationBrowserbaseExtensionIntegrationDefUpdateArguments",
    "IntegrationBrowserbaseExtensionIntegrationDefUpdateSetup",
    "IntegrationBrowserbaseListSessionsIntegrationDefUpdate",
    "IntegrationBrowserbaseListSessionsIntegrationDefUpdateArguments",
    "IntegrationBrowserbaseListSessionsIntegrationDefUpdateSetup",
    "IntegrationBrowserbaseCreateSessionIntegrationDefUpdate",
    "IntegrationBrowserbaseCreateSessionIntegrationDefUpdateArguments",
    "IntegrationBrowserbaseCreateSessionIntegrationDefUpdateSetup",
    "IntegrationBrowserbaseGetSessionIntegrationDefUpdate",
    "IntegrationBrowserbaseGetSessionIntegrationDefUpdateArguments",
    "IntegrationBrowserbaseGetSessionIntegrationDefUpdateSetup",
    "IntegrationBrowserbaseCompleteSessionIntegrationDefUpdate",
    "IntegrationBrowserbaseCompleteSessionIntegrationDefUpdateArguments",
    "IntegrationBrowserbaseCompleteSessionIntegrationDefUpdateSetup",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdate",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdateArguments",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdateSetup",
    "IntegrationRemoteBrowserIntegrationDefUpdate",
    "IntegrationRemoteBrowserIntegrationDefUpdateArguments",
    "IntegrationRemoteBrowserIntegrationDefUpdateSetup",
    "IntegrationLlamaParseIntegrationDefUpdate",
    "IntegrationLlamaParseIntegrationDefUpdateArguments",
    "IntegrationLlamaParseIntegrationDefUpdateSetup",
    "IntegrationFfmpegIntegrationDefUpdate",
    "IntegrationFfmpegIntegrationDefUpdateArguments",
    "IntegrationCloudinaryUploadIntegrationDefUpdate",
    "IntegrationCloudinaryUploadIntegrationDefUpdateArguments",
    "IntegrationCloudinaryUploadIntegrationDefUpdateSetup",
    "IntegrationCloudinaryEditIntegrationDefUpdate",
    "IntegrationCloudinaryEditIntegrationDefUpdateArguments",
    "IntegrationCloudinaryEditIntegrationDefUpdateSetup",
    "IntegrationArxivIntegrationDefUpdate",
    "IntegrationArxivIntegrationDefUpdateArguments",
    "IntegrationUnstructuredIntegrationDefUpdate",
    "IntegrationUnstructuredIntegrationDefUpdateArguments",
    "IntegrationUnstructuredIntegrationDefUpdateSetup",
    "IntegrationAlgoliaIntegrationDefUpdate",
    "IntegrationAlgoliaIntegrationDefUpdateArguments",
    "IntegrationAlgoliaIntegrationDefUpdateSetup",
    "System",
    "TextEditor20241022",
]


class ToolUpdateParams(TypedDict, total=False):
    agent_id: Required[str]

    api_call: Optional[APICall]
    """API call definition"""

    bash_20241022: Optional[Bash20241022]

    computer_20241022: Optional[Computer20241022]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[Function]
    """Function definition"""

    integration: Optional[Integration]
    """Brave integration definition"""

    name: Optional[str]

    system: Optional[System]
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022]

    type: Optional[
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


class APICall(TypedDict, total=False):
    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    files: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    params: Union[str, object, None]

    schema: Optional[object]

    timeout: Optional[int]

    url: Optional[str]


class Bash20241022(TypedDict, total=False):
    name: str

    type: Literal["bash_20241022"]


class Computer20241022(TypedDict, total=False):
    display_height_px: int

    display_number: int

    display_width_px: int

    name: str

    type: Literal["computer_20241022"]


class Function(TypedDict, total=False):
    description: object

    name: object

    parameters: Optional[object]


class IntegrationDummyIntegrationDefUpdate(TypedDict, total=False):
    arguments: object

    method: Optional[str]

    provider: Literal["dummy"]

    setup: object


class IntegrationBraveIntegrationDefUpdateArguments(TypedDict, total=False):
    query: Optional[str]


class IntegrationBraveIntegrationDefUpdateSetup(TypedDict, total=False):
    brave_api_key: Optional[str]


class IntegrationBraveIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBraveIntegrationDefUpdateArguments]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[IntegrationBraveIntegrationDefUpdateSetup]
    """Integration definition for Brave Search"""


_IntegrationEmailIntegrationDefUpdateArgumentsReservedKeywords = TypedDict(
    "_IntegrationEmailIntegrationDefUpdateArgumentsReservedKeywords",
    {
        "from": Optional[str],
    },
    total=False,
)


class IntegrationEmailIntegrationDefUpdateArguments(
    _IntegrationEmailIntegrationDefUpdateArgumentsReservedKeywords, total=False
):
    body: Optional[str]

    subject: Optional[str]

    to: Optional[str]


class IntegrationEmailIntegrationDefUpdateSetup(TypedDict, total=False):
    host: Optional[str]

    password: Optional[str]

    port: Optional[int]

    user: Optional[str]


class IntegrationEmailIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationEmailIntegrationDefUpdateArguments]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[IntegrationEmailIntegrationDefUpdateSetup]
    """Setup parameters for Email integration"""


class IntegrationSpiderIntegrationDefUpdateArguments(TypedDict, total=False):
    content_type: Literal["application/json", "text/csv", "application/xml", "application/jsonl"]

    params: Optional[object]

    url: Optional[str]


class IntegrationSpiderIntegrationDefUpdateSetup(TypedDict, total=False):
    spider_api_key: Optional[str]


class IntegrationSpiderIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationSpiderIntegrationDefUpdateArguments]
    """Arguments for Spider integration"""

    method: Optional[Literal["crawl", "links", "screenshot", "search"]]

    provider: Literal["spider"]

    setup: Optional[IntegrationSpiderIntegrationDefUpdateSetup]
    """Setup parameters for Spider integration"""


class IntegrationWikipediaIntegrationDefUpdateArguments(TypedDict, total=False):
    load_max_docs: int

    query: Optional[str]


class IntegrationWikipediaIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationWikipediaIntegrationDefUpdateArguments]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: object


class IntegrationWeatherIntegrationDefUpdateArguments(TypedDict, total=False):
    location: Optional[str]


class IntegrationWeatherIntegrationDefUpdateSetup(TypedDict, total=False):
    openweathermap_api_key: Optional[str]


class IntegrationWeatherIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationWeatherIntegrationDefUpdateArguments]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[IntegrationWeatherIntegrationDefUpdateSetup]
    """Integration definition for Weather"""


class IntegrationBrowserbaseContextIntegrationDefUpdateArguments(TypedDict, total=False):
    project_id: Annotated[Optional[str], PropertyInfo(alias="projectId")]


class IntegrationBrowserbaseContextIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]


class IntegrationBrowserbaseContextIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseContextIntegrationDefUpdateArguments]

    method: Literal["create_context"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseContextIntegrationDefUpdateSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseExtensionIntegrationDefUpdateArguments(TypedDict, total=False):
    ref: Optional[str]

    repository_name: Annotated[Optional[str], PropertyInfo(alias="repositoryName")]


class IntegrationBrowserbaseExtensionIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]


class IntegrationBrowserbaseExtensionIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseExtensionIntegrationDefUpdateArguments]

    method: Optional[Literal["install_extension_from_github"]]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseExtensionIntegrationDefUpdateSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseListSessionsIntegrationDefUpdateArguments(TypedDict, total=False):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]]


class IntegrationBrowserbaseListSessionsIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]


class IntegrationBrowserbaseListSessionsIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseListSessionsIntegrationDefUpdateArguments]

    method: Literal["list_sessions"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseListSessionsIntegrationDefUpdateSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCreateSessionIntegrationDefUpdateArguments(TypedDict, total=False):
    browser_settings: Annotated[object, PropertyInfo(alias="browserSettings")]

    extension_id: Annotated[Optional[str], PropertyInfo(alias="extensionId")]

    keep_alive: Annotated[bool, PropertyInfo(alias="keepAlive")]

    project_id: Annotated[Optional[str], PropertyInfo(alias="projectId")]

    proxies: Union[bool, Iterable[object]]

    timeout: int


class IntegrationBrowserbaseCreateSessionIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]


class IntegrationBrowserbaseCreateSessionIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefUpdateArguments]

    method: Literal["create_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefUpdateSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionIntegrationDefUpdateArguments(TypedDict, total=False):
    id: Optional[str]


class IntegrationBrowserbaseGetSessionIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]


class IntegrationBrowserbaseGetSessionIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseGetSessionIntegrationDefUpdateArguments]

    method: Literal["get_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseGetSessionIntegrationDefUpdateSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCompleteSessionIntegrationDefUpdateArguments(TypedDict, total=False):
    id: Optional[str]

    status: Literal["REQUEST_RELEASE"]


class IntegrationBrowserbaseCompleteSessionIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]


class IntegrationBrowserbaseCompleteSessionIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseCompleteSessionIntegrationDefUpdateArguments]

    method: Literal["complete_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseCompleteSessionIntegrationDefUpdateSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdateArguments(TypedDict, total=False):
    id: Optional[str]


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdateSetup(TypedDict, total=False):
    api_key: Optional[str]

    api_url: Optional[str]

    connect_url: Optional[str]

    project_id: Optional[str]


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdateArguments]

    method: Literal["get_live_urls"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdateSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationRemoteBrowserIntegrationDefUpdateArguments(TypedDict, total=False):
    action: Optional[
        Literal[
            "key",
            "type",
            "mouse_move",
            "left_click",
            "left_click_drag",
            "right_click",
            "middle_click",
            "double_click",
            "screenshot",
            "cursor_position",
            "navigate",
            "refresh",
        ]
    ]

    connect_url: Optional[str]

    coordinate: Optional[Iterable[object]]

    text: Optional[str]


class IntegrationRemoteBrowserIntegrationDefUpdateSetup(TypedDict, total=False):
    connect_url: Optional[str]

    height: Optional[int]

    width: Optional[int]


class IntegrationRemoteBrowserIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationRemoteBrowserIntegrationDefUpdateArguments]
    """The arguments for the remote browser"""

    method: Literal["perform_action"]

    provider: Literal["remote_browser"]

    setup: Optional[IntegrationRemoteBrowserIntegrationDefUpdateSetup]
    """The setup parameters for the remote browser"""


class IntegrationLlamaParseIntegrationDefUpdateArguments(TypedDict, total=False):
    base64: bool

    file: Union[str, List[str], None]

    filename: Optional[str]

    params: Optional[object]


class IntegrationLlamaParseIntegrationDefUpdateSetup(TypedDict, total=False):
    llamaparse_api_key: Optional[str]

    params: Optional[object]


class IntegrationLlamaParseIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationLlamaParseIntegrationDefUpdateArguments]
    """Arguments for LlamaParse integration"""

    method: Optional[str]

    provider: Literal["llama_parse"]

    setup: Optional[IntegrationLlamaParseIntegrationDefUpdateSetup]
    """Setup parameters for LlamaParse integration"""


class IntegrationFfmpegIntegrationDefUpdateArguments(TypedDict, total=False):
    cmd: Optional[str]

    file: Union[str, List[str], None]


class IntegrationFfmpegIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationFfmpegIntegrationDefUpdateArguments]
    """Arguments for Ffmpeg CMD"""

    method: Optional[str]

    provider: Literal["ffmpeg"]

    setup: object


class IntegrationCloudinaryUploadIntegrationDefUpdateArguments(TypedDict, total=False):
    file: Optional[str]

    public_id: Optional[str]

    return_base64: bool

    upload_params: Optional[object]


class IntegrationCloudinaryUploadIntegrationDefUpdateSetup(TypedDict, total=False):
    cloudinary_api_key: Optional[str]

    cloudinary_api_secret: Optional[str]

    cloudinary_cloud_name: Optional[str]

    params: Optional[object]


class IntegrationCloudinaryUploadIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationCloudinaryUploadIntegrationDefUpdateArguments]
    """Arguments for Cloudinary media upload"""

    method: Literal["media_upload"]

    provider: Literal["cloudinary"]

    setup: Optional[IntegrationCloudinaryUploadIntegrationDefUpdateSetup]
    """Setup parameters for Cloudinary integration"""


class IntegrationCloudinaryEditIntegrationDefUpdateArguments(TypedDict, total=False):
    public_id: Optional[str]

    return_base64: bool

    transformation: Optional[Iterable[object]]


class IntegrationCloudinaryEditIntegrationDefUpdateSetup(TypedDict, total=False):
    cloudinary_api_key: Optional[str]

    cloudinary_api_secret: Optional[str]

    cloudinary_cloud_name: Optional[str]

    params: Optional[object]


class IntegrationCloudinaryEditIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationCloudinaryEditIntegrationDefUpdateArguments]
    """Arguments for Cloudinary media edit"""

    method: Literal["media_edit"]

    provider: Literal["cloudinary"]

    setup: Optional[IntegrationCloudinaryEditIntegrationDefUpdateSetup]
    """Setup parameters for Cloudinary integration"""


class IntegrationArxivIntegrationDefUpdateArguments(TypedDict, total=False):
    download_pdf: bool

    id_list: Optional[List[str]]

    max_results: int

    query: Optional[str]

    sort_by: Literal["relevance", "lastUpdatedDate", "submittedDate"]

    sort_order: Literal["ascending", "descending"]


class IntegrationArxivIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationArxivIntegrationDefUpdateArguments]
    """Arguments for Arxiv Search"""

    method: Optional[str]

    provider: Literal["arxiv"]

    setup: object


class IntegrationUnstructuredIntegrationDefUpdateArguments(TypedDict, total=False):
    file: Optional[str]

    filename: Optional[str]

    partition_params: Optional[object]


class IntegrationUnstructuredIntegrationDefUpdateSetup(TypedDict, total=False):
    retry_config: Optional[object]

    server: Optional[str]

    server_url: Optional[str]

    timeout_ms: Optional[int]

    unstructured_api_key: Optional[str]

    url_params: Optional[object]


class IntegrationUnstructuredIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationUnstructuredIntegrationDefUpdateArguments]
    """Arguments for Unstructured partition integration"""

    method: Optional[str]

    provider: Literal["unstructured"]

    setup: Optional[IntegrationUnstructuredIntegrationDefUpdateSetup]
    """Setup parameters for Unstructured integration"""


class IntegrationAlgoliaIntegrationDefUpdateArguments(TypedDict, total=False):
    attributes_to_retrieve: Optional[object]

    hits_per_page: int

    index_name: Optional[str]

    query: Optional[str]


class IntegrationAlgoliaIntegrationDefUpdateSetup(TypedDict, total=False):
    algolia_api_key: Optional[str]

    algolia_application_id: Optional[str]


class IntegrationAlgoliaIntegrationDefUpdate(TypedDict, total=False):
    arguments: Optional[IntegrationAlgoliaIntegrationDefUpdateArguments]
    """Arguments for Algolia Search"""

    method: Optional[str]

    provider: Literal["algolia"]

    setup: Optional[IntegrationAlgoliaIntegrationDefUpdateSetup]
    """Integration definition for Algolia"""


Integration: TypeAlias = Union[
    IntegrationDummyIntegrationDefUpdate,
    IntegrationBraveIntegrationDefUpdate,
    IntegrationEmailIntegrationDefUpdate,
    IntegrationSpiderIntegrationDefUpdate,
    IntegrationWikipediaIntegrationDefUpdate,
    IntegrationWeatherIntegrationDefUpdate,
    IntegrationBrowserbaseContextIntegrationDefUpdate,
    IntegrationBrowserbaseExtensionIntegrationDefUpdate,
    IntegrationBrowserbaseListSessionsIntegrationDefUpdate,
    IntegrationBrowserbaseCreateSessionIntegrationDefUpdate,
    IntegrationBrowserbaseGetSessionIntegrationDefUpdate,
    IntegrationBrowserbaseCompleteSessionIntegrationDefUpdate,
    IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefUpdate,
    IntegrationRemoteBrowserIntegrationDefUpdate,
    IntegrationLlamaParseIntegrationDefUpdate,
    IntegrationFfmpegIntegrationDefUpdate,
    IntegrationCloudinaryUploadIntegrationDefUpdate,
    IntegrationCloudinaryEditIntegrationDefUpdate,
    IntegrationArxivIntegrationDefUpdate,
    IntegrationUnstructuredIntegrationDefUpdate,
    IntegrationAlgoliaIntegrationDefUpdate,
]


class System(TypedDict, total=False):
    arguments: Optional[object]

    operation: Optional[
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

    resource: Optional[Literal["agent", "user", "task", "execution", "doc", "session", "job"]]

    resource_id: Optional[str]

    subresource: Optional[Literal["tool", "doc", "execution", "transition"]]


class TextEditor20241022(TypedDict, total=False):
    name: str

    type: Literal["text_editor_20241022"]

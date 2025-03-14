# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ToolResetParams",
    "APICall",
    "Bash20241022",
    "Computer20241022",
    "Function",
    "Integration",
    "IntegrationDummyIntegrationDef",
    "IntegrationBraveIntegrationDef",
    "IntegrationBraveIntegrationDefArguments",
    "IntegrationBraveIntegrationDefSetup",
    "IntegrationEmailIntegrationDef",
    "IntegrationEmailIntegrationDefArguments",
    "IntegrationEmailIntegrationDefSetup",
    "IntegrationSpiderIntegrationDef",
    "IntegrationSpiderIntegrationDefArguments",
    "IntegrationSpiderIntegrationDefSetup",
    "IntegrationWikipediaIntegrationDef",
    "IntegrationWikipediaIntegrationDefArguments",
    "IntegrationWeatherIntegrationDef",
    "IntegrationWeatherIntegrationDefArguments",
    "IntegrationWeatherIntegrationDefSetup",
    "IntegrationBrowserbaseContextIntegrationDef",
    "IntegrationBrowserbaseContextIntegrationDefArguments",
    "IntegrationBrowserbaseContextIntegrationDefSetup",
    "IntegrationBrowserbaseExtensionIntegrationDef",
    "IntegrationBrowserbaseExtensionIntegrationDefArguments",
    "IntegrationBrowserbaseExtensionIntegrationDefSetup",
    "IntegrationBrowserbaseListSessionsIntegrationDef",
    "IntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "IntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "IntegrationBrowserbaseCreateSessionIntegrationDef",
    "IntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "IntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "IntegrationBrowserbaseGetSessionIntegrationDef",
    "IntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "IntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "IntegrationBrowserbaseCompleteSessionIntegrationDef",
    "IntegrationBrowserbaseCompleteSessionIntegrationDefArguments",
    "IntegrationBrowserbaseCompleteSessionIntegrationDefSetup",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "IntegrationRemoteBrowserIntegrationDef",
    "IntegrationRemoteBrowserIntegrationDefSetup",
    "IntegrationRemoteBrowserIntegrationDefArguments",
    "IntegrationLlamaParseIntegrationDef",
    "IntegrationLlamaParseIntegrationDefArguments",
    "IntegrationLlamaParseIntegrationDefSetup",
    "IntegrationFfmpegIntegrationDef",
    "IntegrationFfmpegIntegrationDefArguments",
    "IntegrationCloudinaryUploadIntegrationDef",
    "IntegrationCloudinaryUploadIntegrationDefArguments",
    "IntegrationCloudinaryUploadIntegrationDefSetup",
    "IntegrationCloudinaryEditIntegrationDef",
    "IntegrationCloudinaryEditIntegrationDefArguments",
    "IntegrationCloudinaryEditIntegrationDefSetup",
    "IntegrationArxivIntegrationDef",
    "IntegrationArxivIntegrationDefArguments",
    "IntegrationUnstructuredIntegrationDef",
    "IntegrationUnstructuredIntegrationDefArguments",
    "IntegrationUnstructuredIntegrationDefSetup",
    "IntegrationAlgoliaIntegrationDef",
    "IntegrationAlgoliaIntegrationDefArguments",
    "IntegrationAlgoliaIntegrationDefSetup",
    "System",
    "TextEditor20241022",
]


class ToolResetParams(TypedDict, total=False):
    agent_id: Required[str]

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

    bash_20241022: Optional[Bash20241022]

    computer_20241022: Optional[Computer20241022]
    """Anthropic new tools"""

    description: Optional[str]

    function: Optional[Function]
    """Function definition"""

    integration: Optional[Integration]
    """Brave integration definition"""

    system: Optional[System]
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022]


class APICall(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]]

    url: Required[str]

    content: Optional[str]

    cookies: Optional[Dict[str, str]]

    data: Optional[object]

    files: Optional[object]

    follow_redirects: Optional[bool]

    headers: Optional[Dict[str, str]]

    json: Optional[object]

    params: Union[str, object, None]

    schema: Optional[object]

    timeout: Optional[int]


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


class IntegrationDummyIntegrationDef(TypedDict, total=False):
    arguments: object

    method: Optional[str]

    provider: Literal["dummy"]

    setup: object


class IntegrationBraveIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]


class IntegrationBraveIntegrationDefSetup(TypedDict, total=False):
    brave_api_key: Required[str]


class IntegrationBraveIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBraveIntegrationDefArguments]
    """Arguments for Brave Search"""

    method: Optional[str]

    provider: Literal["brave"]

    setup: Optional[IntegrationBraveIntegrationDefSetup]
    """Integration definition for Brave Search"""


_IntegrationEmailIntegrationDefArgumentsReservedKeywords = TypedDict(
    "_IntegrationEmailIntegrationDefArgumentsReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class IntegrationEmailIntegrationDefArguments(_IntegrationEmailIntegrationDefArgumentsReservedKeywords, total=False):
    body: Required[str]

    subject: Required[str]

    to: Required[str]


class IntegrationEmailIntegrationDefSetup(TypedDict, total=False):
    host: Required[str]

    password: Required[str]

    port: Required[int]

    user: Required[str]


class IntegrationEmailIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationEmailIntegrationDefArguments]
    """Arguments for Email sending"""

    method: Optional[str]

    provider: Literal["email"]

    setup: Optional[IntegrationEmailIntegrationDefSetup]
    """Setup parameters for Email integration"""


class IntegrationSpiderIntegrationDefArguments(TypedDict, total=False):
    url: Required[str]

    content_type: Literal["application/json", "text/csv", "application/xml", "application/jsonl"]

    params: Optional[object]


class IntegrationSpiderIntegrationDefSetup(TypedDict, total=False):
    spider_api_key: Required[str]


class IntegrationSpiderIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationSpiderIntegrationDefArguments]
    """Arguments for Spider integration"""

    method: Optional[Literal["crawl", "links", "screenshot", "search"]]

    provider: Literal["spider"]

    setup: Optional[IntegrationSpiderIntegrationDefSetup]
    """Setup parameters for Spider integration"""


class IntegrationWikipediaIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]

    load_max_docs: int


class IntegrationWikipediaIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationWikipediaIntegrationDefArguments]
    """Arguments for Wikipedia Search"""

    method: Optional[str]

    provider: Literal["wikipedia"]

    setup: object


class IntegrationWeatherIntegrationDefArguments(TypedDict, total=False):
    location: Required[str]


class IntegrationWeatherIntegrationDefSetup(TypedDict, total=False):
    openweathermap_api_key: Required[str]


class IntegrationWeatherIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationWeatherIntegrationDefArguments]
    """Arguments for Weather"""

    method: Optional[str]

    provider: Literal["weather"]

    setup: Optional[IntegrationWeatherIntegrationDefSetup]
    """Integration definition for Weather"""


class IntegrationBrowserbaseContextIntegrationDefArguments(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]


class IntegrationBrowserbaseContextIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class IntegrationBrowserbaseContextIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseContextIntegrationDefArguments]

    method: Literal["create_context"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseContextIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseExtensionIntegrationDefArguments(TypedDict, total=False):
    repository_name: Required[Annotated[str, PropertyInfo(alias="repositoryName")]]

    ref: Optional[str]


class IntegrationBrowserbaseExtensionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class IntegrationBrowserbaseExtensionIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseExtensionIntegrationDefArguments]

    method: Optional[Literal["install_extension_from_github"]]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseExtensionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseListSessionsIntegrationDefArguments(TypedDict, total=False):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]]


class IntegrationBrowserbaseListSessionsIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class IntegrationBrowserbaseListSessionsIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseListSessionsIntegrationDefArguments]

    method: Literal["list_sessions"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseListSessionsIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCreateSessionIntegrationDefArguments(TypedDict, total=False):
    browser_settings: Annotated[object, PropertyInfo(alias="browserSettings")]

    extension_id: Annotated[Optional[str], PropertyInfo(alias="extensionId")]

    keep_alive: Annotated[bool, PropertyInfo(alias="keepAlive")]

    project_id: Annotated[Optional[str], PropertyInfo(alias="projectId")]

    proxies: Union[bool, Iterable[object]]

    timeout: int


class IntegrationBrowserbaseCreateSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class IntegrationBrowserbaseCreateSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefArguments]

    method: Literal["create_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]


class IntegrationBrowserbaseGetSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class IntegrationBrowserbaseGetSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseGetSessionIntegrationDefArguments]

    method: Literal["get_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseGetSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCompleteSessionIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]

    status: Literal["REQUEST_RELEASE"]


class IntegrationBrowserbaseCompleteSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class IntegrationBrowserbaseCompleteSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseCompleteSessionIntegrationDefArguments]

    method: Literal["complete_session"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseCompleteSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments]

    method: Literal["get_live_urls"]

    provider: Literal["browserbase"]

    setup: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class IntegrationRemoteBrowserIntegrationDefSetup(TypedDict, total=False):
    connect_url: Optional[str]

    height: Optional[int]

    width: Optional[int]


class IntegrationRemoteBrowserIntegrationDefArguments(TypedDict, total=False):
    action: Required[
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


class IntegrationRemoteBrowserIntegrationDef(TypedDict, total=False):
    setup: Required[IntegrationRemoteBrowserIntegrationDefSetup]
    """The setup parameters for the remote browser"""

    arguments: Optional[IntegrationRemoteBrowserIntegrationDefArguments]
    """The arguments for the remote browser"""

    method: Literal["perform_action"]

    provider: Literal["remote_browser"]


class IntegrationLlamaParseIntegrationDefArguments(TypedDict, total=False):
    file: Required[Union[str, List[str]]]

    base64: bool

    filename: Optional[str]

    params: Optional[object]


class IntegrationLlamaParseIntegrationDefSetup(TypedDict, total=False):
    llamaparse_api_key: Required[str]

    params: Optional[object]


class IntegrationLlamaParseIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationLlamaParseIntegrationDefArguments]
    """Arguments for LlamaParse integration"""

    method: Optional[str]

    provider: Literal["llama_parse"]

    setup: Optional[IntegrationLlamaParseIntegrationDefSetup]
    """Setup parameters for LlamaParse integration"""


class IntegrationFfmpegIntegrationDefArguments(TypedDict, total=False):
    cmd: Required[str]

    file: Union[str, List[str], None]


class IntegrationFfmpegIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationFfmpegIntegrationDefArguments]
    """Arguments for Ffmpeg CMD"""

    method: Optional[str]

    provider: Literal["ffmpeg"]

    setup: object


class IntegrationCloudinaryUploadIntegrationDefArguments(TypedDict, total=False):
    file: Required[str]

    public_id: Optional[str]

    return_base64: bool

    upload_params: Optional[object]


class IntegrationCloudinaryUploadIntegrationDefSetup(TypedDict, total=False):
    cloudinary_api_key: Required[str]

    cloudinary_api_secret: Required[str]

    cloudinary_cloud_name: Required[str]

    params: Optional[object]


class IntegrationCloudinaryUploadIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationCloudinaryUploadIntegrationDefArguments]
    """Arguments for Cloudinary media upload"""

    method: Literal["media_upload"]

    provider: Literal["cloudinary"]

    setup: Optional[IntegrationCloudinaryUploadIntegrationDefSetup]
    """Setup parameters for Cloudinary integration"""


class IntegrationCloudinaryEditIntegrationDefArguments(TypedDict, total=False):
    public_id: Required[str]

    transformation: Required[Iterable[object]]

    return_base64: bool


class IntegrationCloudinaryEditIntegrationDefSetup(TypedDict, total=False):
    cloudinary_api_key: Required[str]

    cloudinary_api_secret: Required[str]

    cloudinary_cloud_name: Required[str]

    params: Optional[object]


class IntegrationCloudinaryEditIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationCloudinaryEditIntegrationDefArguments]
    """Arguments for Cloudinary media edit"""

    method: Literal["media_edit"]

    provider: Literal["cloudinary"]

    setup: Optional[IntegrationCloudinaryEditIntegrationDefSetup]
    """Setup parameters for Cloudinary integration"""


class IntegrationArxivIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]

    download_pdf: bool

    id_list: Optional[List[str]]

    max_results: int

    sort_by: Literal["relevance", "lastUpdatedDate", "submittedDate"]

    sort_order: Literal["ascending", "descending"]


class IntegrationArxivIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationArxivIntegrationDefArguments]
    """Arguments for Arxiv Search"""

    method: Optional[str]

    provider: Literal["arxiv"]

    setup: object


class IntegrationUnstructuredIntegrationDefArguments(TypedDict, total=False):
    file: Required[str]

    filename: Optional[str]

    partition_params: Optional[object]


class IntegrationUnstructuredIntegrationDefSetup(TypedDict, total=False):
    unstructured_api_key: Required[str]

    retry_config: Optional[object]

    server: Optional[str]

    server_url: Optional[str]

    timeout_ms: Optional[int]

    url_params: Optional[object]


class IntegrationUnstructuredIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationUnstructuredIntegrationDefArguments]
    """Arguments for Unstructured partition integration"""

    method: Optional[str]

    provider: Literal["unstructured"]

    setup: Optional[IntegrationUnstructuredIntegrationDefSetup]
    """Setup parameters for Unstructured integration"""


class IntegrationAlgoliaIntegrationDefArguments(TypedDict, total=False):
    index_name: Required[str]

    query: Required[str]

    attributes_to_retrieve: Optional[object]

    hits_per_page: int


class IntegrationAlgoliaIntegrationDefSetup(TypedDict, total=False):
    algolia_api_key: Required[str]

    algolia_application_id: Required[str]


class IntegrationAlgoliaIntegrationDef(TypedDict, total=False):
    arguments: Optional[IntegrationAlgoliaIntegrationDefArguments]
    """Arguments for Algolia Search"""

    method: Optional[str]

    provider: Literal["algolia"]

    setup: Optional[IntegrationAlgoliaIntegrationDefSetup]
    """Integration definition for Algolia"""


Integration: TypeAlias = Union[
    IntegrationDummyIntegrationDef,
    IntegrationBraveIntegrationDef,
    IntegrationEmailIntegrationDef,
    IntegrationSpiderIntegrationDef,
    IntegrationWikipediaIntegrationDef,
    IntegrationWeatherIntegrationDef,
    IntegrationBrowserbaseContextIntegrationDef,
    IntegrationBrowserbaseExtensionIntegrationDef,
    IntegrationBrowserbaseListSessionsIntegrationDef,
    IntegrationBrowserbaseCreateSessionIntegrationDef,
    IntegrationBrowserbaseGetSessionIntegrationDef,
    IntegrationBrowserbaseCompleteSessionIntegrationDef,
    IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
    IntegrationRemoteBrowserIntegrationDef,
    IntegrationLlamaParseIntegrationDef,
    IntegrationFfmpegIntegrationDef,
    IntegrationCloudinaryUploadIntegrationDef,
    IntegrationCloudinaryEditIntegrationDef,
    IntegrationArxivIntegrationDef,
    IntegrationUnstructuredIntegrationDef,
    IntegrationAlgoliaIntegrationDef,
]


class System(TypedDict, total=False):
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


class TextEditor20241022(TypedDict, total=False):
    name: str

    type: Literal["text_editor_20241022"]

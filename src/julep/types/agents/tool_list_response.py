# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ToolListResponse",
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


class APICall(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "CONNECT", "TRACE"]

    url: str

    content: Optional[str] = None

    cookies: Optional[Dict[str, str]] = None

    data: Optional[object] = None

    files: Optional[object] = None

    follow_redirects: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    json_: Optional[object] = FieldInfo(alias="json", default=None)

    params: Union[str, object, None] = None

    schema_: Optional[object] = FieldInfo(alias="schema", default=None)

    timeout: Optional[int] = None


class Bash20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["bash_20241022"]] = None


class Computer20241022(BaseModel):
    display_height_px: Optional[int] = None

    display_number: Optional[int] = None

    display_width_px: Optional[int] = None

    name: Optional[str] = None

    type: Optional[Literal["computer_20241022"]] = None


class Function(BaseModel):
    description: Optional[object] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class IntegrationDummyIntegrationDef(BaseModel):
    arguments: Optional[object] = None

    method: Optional[str] = None

    provider: Optional[Literal["dummy"]] = None

    setup: Optional[object] = None


class IntegrationBraveIntegrationDefArguments(BaseModel):
    query: str


class IntegrationBraveIntegrationDefSetup(BaseModel):
    brave_api_key: str


class IntegrationBraveIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBraveIntegrationDefArguments] = None
    """Arguments for Brave Search"""

    method: Optional[str] = None

    provider: Optional[Literal["brave"]] = None

    setup: Optional[IntegrationBraveIntegrationDefSetup] = None
    """Integration definition for Brave Search"""


class IntegrationEmailIntegrationDefArguments(BaseModel):
    body: str

    from_: str = FieldInfo(alias="from")

    subject: str

    to: str


class IntegrationEmailIntegrationDefSetup(BaseModel):
    host: str

    password: str

    port: int

    user: str


class IntegrationEmailIntegrationDef(BaseModel):
    arguments: Optional[IntegrationEmailIntegrationDefArguments] = None
    """Arguments for Email sending"""

    method: Optional[str] = None

    provider: Optional[Literal["email"]] = None

    setup: Optional[IntegrationEmailIntegrationDefSetup] = None
    """Setup parameters for Email integration"""


class IntegrationSpiderIntegrationDefArguments(BaseModel):
    url: str

    content_type: Optional[Literal["application/json", "text/csv", "application/xml", "application/jsonl"]] = None

    params: Optional[object] = None


class IntegrationSpiderIntegrationDefSetup(BaseModel):
    spider_api_key: str


class IntegrationSpiderIntegrationDef(BaseModel):
    arguments: Optional[IntegrationSpiderIntegrationDefArguments] = None
    """Arguments for Spider integration"""

    method: Optional[Literal["crawl", "links", "screenshot", "search"]] = None

    provider: Optional[Literal["spider"]] = None

    setup: Optional[IntegrationSpiderIntegrationDefSetup] = None
    """Setup parameters for Spider integration"""


class IntegrationWikipediaIntegrationDefArguments(BaseModel):
    query: str

    load_max_docs: Optional[int] = None


class IntegrationWikipediaIntegrationDef(BaseModel):
    arguments: Optional[IntegrationWikipediaIntegrationDefArguments] = None
    """Arguments for Wikipedia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["wikipedia"]] = None

    setup: Optional[object] = None


class IntegrationWeatherIntegrationDefArguments(BaseModel):
    location: str


class IntegrationWeatherIntegrationDefSetup(BaseModel):
    openweathermap_api_key: str


class IntegrationWeatherIntegrationDef(BaseModel):
    arguments: Optional[IntegrationWeatherIntegrationDefArguments] = None
    """Arguments for Weather"""

    method: Optional[str] = None

    provider: Optional[Literal["weather"]] = None

    setup: Optional[IntegrationWeatherIntegrationDefSetup] = None
    """Integration definition for Weather"""


class IntegrationBrowserbaseContextIntegrationDefArguments(BaseModel):
    project_id: str = FieldInfo(alias="projectId")


class IntegrationBrowserbaseContextIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class IntegrationBrowserbaseContextIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseContextIntegrationDefArguments] = None

    method: Optional[Literal["create_context"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseContextIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseExtensionIntegrationDefArguments(BaseModel):
    repository_name: str = FieldInfo(alias="repositoryName")

    ref: Optional[str] = None


class IntegrationBrowserbaseExtensionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class IntegrationBrowserbaseExtensionIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseExtensionIntegrationDefArguments] = None

    method: Optional[Literal["install_extension_from_github"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseExtensionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseListSessionsIntegrationDefArguments(BaseModel):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]] = None


class IntegrationBrowserbaseListSessionsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class IntegrationBrowserbaseListSessionsIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseListSessionsIntegrationDefArguments] = None

    method: Optional[Literal["list_sessions"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseListSessionsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCreateSessionIntegrationDefArguments(BaseModel):
    browser_settings: Optional[object] = FieldInfo(alias="browserSettings", default=None)

    extension_id: Optional[str] = FieldInfo(alias="extensionId", default=None)

    keep_alive: Optional[bool] = FieldInfo(alias="keepAlive", default=None)

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)

    proxies: Union[bool, List[object], None] = None

    timeout: Optional[int] = None


class IntegrationBrowserbaseCreateSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class IntegrationBrowserbaseCreateSessionIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefArguments] = None

    method: Optional[Literal["create_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseCreateSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionIntegrationDefArguments(BaseModel):
    id: str


class IntegrationBrowserbaseGetSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class IntegrationBrowserbaseGetSessionIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseGetSessionIntegrationDefArguments] = None

    method: Optional[Literal["get_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseGetSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseCompleteSessionIntegrationDefArguments(BaseModel):
    id: str

    status: Optional[Literal["REQUEST_RELEASE"]] = None


class IntegrationBrowserbaseCompleteSessionIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class IntegrationBrowserbaseCompleteSessionIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseCompleteSessionIntegrationDefArguments] = None

    method: Optional[Literal["complete_session"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseCompleteSessionIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(BaseModel):
    id: str


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(BaseModel):
    api_key: str

    project_id: str

    api_url: Optional[str] = None

    connect_url: Optional[str] = None


class IntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(BaseModel):
    arguments: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments] = None

    method: Optional[Literal["get_live_urls"]] = None

    provider: Optional[Literal["browserbase"]] = None

    setup: Optional[IntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup] = None
    """The setup parameters for the browserbase integration"""


class IntegrationRemoteBrowserIntegrationDefSetup(BaseModel):
    connect_url: Optional[str] = None

    height: Optional[int] = None

    width: Optional[int] = None


class IntegrationRemoteBrowserIntegrationDefArguments(BaseModel):
    action: Literal[
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

    connect_url: Optional[str] = None

    coordinate: Optional[List[object]] = None

    text: Optional[str] = None


class IntegrationRemoteBrowserIntegrationDef(BaseModel):
    setup: IntegrationRemoteBrowserIntegrationDefSetup
    """The setup parameters for the remote browser"""

    arguments: Optional[IntegrationRemoteBrowserIntegrationDefArguments] = None
    """The arguments for the remote browser"""

    method: Optional[Literal["perform_action"]] = None

    provider: Optional[Literal["remote_browser"]] = None


class IntegrationLlamaParseIntegrationDefArguments(BaseModel):
    file: Union[str, List[str]]

    base64: Optional[bool] = None

    filename: Optional[str] = None

    params: Optional[object] = None


class IntegrationLlamaParseIntegrationDefSetup(BaseModel):
    llamaparse_api_key: str

    params: Optional[object] = None


class IntegrationLlamaParseIntegrationDef(BaseModel):
    arguments: Optional[IntegrationLlamaParseIntegrationDefArguments] = None
    """Arguments for LlamaParse integration"""

    method: Optional[str] = None

    provider: Optional[Literal["llama_parse"]] = None

    setup: Optional[IntegrationLlamaParseIntegrationDefSetup] = None
    """Setup parameters for LlamaParse integration"""


class IntegrationFfmpegIntegrationDefArguments(BaseModel):
    cmd: str

    file: Union[str, List[str], None] = None


class IntegrationFfmpegIntegrationDef(BaseModel):
    arguments: Optional[IntegrationFfmpegIntegrationDefArguments] = None
    """Arguments for Ffmpeg CMD"""

    method: Optional[str] = None

    provider: Optional[Literal["ffmpeg"]] = None

    setup: Optional[object] = None


class IntegrationCloudinaryUploadIntegrationDefArguments(BaseModel):
    file: str

    public_id: Optional[str] = None

    return_base64: Optional[bool] = None

    upload_params: Optional[object] = None


class IntegrationCloudinaryUploadIntegrationDefSetup(BaseModel):
    cloudinary_api_key: str

    cloudinary_api_secret: str

    cloudinary_cloud_name: str

    params: Optional[object] = None


class IntegrationCloudinaryUploadIntegrationDef(BaseModel):
    arguments: Optional[IntegrationCloudinaryUploadIntegrationDefArguments] = None
    """Arguments for Cloudinary media upload"""

    method: Optional[Literal["media_upload"]] = None

    provider: Optional[Literal["cloudinary"]] = None

    setup: Optional[IntegrationCloudinaryUploadIntegrationDefSetup] = None
    """Setup parameters for Cloudinary integration"""


class IntegrationCloudinaryEditIntegrationDefArguments(BaseModel):
    public_id: str

    transformation: List[object]

    return_base64: Optional[bool] = None


class IntegrationCloudinaryEditIntegrationDefSetup(BaseModel):
    cloudinary_api_key: str

    cloudinary_api_secret: str

    cloudinary_cloud_name: str

    params: Optional[object] = None


class IntegrationCloudinaryEditIntegrationDef(BaseModel):
    arguments: Optional[IntegrationCloudinaryEditIntegrationDefArguments] = None
    """Arguments for Cloudinary media edit"""

    method: Optional[Literal["media_edit"]] = None

    provider: Optional[Literal["cloudinary"]] = None

    setup: Optional[IntegrationCloudinaryEditIntegrationDefSetup] = None
    """Setup parameters for Cloudinary integration"""


class IntegrationArxivIntegrationDefArguments(BaseModel):
    query: str

    download_pdf: Optional[bool] = None

    id_list: Optional[List[str]] = None

    max_results: Optional[int] = None

    sort_by: Optional[Literal["relevance", "lastUpdatedDate", "submittedDate"]] = None

    sort_order: Optional[Literal["ascending", "descending"]] = None


class IntegrationArxivIntegrationDef(BaseModel):
    arguments: Optional[IntegrationArxivIntegrationDefArguments] = None
    """Arguments for Arxiv Search"""

    method: Optional[str] = None

    provider: Optional[Literal["arxiv"]] = None

    setup: Optional[object] = None


class IntegrationUnstructuredIntegrationDefArguments(BaseModel):
    file: str

    filename: Optional[str] = None

    partition_params: Optional[object] = None


class IntegrationUnstructuredIntegrationDefSetup(BaseModel):
    unstructured_api_key: str

    retry_config: Optional[object] = None

    server: Optional[str] = None

    server_url: Optional[str] = None

    timeout_ms: Optional[int] = None

    url_params: Optional[object] = None


class IntegrationUnstructuredIntegrationDef(BaseModel):
    arguments: Optional[IntegrationUnstructuredIntegrationDefArguments] = None
    """Arguments for Unstructured partition integration"""

    method: Optional[str] = None

    provider: Optional[Literal["unstructured"]] = None

    setup: Optional[IntegrationUnstructuredIntegrationDefSetup] = None
    """Setup parameters for Unstructured integration"""


class IntegrationAlgoliaIntegrationDefArguments(BaseModel):
    index_name: str

    query: str

    attributes_to_retrieve: Optional[object] = None

    hits_per_page: Optional[int] = None


class IntegrationAlgoliaIntegrationDefSetup(BaseModel):
    algolia_api_key: str

    algolia_application_id: str


class IntegrationAlgoliaIntegrationDef(BaseModel):
    arguments: Optional[IntegrationAlgoliaIntegrationDefArguments] = None
    """Arguments for Algolia Search"""

    method: Optional[str] = None

    provider: Optional[Literal["algolia"]] = None

    setup: Optional[IntegrationAlgoliaIntegrationDefSetup] = None
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
    None,
]


class System(BaseModel):
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


class TextEditor20241022(BaseModel):
    name: Optional[str] = None

    type: Optional[Literal["text_editor_20241022"]] = None


class ToolListResponse(BaseModel):
    id: str

    created_at: datetime

    name: str

    type: Literal[
        "function", "integration", "system", "api_call", "computer_20241022", "text_editor_20241022", "bash_20241022"
    ]

    updated_at: datetime

    api_call: Optional[APICall] = None
    """API call definition"""

    bash_20241022: Optional[Bash20241022] = None

    computer_20241022: Optional[Computer20241022] = None
    """Anthropic new tools"""

    description: Optional[str] = None

    function: Optional[Function] = None
    """Function definition"""

    integration: Optional[Integration] = None
    """Brave integration definition"""

    system: Optional[System] = None
    """System definition"""

    text_editor_20241022: Optional[TextEditor20241022] = None

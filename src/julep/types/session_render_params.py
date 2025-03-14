# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SessionRenderParams",
    "Message",
    "MessageContentUnionMember2",
    "MessageContentUnionMember2Content",
    "MessageContentUnionMember2ContentModel7",
    "MessageContentUnionMember2ContentModel7ImageURL",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInput",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember0",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1",
    "MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1Source",
    "MessageToolCall",
    "MessageToolCallChosenFunctionCall",
    "MessageToolCallChosenFunctionCallFunction",
    "MessageToolCallChosenFunctionCallBash20241022",
    "MessageToolCallChosenFunctionCallComputer20241022",
    "MessageToolCallChosenFunctionCallTextEditor20241022",
    "MessageToolCallChosenComputer20241022",
    "MessageToolCallChosenTextEditor20241022",
    "MessageToolCallChosenBash20241022",
    "ResponseFormat",
    "ResponseFormatSimpleCompletionResponseFormat",
    "ResponseFormatSchemaCompletionResponseFormat",
    "ToolChoice",
    "ToolChoiceNamedToolChoice",
    "ToolChoiceNamedToolChoiceFunction",
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
    "ToolIntegrationBrowserbaseContextIntegrationDef",
    "ToolIntegrationBrowserbaseContextIntegrationDefArguments",
    "ToolIntegrationBrowserbaseContextIntegrationDefSetup",
    "ToolIntegrationBrowserbaseExtensionIntegrationDef",
    "ToolIntegrationBrowserbaseExtensionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseExtensionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseListSessionsIntegrationDef",
    "ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments",
    "ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup",
    "ToolIntegrationBrowserbaseCreateSessionIntegrationDef",
    "ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseGetSessionIntegrationDef",
    "ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseCompleteSessionIntegrationDef",
    "ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments",
    "ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup",
    "ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef",
    "ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments",
    "ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup",
    "ToolIntegrationRemoteBrowserIntegrationDef",
    "ToolIntegrationRemoteBrowserIntegrationDefSetup",
    "ToolIntegrationRemoteBrowserIntegrationDefArguments",
    "ToolIntegrationLlamaParseIntegrationDef",
    "ToolIntegrationLlamaParseIntegrationDefArguments",
    "ToolIntegrationLlamaParseIntegrationDefSetup",
    "ToolIntegrationFfmpegIntegrationDef",
    "ToolIntegrationFfmpegIntegrationDefArguments",
    "ToolIntegrationCloudinaryUploadIntegrationDef",
    "ToolIntegrationCloudinaryUploadIntegrationDefArguments",
    "ToolIntegrationCloudinaryUploadIntegrationDefSetup",
    "ToolIntegrationCloudinaryEditIntegrationDef",
    "ToolIntegrationCloudinaryEditIntegrationDefArguments",
    "ToolIntegrationCloudinaryEditIntegrationDefSetup",
    "ToolIntegrationArxivIntegrationDef",
    "ToolIntegrationArxivIntegrationDefArguments",
    "ToolIntegrationUnstructuredIntegrationDef",
    "ToolIntegrationUnstructuredIntegrationDefArguments",
    "ToolIntegrationUnstructuredIntegrationDefSetup",
    "ToolIntegrationAlgoliaIntegrationDef",
    "ToolIntegrationAlgoliaIntegrationDefArguments",
    "ToolIntegrationAlgoliaIntegrationDefSetup",
    "ToolSystem",
    "ToolTextEditor20241022",
]


class SessionRenderParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    agent: Optional[str]

    frequency_penalty: Optional[float]

    length_penalty: Optional[float]

    logit_bias: Optional[Dict[str, float]]

    max_tokens: Optional[int]

    min_p: Optional[float]

    model: Optional[str]

    presence_penalty: Optional[float]

    recall: bool

    repetition_penalty: Optional[float]

    response_format: Optional[ResponseFormat]

    save: bool

    seed: Optional[int]

    stop: List[str]

    stream: bool

    temperature: Optional[float]

    tool_choice: Optional[ToolChoice]

    tools: Optional[Iterable[Tool]]

    top_p: Optional[float]


class MessageContentUnionMember2Content(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MessageContentUnionMember2ContentModel7ImageURL(TypedDict, total=False):
    url: Required[str]

    detail: Literal["low", "high", "auto"]


class MessageContentUnionMember2ContentModel7(TypedDict, total=False):
    image_url: Required[MessageContentUnionMember2ContentModel7ImageURL]
    """The image URL"""

    type: Literal["image_url"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Literal["text"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1Source(TypedDict, total=False):
    data: Required[str]

    media_type: Required[str]

    type: Literal["base64"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1(TypedDict, total=False):
    source: Required[MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1Source]

    type: Literal["image"]


class MessageContentUnionMember2AgentsAPIAutogenChatContentModelInput(TypedDict, total=False):
    content: Required[
        Union[
            Iterable[MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember0],
            Iterable[MessageContentUnionMember2AgentsAPIAutogenChatContentModelInputContentUnionMember1],
        ]
    ]

    tool_use_id: Required[str]

    type: Literal["tool_result"]


MessageContentUnionMember2: TypeAlias = Union[
    MessageContentUnionMember2Content,
    MessageContentUnionMember2ContentModel7,
    MessageContentUnionMember2AgentsAPIAutogenChatContentModelInput,
]


class MessageToolCallChosenFunctionCallFunction(TypedDict, total=False):
    name: Required[str]

    arguments: Optional[str]


class MessageToolCallChosenFunctionCallBash20241022(TypedDict, total=False):
    command: Optional[str]

    restart: bool


class MessageToolCallChosenFunctionCallComputer20241022(TypedDict, total=False):
    action: Required[
        Literal[
            "key",
            "type",
            "cursor_position",
            "mouse_move",
            "left_click",
            "right_click",
            "middle_click",
            "double_click",
            "screenshot",
        ]
    ]

    coordinate: Optional[Iterable[int]]

    text: Optional[str]


class MessageToolCallChosenFunctionCallTextEditor20241022(TypedDict, total=False):
    command: Required[Literal["str_replace", "insert", "view", "undo_edit"]]

    path: Required[str]

    file_text: Optional[str]

    insert_line: Optional[int]

    new_str: Optional[str]

    old_str: Optional[str]

    view_range: Optional[Iterable[int]]


class MessageToolCallChosenFunctionCall(TypedDict, total=False):
    function: Required[MessageToolCallChosenFunctionCallFunction]

    api_call: object

    bash_20241022: Optional[MessageToolCallChosenFunctionCallBash20241022]

    computer_20241022: Optional[MessageToolCallChosenFunctionCallComputer20241022]

    integration: object

    system: object

    text_editor_20241022: Optional[MessageToolCallChosenFunctionCallTextEditor20241022]

    type: Literal["function"]


class MessageToolCallChosenComputer20241022(TypedDict, total=False):
    action: Required[
        Literal[
            "key",
            "type",
            "cursor_position",
            "mouse_move",
            "left_click",
            "right_click",
            "middle_click",
            "double_click",
            "screenshot",
        ]
    ]

    coordinate: Optional[Iterable[int]]

    text: Optional[str]


class MessageToolCallChosenTextEditor20241022(TypedDict, total=False):
    command: Required[Literal["str_replace", "insert", "view", "undo_edit"]]

    path: Required[str]

    file_text: Optional[str]

    insert_line: Optional[int]

    new_str: Optional[str]

    old_str: Optional[str]

    view_range: Optional[Iterable[int]]


class MessageToolCallChosenBash20241022(TypedDict, total=False):
    command: Optional[str]

    restart: bool


MessageToolCall: TypeAlias = Union[
    MessageToolCallChosenFunctionCall,
    MessageToolCallChosenComputer20241022,
    MessageToolCallChosenTextEditor20241022,
    MessageToolCallChosenBash20241022,
]

_MessageReservedKeywords = TypedDict(
    "_MessageReservedKeywords",
    {
        "continue": Optional[bool],
    },
    total=False,
)


class Message(_MessageReservedKeywords, total=False):
    role: Required[Literal["user", "assistant", "system", "tool"]]

    content: Union[str, List[str], Iterable[MessageContentUnionMember2], None]

    name: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[MessageToolCall]]


class ResponseFormatSimpleCompletionResponseFormat(TypedDict, total=False):
    type: Literal["text", "json_object"]


class ResponseFormatSchemaCompletionResponseFormat(TypedDict, total=False):
    json_schema: Required[object]

    type: Literal["json_schema"]


ResponseFormat: TypeAlias = Union[
    ResponseFormatSimpleCompletionResponseFormat, ResponseFormatSchemaCompletionResponseFormat
]


class ToolChoiceNamedToolChoiceFunction(TypedDict, total=False):
    name: Required[str]

    arguments: Optional[str]


class ToolChoiceNamedToolChoice(TypedDict, total=False):
    function: Optional[ToolChoiceNamedToolChoiceFunction]


ToolChoice: TypeAlias = Union[Literal["auto", "none"], ToolChoiceNamedToolChoice]


class ToolAPICall(TypedDict, total=False):
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
    description: object

    name: object

    parameters: Optional[object]


class ToolIntegrationDummyIntegrationDef(TypedDict, total=False):
    arguments: object

    method: Optional[str]

    provider: Literal["dummy"]

    setup: object


class ToolIntegrationBraveIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]


class ToolIntegrationBraveIntegrationDefSetup(TypedDict, total=False):
    brave_api_key: Required[str]


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

    content_type: Literal["application/json", "text/csv", "application/xml", "application/jsonl"]

    params: Optional[object]


class ToolIntegrationSpiderIntegrationDefSetup(TypedDict, total=False):
    spider_api_key: Required[str]


class ToolIntegrationSpiderIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationSpiderIntegrationDefArguments]
    """Arguments for Spider integration"""

    method: Optional[Literal["crawl", "links", "screenshot", "search"]]

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

    setup: object


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


class ToolIntegrationBrowserbaseContextIntegrationDefArguments(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]


class ToolIntegrationBrowserbaseContextIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class ToolIntegrationBrowserbaseContextIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBrowserbaseContextIntegrationDefArguments]

    method: Literal["create_context"]

    provider: Literal["browserbase"]

    setup: Optional[ToolIntegrationBrowserbaseContextIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseExtensionIntegrationDefArguments(TypedDict, total=False):
    repository_name: Required[Annotated[str, PropertyInfo(alias="repositoryName")]]

    ref: Optional[str]


class ToolIntegrationBrowserbaseExtensionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class ToolIntegrationBrowserbaseExtensionIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBrowserbaseExtensionIntegrationDefArguments]

    method: Optional[Literal["install_extension_from_github"]]

    provider: Literal["browserbase"]

    setup: Optional[ToolIntegrationBrowserbaseExtensionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments(TypedDict, total=False):
    status: Optional[Literal["RUNNING", "ERROR", "TIMED_OUT", "COMPLETED"]]


class ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class ToolIntegrationBrowserbaseListSessionsIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBrowserbaseListSessionsIntegrationDefArguments]

    method: Literal["list_sessions"]

    provider: Literal["browserbase"]

    setup: Optional[ToolIntegrationBrowserbaseListSessionsIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments(TypedDict, total=False):
    browser_settings: Annotated[object, PropertyInfo(alias="browserSettings")]

    extension_id: Annotated[Optional[str], PropertyInfo(alias="extensionId")]

    keep_alive: Annotated[bool, PropertyInfo(alias="keepAlive")]

    project_id: Annotated[Optional[str], PropertyInfo(alias="projectId")]

    proxies: Union[bool, Iterable[object]]

    timeout: int


class ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class ToolIntegrationBrowserbaseCreateSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBrowserbaseCreateSessionIntegrationDefArguments]

    method: Literal["create_session"]

    provider: Literal["browserbase"]

    setup: Optional[ToolIntegrationBrowserbaseCreateSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]


class ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class ToolIntegrationBrowserbaseGetSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBrowserbaseGetSessionIntegrationDefArguments]

    method: Literal["get_session"]

    provider: Literal["browserbase"]

    setup: Optional[ToolIntegrationBrowserbaseGetSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]

    status: Literal["REQUEST_RELEASE"]


class ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class ToolIntegrationBrowserbaseCompleteSessionIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBrowserbaseCompleteSessionIntegrationDefArguments]

    method: Literal["complete_session"]

    provider: Literal["browserbase"]

    setup: Optional[ToolIntegrationBrowserbaseCompleteSessionIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments(TypedDict, total=False):
    id: Required[str]


class ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup(TypedDict, total=False):
    api_key: Required[str]

    project_id: Required[str]

    api_url: Optional[str]

    connect_url: Optional[str]


class ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefArguments]

    method: Literal["get_live_urls"]

    provider: Literal["browserbase"]

    setup: Optional[ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDefSetup]
    """The setup parameters for the browserbase integration"""


class ToolIntegrationRemoteBrowserIntegrationDefSetup(TypedDict, total=False):
    connect_url: Optional[str]

    height: Optional[int]

    width: Optional[int]


class ToolIntegrationRemoteBrowserIntegrationDefArguments(TypedDict, total=False):
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


class ToolIntegrationRemoteBrowserIntegrationDef(TypedDict, total=False):
    setup: Required[ToolIntegrationRemoteBrowserIntegrationDefSetup]
    """The setup parameters for the remote browser"""

    arguments: Optional[ToolIntegrationRemoteBrowserIntegrationDefArguments]
    """The arguments for the remote browser"""

    method: Literal["perform_action"]

    provider: Literal["remote_browser"]


class ToolIntegrationLlamaParseIntegrationDefArguments(TypedDict, total=False):
    file: Required[Union[str, List[str]]]

    base64: bool

    filename: Optional[str]

    params: Optional[object]


class ToolIntegrationLlamaParseIntegrationDefSetup(TypedDict, total=False):
    llamaparse_api_key: Required[str]

    params: Optional[object]


class ToolIntegrationLlamaParseIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationLlamaParseIntegrationDefArguments]
    """Arguments for LlamaParse integration"""

    method: Optional[str]

    provider: Literal["llama_parse"]

    setup: Optional[ToolIntegrationLlamaParseIntegrationDefSetup]
    """Setup parameters for LlamaParse integration"""


class ToolIntegrationFfmpegIntegrationDefArguments(TypedDict, total=False):
    cmd: Required[str]

    file: Union[str, List[str], None]


class ToolIntegrationFfmpegIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationFfmpegIntegrationDefArguments]
    """Arguments for Ffmpeg CMD"""

    method: Optional[str]

    provider: Literal["ffmpeg"]

    setup: object


class ToolIntegrationCloudinaryUploadIntegrationDefArguments(TypedDict, total=False):
    file: Required[str]

    public_id: Optional[str]

    return_base64: bool

    upload_params: Optional[object]


class ToolIntegrationCloudinaryUploadIntegrationDefSetup(TypedDict, total=False):
    cloudinary_api_key: Required[str]

    cloudinary_api_secret: Required[str]

    cloudinary_cloud_name: Required[str]

    params: Optional[object]


class ToolIntegrationCloudinaryUploadIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationCloudinaryUploadIntegrationDefArguments]
    """Arguments for Cloudinary media upload"""

    method: Literal["media_upload"]

    provider: Literal["cloudinary"]

    setup: Optional[ToolIntegrationCloudinaryUploadIntegrationDefSetup]
    """Setup parameters for Cloudinary integration"""


class ToolIntegrationCloudinaryEditIntegrationDefArguments(TypedDict, total=False):
    public_id: Required[str]

    transformation: Required[Iterable[object]]

    return_base64: bool


class ToolIntegrationCloudinaryEditIntegrationDefSetup(TypedDict, total=False):
    cloudinary_api_key: Required[str]

    cloudinary_api_secret: Required[str]

    cloudinary_cloud_name: Required[str]

    params: Optional[object]


class ToolIntegrationCloudinaryEditIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationCloudinaryEditIntegrationDefArguments]
    """Arguments for Cloudinary media edit"""

    method: Literal["media_edit"]

    provider: Literal["cloudinary"]

    setup: Optional[ToolIntegrationCloudinaryEditIntegrationDefSetup]
    """Setup parameters for Cloudinary integration"""


class ToolIntegrationArxivIntegrationDefArguments(TypedDict, total=False):
    query: Required[str]

    download_pdf: bool

    id_list: Optional[List[str]]

    max_results: int

    sort_by: Literal["relevance", "lastUpdatedDate", "submittedDate"]

    sort_order: Literal["ascending", "descending"]


class ToolIntegrationArxivIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationArxivIntegrationDefArguments]
    """Arguments for Arxiv Search"""

    method: Optional[str]

    provider: Literal["arxiv"]

    setup: object


class ToolIntegrationUnstructuredIntegrationDefArguments(TypedDict, total=False):
    file: Required[str]

    filename: Optional[str]

    partition_params: Optional[object]


class ToolIntegrationUnstructuredIntegrationDefSetup(TypedDict, total=False):
    unstructured_api_key: Required[str]

    retry_config: Optional[object]

    server: Optional[str]

    server_url: Optional[str]

    timeout_ms: Optional[int]

    url_params: Optional[object]


class ToolIntegrationUnstructuredIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationUnstructuredIntegrationDefArguments]
    """Arguments for Unstructured partition integration"""

    method: Optional[str]

    provider: Literal["unstructured"]

    setup: Optional[ToolIntegrationUnstructuredIntegrationDefSetup]
    """Setup parameters for Unstructured integration"""


class ToolIntegrationAlgoliaIntegrationDefArguments(TypedDict, total=False):
    index_name: Required[str]

    query: Required[str]

    attributes_to_retrieve: Optional[object]

    hits_per_page: int


class ToolIntegrationAlgoliaIntegrationDefSetup(TypedDict, total=False):
    algolia_api_key: Required[str]

    algolia_application_id: Required[str]


class ToolIntegrationAlgoliaIntegrationDef(TypedDict, total=False):
    arguments: Optional[ToolIntegrationAlgoliaIntegrationDefArguments]
    """Arguments for Algolia Search"""

    method: Optional[str]

    provider: Literal["algolia"]

    setup: Optional[ToolIntegrationAlgoliaIntegrationDefSetup]
    """Integration definition for Algolia"""


ToolIntegration: TypeAlias = Union[
    ToolIntegrationDummyIntegrationDef,
    ToolIntegrationBraveIntegrationDef,
    ToolIntegrationEmailIntegrationDef,
    ToolIntegrationSpiderIntegrationDef,
    ToolIntegrationWikipediaIntegrationDef,
    ToolIntegrationWeatherIntegrationDef,
    ToolIntegrationBrowserbaseContextIntegrationDef,
    ToolIntegrationBrowserbaseExtensionIntegrationDef,
    ToolIntegrationBrowserbaseListSessionsIntegrationDef,
    ToolIntegrationBrowserbaseCreateSessionIntegrationDef,
    ToolIntegrationBrowserbaseGetSessionIntegrationDef,
    ToolIntegrationBrowserbaseCompleteSessionIntegrationDef,
    ToolIntegrationBrowserbaseGetSessionLiveURLsIntegrationDef,
    ToolIntegrationRemoteBrowserIntegrationDef,
    ToolIntegrationLlamaParseIntegrationDef,
    ToolIntegrationFfmpegIntegrationDef,
    ToolIntegrationCloudinaryUploadIntegrationDef,
    ToolIntegrationCloudinaryEditIntegrationDef,
    ToolIntegrationArxivIntegrationDef,
    ToolIntegrationUnstructuredIntegrationDef,
    ToolIntegrationAlgoliaIntegrationDef,
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

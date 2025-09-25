# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    session_chat_params,
    session_list_params,
    session_reset_params,
    session_create_params,
    session_render_params,
    session_update_params,
    session_create_or_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.history import History
from ..types.session import Session
from ..types.session_chat_response import ChunkChatResponse, SessionChatResponse
from ..types.session_delete_response import SessionDeleteResponse
from ..types.session_render_response import SessionRenderResponse

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent: Optional[str] | Omit = omit,
        agents: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_create_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        user: Optional[str] | Omit = omit,
        users: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sessions",
            body=maybe_transform(
                {
                    "agent": agent,
                    "agents": agents,
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def update(
        self,
        session_id: str,
        *,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_update_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Patch Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            f"/sessions/{session_id}",
            body=maybe_transform(
                {
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: Dict[str, object] | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOffsetPagination[Session]:
        """
        List Sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/sessions",
            page=SyncOffsetPagination[Session],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=Session,
        )

    def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDeleteResponse:
        """
        Delete Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionDeleteResponse,
        )

    def chat(
        self,
        session_id: str,
        *,
        messages: Iterable[session_chat_params.Message],
        connection_pool: object | Omit = omit,
        agent: Optional[str] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        length_penalty: Optional[float] | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        model: Optional[str] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        recall: bool | Omit = omit,
        recall_tools: bool | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        response_format: Optional[session_chat_params.ResponseFormat] | Omit = omit,
        save: bool | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[session_chat_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[session_chat_params.Tool]] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        x_custom_api_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[SessionChatResponse, Stream[ChunkChatResponse]]:
        """
        Initiates a chat session.

        Routes to different implementations based on feature flags:

        - If auto_run_tools_chat feature flag is enabled, uses the new auto-tools
          implementation
        - Otherwise, uses the legacy implementation

        Parameters: developer (Developer): The developer associated with the chat
        session. session_id (UUID): The unique identifier of the chat session.
        chat_input (ChatInput): The chat input data. background_tasks (BackgroundTasks):
        The background tasks to run. x_custom_api_key (Optional[str]): The custom API
        key. mock_response (Optional[str]): Mock response for testing. connection_pool:
        Connection pool for testing purposes.

        Returns: ChatResponse or StreamingResponse: The chat response or streaming
        response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"X-Custom-Api-Key": x_custom_api_key}), **(extra_headers or {})}

        # If streaming is requested, return a Stream[ChunkChatResponse]
        if stream is True:
            extra_headers = {**extra_headers, "Accept": "text/event-stream"}
            return self._post(
                f"/sessions/{session_id}/chat",
                body=maybe_transform(
                    {
                        "messages": messages,
                        "agent": agent,
                        "auto_run_tools": auto_run_tools,
                        "frequency_penalty": frequency_penalty,
                        "length_penalty": length_penalty,
                        "logit_bias": logit_bias,
                        "max_tokens": max_tokens,
                        "metadata": metadata,
                        "min_p": min_p,
                        "model": model,
                        "presence_penalty": presence_penalty,
                        "recall": recall,
                        "recall_tools": recall_tools,
                        "repetition_penalty": repetition_penalty,
                        "response_format": response_format,
                        "save": save,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_p": top_p,
                    },
                    session_chat_params.SessionChatParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"connection_pool": connection_pool}, session_chat_params.SessionChatParams),
                ),
                cast_to=ChunkChatResponse,
                stream=True,
                stream_cls=Stream[ChunkChatResponse],
            )

        # For non-streaming, return the regular response
        return cast(
            SessionChatResponse,
            self._post(
                f"/sessions/{session_id}/chat",
                body=maybe_transform(
                    {
                        "messages": messages,
                        "agent": agent,
                        "auto_run_tools": auto_run_tools,
                        "frequency_penalty": frequency_penalty,
                        "length_penalty": length_penalty,
                        "logit_bias": logit_bias,
                        "max_tokens": max_tokens,
                        "metadata": metadata,
                        "min_p": min_p,
                        "model": model,
                        "presence_penalty": presence_penalty,
                        "recall": recall,
                        "recall_tools": recall_tools,
                        "repetition_penalty": repetition_penalty,
                        "response_format": response_format,
                        "save": save,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_p": top_p,
                    },
                    session_chat_params.SessionChatParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"connection_pool": connection_pool}, session_chat_params.SessionChatParams),
                ),
                cast_to=cast(
                    Any, SessionChatResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def create_or_update(
        self,
        session_id: str,
        *,
        agent: Optional[str] | Omit = omit,
        agents: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_create_or_update_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        user: Optional[str] | Omit = omit,
        users: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create Or Update Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/sessions/{session_id}",
            body=maybe_transform(
                {
                    "agent": agent,
                    "agents": agents,
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_or_update_params.SessionCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def get(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Get Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def history(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> History:
        """
        Get Session History

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/sessions/{session_id}/history",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=History,
        )

    def render(
        self,
        session_id: str,
        *,
        messages: Iterable[session_render_params.Message],
        agent: Optional[str] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        length_penalty: Optional[float] | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        model: Optional[str] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        recall: bool | Omit = omit,
        recall_tools: bool | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        response_format: Optional[session_render_params.ResponseFormat] | Omit = omit,
        save: bool | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[session_render_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[session_render_params.Tool]] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRenderResponse:
        """
        Renders a chat input.

        Routes to different implementations based on feature flags:

        - If auto_run_tools_chat feature flag is enabled, uses the new auto-tools
          implementation
        - Otherwise, uses the legacy implementation

        Parameters: developer (Developer): The developer associated with the chat
        session. session_id (UUID): The unique identifier of the chat session.
        chat_input (ChatInput): The chat input data.

        Returns: RenderResponse: The rendered chat input.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/sessions/{session_id}/render",
            body=maybe_transform(
                {
                    "messages": messages,
                    "agent": agent,
                    "auto_run_tools": auto_run_tools,
                    "frequency_penalty": frequency_penalty,
                    "length_penalty": length_penalty,
                    "logit_bias": logit_bias,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "min_p": min_p,
                    "model": model,
                    "presence_penalty": presence_penalty,
                    "recall": recall,
                    "recall_tools": recall_tools,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "save": save,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                session_render_params.SessionRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRenderResponse,
        )

    def reset(
        self,
        session_id: str,
        *,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_reset_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._put(
            f"/sessions/{session_id}",
            body=maybe_transform(
                {
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                },
                session_reset_params.SessionResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent: Optional[str] | Omit = omit,
        agents: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_create_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        user: Optional[str] | Omit = omit,
        users: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sessions",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "agents": agents,
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def update(
        self,
        session_id: str,
        *,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_update_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Patch Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            f"/sessions/{session_id}",
            body=await async_maybe_transform(
                {
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | Omit = omit,
        limit: int | Omit = omit,
        metadata_filter: Dict[str, object] | Omit = omit,
        offset: int | Omit = omit,
        sort_by: Literal["created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Session, AsyncOffsetPagination[Session]]:
        """
        List Sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/sessions",
            page=AsyncOffsetPagination[Session],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "metadata_filter": metadata_filter,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            model=Session,
        )

    async def delete(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDeleteResponse:
        """
        Delete Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionDeleteResponse,
        )

    async def chat(
        self,
        session_id: str,
        *,
        messages: Iterable[session_chat_params.Message],
        connection_pool: object | Omit = omit,
        agent: Optional[str] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        length_penalty: Optional[float] | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        model: Optional[str] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        recall: bool | Omit = omit,
        recall_tools: bool | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        response_format: Optional[session_chat_params.ResponseFormat] | Omit = omit,
        save: bool | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[session_chat_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[session_chat_params.Tool]] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        x_custom_api_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[SessionChatResponse, AsyncStream[ChunkChatResponse]]:
        """
        Initiates a chat session.

        Routes to different implementations based on feature flags:

        - If auto_run_tools_chat feature flag is enabled, uses the new auto-tools
          implementation
        - Otherwise, uses the legacy implementation

        Parameters: developer (Developer): The developer associated with the chat
        session. session_id (UUID): The unique identifier of the chat session.
        chat_input (ChatInput): The chat input data. background_tasks (BackgroundTasks):
        The background tasks to run. x_custom_api_key (Optional[str]): The custom API
        key. mock_response (Optional[str]): Mock response for testing. connection_pool:
        Connection pool for testing purposes.

        Returns: ChatResponse or StreamingResponse: The chat response or streaming
        response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"X-Custom-Api-Key": x_custom_api_key}), **(extra_headers or {})}

        # If streaming is requested, return an AsyncStream[ChunkChatResponse]
        if stream is True:
            extra_headers = {**extra_headers, "Accept": "text/event-stream"}
            body = await async_maybe_transform(
                {
                    "messages": messages,
                    "agent": agent,
                    "auto_run_tools": auto_run_tools,
                    "frequency_penalty": frequency_penalty,
                    "length_penalty": length_penalty,
                    "logit_bias": logit_bias,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "min_p": min_p,
                    "model": model,
                    "presence_penalty": presence_penalty,
                    "recall": recall,
                    "recall_tools": recall_tools,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "save": save,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                session_chat_params.SessionChatParams,
            )
            query = await async_maybe_transform(
                {"connection_pool": connection_pool}, session_chat_params.SessionChatParams
            )
            return await self._post(  # Keep the await, but ensure it returns an AsyncStream
                f"/sessions/{session_id}/chat",
                body=body,
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=query,
                ),
                cast_to=ChunkChatResponse,
                stream=True,
                stream_cls=AsyncStream[ChunkChatResponse],
            )

        # For non-streaming, return the regular response
        return cast(
            SessionChatResponse,
            await self._post(
                f"/sessions/{session_id}/chat",
                body=await async_maybe_transform(
                    {
                        "messages": messages,
                        "agent": agent,
                        "auto_run_tools": auto_run_tools,
                        "frequency_penalty": frequency_penalty,
                        "length_penalty": length_penalty,
                        "logit_bias": logit_bias,
                        "max_tokens": max_tokens,
                        "metadata": metadata,
                        "min_p": min_p,
                        "model": model,
                        "presence_penalty": presence_penalty,
                        "recall": recall,
                        "recall_tools": recall_tools,
                        "repetition_penalty": repetition_penalty,
                        "response_format": response_format,
                        "save": save,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_p": top_p,
                    },
                    session_chat_params.SessionChatParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"connection_pool": connection_pool}, session_chat_params.SessionChatParams
                    ),
                ),
                cast_to=cast(
                    Any, SessionChatResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def create_or_update(
        self,
        session_id: str,
        *,
        agent: Optional[str] | Omit = omit,
        agents: Optional[SequenceNotStr[str]] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_create_or_update_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        user: Optional[str] | Omit = omit,
        users: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create Or Update Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/sessions/{session_id}",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "agents": agents,
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_or_update_params.SessionCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def get(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Get Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/sessions/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )

    async def history(
        self,
        session_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> History:
        """
        Get Session History

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/sessions/{session_id}/history",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=History,
        )

    async def render(
        self,
        session_id: str,
        *,
        messages: Iterable[session_render_params.Message],
        agent: Optional[str] | Omit = omit,
        auto_run_tools: bool | Omit = omit,
        frequency_penalty: Optional[float] | Omit = omit,
        length_penalty: Optional[float] | Omit = omit,
        logit_bias: Optional[Dict[str, float]] | Omit = omit,
        max_tokens: Optional[int] | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        min_p: Optional[float] | Omit = omit,
        model: Optional[str] | Omit = omit,
        presence_penalty: Optional[float] | Omit = omit,
        recall: bool | Omit = omit,
        recall_tools: bool | Omit = omit,
        repetition_penalty: Optional[float] | Omit = omit,
        response_format: Optional[session_render_params.ResponseFormat] | Omit = omit,
        save: bool | Omit = omit,
        seed: Optional[int] | Omit = omit,
        stop: SequenceNotStr[str] | Omit = omit,
        stream: bool | Omit = omit,
        temperature: Optional[float] | Omit = omit,
        tool_choice: Optional[session_render_params.ToolChoice] | Omit = omit,
        tools: Optional[Iterable[session_render_params.Tool]] | Omit = omit,
        top_p: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRenderResponse:
        """
        Renders a chat input.

        Routes to different implementations based on feature flags:

        - If auto_run_tools_chat feature flag is enabled, uses the new auto-tools
          implementation
        - Otherwise, uses the legacy implementation

        Parameters: developer (Developer): The developer associated with the chat
        session. session_id (UUID): The unique identifier of the chat session.
        chat_input (ChatInput): The chat input data.

        Returns: RenderResponse: The rendered chat input.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/sessions/{session_id}/render",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "agent": agent,
                    "auto_run_tools": auto_run_tools,
                    "frequency_penalty": frequency_penalty,
                    "length_penalty": length_penalty,
                    "logit_bias": logit_bias,
                    "max_tokens": max_tokens,
                    "metadata": metadata,
                    "min_p": min_p,
                    "model": model,
                    "presence_penalty": presence_penalty,
                    "recall": recall,
                    "recall_tools": recall_tools,
                    "repetition_penalty": repetition_penalty,
                    "response_format": response_format,
                    "save": save,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                session_render_params.SessionRenderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionRenderResponse,
        )

    async def reset(
        self,
        session_id: str,
        *,
        auto_run_tools: bool | Omit = omit,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | Omit = omit,
        forward_tool_calls: bool | Omit = omit,
        metadata: Optional[object] | Omit = omit,
        recall_options: Optional[session_reset_params.RecallOptions] | Omit = omit,
        render_templates: bool | Omit = omit,
        situation: Optional[str] | Omit = omit,
        system_template: Optional[str] | Omit = omit,
        token_budget: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._put(
            f"/sessions/{session_id}",
            body=await async_maybe_transform(
                {
                    "auto_run_tools": auto_run_tools,
                    "context_overflow": context_overflow,
                    "forward_tool_calls": forward_tool_calls,
                    "metadata": metadata,
                    "recall_options": recall_options,
                    "render_templates": render_templates,
                    "situation": situation,
                    "system_template": system_template,
                    "token_budget": token_budget,
                },
                session_reset_params.SessionResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Session,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.update = to_raw_response_wrapper(
            sessions.update,
        )
        self.list = to_raw_response_wrapper(
            sessions.list,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )
        self.chat = to_raw_response_wrapper(
            sessions.chat,
        )
        self.create_or_update = to_raw_response_wrapper(
            sessions.create_or_update,
        )
        self.get = to_raw_response_wrapper(
            sessions.get,
        )
        self.history = to_raw_response_wrapper(
            sessions.history,
        )
        self.render = to_raw_response_wrapper(
            sessions.render,
        )
        self.reset = to_raw_response_wrapper(
            sessions.reset,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.update = async_to_raw_response_wrapper(
            sessions.update,
        )
        self.list = async_to_raw_response_wrapper(
            sessions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )
        self.chat = async_to_raw_response_wrapper(
            sessions.chat,
        )
        self.create_or_update = async_to_raw_response_wrapper(
            sessions.create_or_update,
        )
        self.get = async_to_raw_response_wrapper(
            sessions.get,
        )
        self.history = async_to_raw_response_wrapper(
            sessions.history,
        )
        self.render = async_to_raw_response_wrapper(
            sessions.render,
        )
        self.reset = async_to_raw_response_wrapper(
            sessions.reset,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.update = to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = to_streamed_response_wrapper(
            sessions.list,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )
        self.chat = to_streamed_response_wrapper(
            sessions.chat,
        )
        self.create_or_update = to_streamed_response_wrapper(
            sessions.create_or_update,
        )
        self.get = to_streamed_response_wrapper(
            sessions.get,
        )
        self.history = to_streamed_response_wrapper(
            sessions.history,
        )
        self.render = to_streamed_response_wrapper(
            sessions.render,
        )
        self.reset = to_streamed_response_wrapper(
            sessions.reset,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            sessions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sessions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )
        self.chat = async_to_streamed_response_wrapper(
            sessions.chat,
        )
        self.create_or_update = async_to_streamed_response_wrapper(
            sessions.create_or_update,
        )
        self.get = async_to_streamed_response_wrapper(
            sessions.get,
        )
        self.history = async_to_streamed_response_wrapper(
            sessions.history,
        )
        self.render = async_to_streamed_response_wrapper(
            sessions.render,
        )
        self.reset = async_to_streamed_response_wrapper(
            sessions.reset,
        )

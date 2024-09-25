# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    session_chat_params,
    session_list_params,
    session_patch_params,
    session_create_params,
    session_update_params,
    session_create_or_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncOffsetPagination, AsyncOffsetPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.history import History
from ..types.session import Session
from ..types.message_param import MessageParam
from ..types.session_chat_response import SessionChatResponse
from ..types.shared.resource_created import ResourceCreated
from ..types.shared.resource_deleted import ResourceDeleted
from ..types.shared.resource_updated import ResourceUpdated

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        agents: Optional[List[str]] | NotGiven = NOT_GIVEN,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        users: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceCreated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceCreated,
        )

    def update(
        self,
        session_id: str,
        *,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceUpdated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceUpdated,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceDeleted:
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
            cast_to=ResourceDeleted,
        )

    def chat(
        self,
        session_id: str,
        *,
        messages: Iterable[MessageParam],
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        length_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_p: Optional[float] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        recall: bool | NotGiven = NOT_GIVEN,
        repetition_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[session_chat_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        save: bool | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[session_chat_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Iterable[session_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        x_custom_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionChatResponse:
        """
        Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"X-Custom-Api-Key": x_custom_api_key}), **(extra_headers or {})}
        return cast(
            SessionChatResponse,
            self._post(
                f"/sessions/{session_id}/chat",
                body=maybe_transform(
                    {
                        "messages": messages,
                        "agent": agent,
                        "frequency_penalty": frequency_penalty,
                        "length_penalty": length_penalty,
                        "logit_bias": logit_bias,
                        "max_tokens": max_tokens,
                        "min_p": min_p,
                        "model": model,
                        "presence_penalty": presence_penalty,
                        "recall": recall,
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
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        agents: Optional[List[str]] | NotGiven = NOT_GIVEN,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        users: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceUpdated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_or_update_params.SessionCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceUpdated,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def patch(
        self,
        session_id: str,
        *,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceUpdated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                },
                session_patch_params.SessionPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceUpdated,
        )


class AsyncSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        agents: Optional[List[str]] | NotGiven = NOT_GIVEN,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        users: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceCreated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceCreated,
        )

    async def update(
        self,
        session_id: str,
        *,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceUpdated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceUpdated,
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceDeleted:
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
            cast_to=ResourceDeleted,
        )

    async def chat(
        self,
        session_id: str,
        *,
        messages: Iterable[MessageParam],
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        length_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[Dict[str, float]] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_p: Optional[float] | NotGiven = NOT_GIVEN,
        model: Optional[str] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        recall: bool | NotGiven = NOT_GIVEN,
        repetition_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[session_chat_params.ResponseFormat] | NotGiven = NOT_GIVEN,
        save: bool | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[session_chat_params.ToolChoice] | NotGiven = NOT_GIVEN,
        tools: Iterable[session_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        x_custom_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionChatResponse:
        """
        Chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {**strip_not_given({"X-Custom-Api-Key": x_custom_api_key}), **(extra_headers or {})}
        return cast(
            SessionChatResponse,
            await self._post(
                f"/sessions/{session_id}/chat",
                body=await async_maybe_transform(
                    {
                        "messages": messages,
                        "agent": agent,
                        "frequency_penalty": frequency_penalty,
                        "length_penalty": length_penalty,
                        "logit_bias": logit_bias,
                        "max_tokens": max_tokens,
                        "min_p": min_p,
                        "model": model,
                        "presence_penalty": presence_penalty,
                        "recall": recall,
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
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        agent: Optional[str] | NotGiven = NOT_GIVEN,
        agents: Optional[List[str]] | NotGiven = NOT_GIVEN,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        users: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceUpdated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                    "user": user,
                    "users": users,
                },
                session_create_or_update_params.SessionCreateOrUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceUpdated,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def patch(
        self,
        session_id: str,
        *,
        context_overflow: Optional[Literal["truncate", "adaptive"]] | NotGiven = NOT_GIVEN,
        forward_tool_results: Optional[bool] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        render_templates: bool | NotGiven = NOT_GIVEN,
        situation: str | NotGiven = NOT_GIVEN,
        token_budget: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceUpdated:
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
                    "context_overflow": context_overflow,
                    "forward_tool_results": forward_tool_results,
                    "metadata": metadata,
                    "render_templates": render_templates,
                    "situation": situation,
                    "token_budget": token_budget,
                },
                session_patch_params.SessionPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceUpdated,
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
        self.patch = to_raw_response_wrapper(
            sessions.patch,
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
        self.patch = async_to_raw_response_wrapper(
            sessions.patch,
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
        self.patch = to_streamed_response_wrapper(
            sessions.patch,
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
        self.patch = async_to_streamed_response_wrapper(
            sessions.patch,
        )

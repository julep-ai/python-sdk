# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.executions import transition_list_params, transition_stream_params
from ...types.transition import Transition

__all__ = ["TransitionsResource", "AsyncTransitionsResource"]


class TransitionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TransitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return TransitionsResourceWithStreamingResponse(self)

    def list(
        self,
        execution_id: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPagination[Transition]:
        """
        List Execution Transitions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get_api_list(
            f"/executions/{execution_id}/transitions",
            page=SyncOffsetPagination[Transition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    transition_list_params.TransitionListParams,
                ),
            ),
            model=Transition,
        )

    def stream(
        self,
        execution_id: str,
        *,
        next_page_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream Transitions Events

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get(
            f"/executions/{execution_id}/transitions.stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_page_token": next_page_token}, transition_stream_params.TransitionStreamParams
                ),
            ),
            cast_to=object,
        )


class AsyncTransitionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return AsyncTransitionsResourceWithStreamingResponse(self)

    def list(
        self,
        execution_id: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Transition, AsyncOffsetPagination[Transition]]:
        """
        List Execution Transitions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get_api_list(
            f"/executions/{execution_id}/transitions",
            page=AsyncOffsetPagination[Transition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                    },
                    transition_list_params.TransitionListParams,
                ),
            ),
            model=Transition,
        )

    async def stream(
        self,
        execution_id: str,
        *,
        next_page_token: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stream Transitions Events

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not execution_id:
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._get(
            f"/executions/{execution_id}/transitions.stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"next_page_token": next_page_token}, transition_stream_params.TransitionStreamParams
                ),
            ),
            cast_to=object,
        )


class TransitionsResourceWithRawResponse:
    def __init__(self, transitions: TransitionsResource) -> None:
        self._transitions = transitions

        self.list = to_raw_response_wrapper(
            transitions.list,
        )
        self.stream = to_raw_response_wrapper(
            transitions.stream,
        )


class AsyncTransitionsResourceWithRawResponse:
    def __init__(self, transitions: AsyncTransitionsResource) -> None:
        self._transitions = transitions

        self.list = async_to_raw_response_wrapper(
            transitions.list,
        )
        self.stream = async_to_raw_response_wrapper(
            transitions.stream,
        )


class TransitionsResourceWithStreamingResponse:
    def __init__(self, transitions: TransitionsResource) -> None:
        self._transitions = transitions

        self.list = to_streamed_response_wrapper(
            transitions.list,
        )
        self.stream = to_streamed_response_wrapper(
            transitions.stream,
        )


class AsyncTransitionsResourceWithStreamingResponse:
    def __init__(self, transitions: AsyncTransitionsResource) -> None:
        self._transitions = transitions

        self.list = async_to_streamed_response_wrapper(
            transitions.list,
        )
        self.stream = async_to_streamed_response_wrapper(
            transitions.stream,
        )

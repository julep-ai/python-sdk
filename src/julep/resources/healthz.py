# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["HealthzResource", "AsyncHealthzResource"]


class HealthzResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HealthzResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return HealthzResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HealthzResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return HealthzResourceWithStreamingResponse(self)

    def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Check Health"""
        return self._get(
            "/healthz",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHealthzResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHealthzResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHealthzResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHealthzResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return AsyncHealthzResourceWithStreamingResponse(self)

    async def check(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Check Health"""
        return await self._get(
            "/healthz",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HealthzResourceWithRawResponse:
    def __init__(self, healthz: HealthzResource) -> None:
        self._healthz = healthz

        self.check = to_raw_response_wrapper(
            healthz.check,
        )


class AsyncHealthzResourceWithRawResponse:
    def __init__(self, healthz: AsyncHealthzResource) -> None:
        self._healthz = healthz

        self.check = async_to_raw_response_wrapper(
            healthz.check,
        )


class HealthzResourceWithStreamingResponse:
    def __init__(self, healthz: HealthzResource) -> None:
        self._healthz = healthz

        self.check = to_streamed_response_wrapper(
            healthz.check,
        )


class AsyncHealthzResourceWithStreamingResponse:
    def __init__(self, healthz: AsyncHealthzResource) -> None:
        self._healthz = healthz

        self.check = async_to_streamed_response_wrapper(
            healthz.check,
        )

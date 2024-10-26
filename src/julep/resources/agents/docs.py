# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.doc import Doc
from ...pagination import SyncOffsetPagination, AsyncOffsetPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.agents import doc_list_params, doc_create_params, doc_search_params
from ...types.shared.resource_created import ResourceCreated
from ...types.shared.resource_deleted import ResourceDeleted
from ...types.agents.doc_search_response import DocSearchResponse

__all__ = ["DocsResource", "AsyncDocsResource"]


class DocsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return DocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return DocsResourceWithStreamingResponse(self)

    def create(
        self,
        agent_id: str,
        *,
        content: Union[str, List[str]],
        title: str,
        embed_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceCreated:
        """
        Create Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/docs",
            body=maybe_transform(
                {
                    "content": content,
                    "title": title,
                    "embed_instruction": embed_instruction,
                    "metadata": metadata,
                },
                doc_create_params.DocCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceCreated,
        )

    def list(
        self,
        agent_id: str,
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
    ) -> SyncOffsetPagination[Doc]:
        """
        List Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/docs",
            page=SyncOffsetPagination[Doc],
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
                    doc_list_params.DocListParams,
                ),
            ),
            model=Doc,
        )

    def delete(
        self,
        doc_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceDeleted:
        """
        Delete Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return self._delete(
            f"/agents/{agent_id}/docs/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceDeleted,
        )

    @overload
    def search(
        self,
        agent_id: str,
        *,
        text: str,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def search(
        self,
        agent_id: str,
        *,
        vector: Iterable[float],
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def search(
        self,
        agent_id: str,
        *,
        text: str,
        vector: Iterable[float],
        alpha: float | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["text"], ["vector"], ["text", "vector"])
    def search(
        self,
        agent_id: str,
        *,
        text: str | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        vector: Iterable[float] | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        alpha: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._post(
            f"/agents/{agent_id}/search",
            body=maybe_transform(
                {
                    "text": text,
                    "lang": lang,
                    "limit": limit,
                    "metadata_filter": metadata_filter,
                    "vector": vector,
                    "confidence": confidence,
                    "alpha": alpha,
                },
                doc_search_params.DocSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocSearchResponse,
        )


class AsyncDocsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/julep-ai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDocsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/julep-ai/python-sdk#with_streaming_response
        """
        return AsyncDocsResourceWithStreamingResponse(self)

    async def create(
        self,
        agent_id: str,
        *,
        content: Union[str, List[str]],
        title: str,
        embed_instruction: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceCreated:
        """
        Create Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/docs",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "title": title,
                    "embed_instruction": embed_instruction,
                    "metadata": metadata,
                },
                doc_create_params.DocCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceCreated,
        )

    def list(
        self,
        agent_id: str,
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
    ) -> AsyncPaginator[Doc, AsyncOffsetPagination[Doc]]:
        """
        List Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get_api_list(
            f"/agents/{agent_id}/docs",
            page=AsyncOffsetPagination[Doc],
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
                    doc_list_params.DocListParams,
                ),
            ),
            model=Doc,
        )

    async def delete(
        self,
        doc_id: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResourceDeleted:
        """
        Delete Agent Doc

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not doc_id:
            raise ValueError(f"Expected a non-empty value for `doc_id` but received {doc_id!r}")
        return await self._delete(
            f"/agents/{agent_id}/docs/{doc_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResourceDeleted,
        )

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        text: str,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        vector: Iterable[float],
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def search(
        self,
        agent_id: str,
        *,
        text: str,
        vector: Iterable[float],
        alpha: float | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        """
        Search Agent Docs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["text"], ["vector"], ["text", "vector"])
    async def search(
        self,
        agent_id: str,
        *,
        text: str | NotGiven = NOT_GIVEN,
        lang: Literal["en-US"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        metadata_filter: Dict[str, Union[float, str, bool, None]] | NotGiven = NOT_GIVEN,
        vector: Iterable[float] | NotGiven = NOT_GIVEN,
        confidence: float | NotGiven = NOT_GIVEN,
        alpha: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocSearchResponse:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._post(
            f"/agents/{agent_id}/search",
            body=await async_maybe_transform(
                {
                    "text": text,
                    "lang": lang,
                    "limit": limit,
                    "metadata_filter": metadata_filter,
                    "vector": vector,
                    "confidence": confidence,
                    "alpha": alpha,
                },
                doc_search_params.DocSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocSearchResponse,
        )


class DocsResourceWithRawResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.create = to_raw_response_wrapper(
            docs.create,
        )
        self.list = to_raw_response_wrapper(
            docs.list,
        )
        self.delete = to_raw_response_wrapper(
            docs.delete,
        )
        self.search = to_raw_response_wrapper(
            docs.search,
        )


class AsyncDocsResourceWithRawResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.create = async_to_raw_response_wrapper(
            docs.create,
        )
        self.list = async_to_raw_response_wrapper(
            docs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            docs.delete,
        )
        self.search = async_to_raw_response_wrapper(
            docs.search,
        )


class DocsResourceWithStreamingResponse:
    def __init__(self, docs: DocsResource) -> None:
        self._docs = docs

        self.create = to_streamed_response_wrapper(
            docs.create,
        )
        self.list = to_streamed_response_wrapper(
            docs.list,
        )
        self.delete = to_streamed_response_wrapper(
            docs.delete,
        )
        self.search = to_streamed_response_wrapper(
            docs.search,
        )


class AsyncDocsResourceWithStreamingResponse:
    def __init__(self, docs: AsyncDocsResource) -> None:
        self._docs = docs

        self.create = async_to_streamed_response_wrapper(
            docs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            docs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            docs.delete,
        )
        self.search = async_to_streamed_response_wrapper(
            docs.search,
        )

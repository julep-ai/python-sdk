# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import Transition
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        transition = client.executions.transitions.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPagination[Transition], transition, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        transition = client.executions.transitions.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[Transition], transition, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.executions.transitions.with_raw_response.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transition = response.parse()
        assert_matches_type(SyncOffsetPagination[Transition], transition, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.executions.transitions.with_streaming_response.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transition = response.parse()
            assert_matches_type(SyncOffsetPagination[Transition], transition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.transitions.with_raw_response.list(
                execution_id="",
            )

    @parametrize
    def test_method_stream(self, client: Julep) -> None:
        transition = client.executions.transitions.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, transition, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Julep) -> None:
        transition = client.executions.transitions.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_page_token="next_page_token",
        )
        assert_matches_type(object, transition, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Julep) -> None:
        response = client.executions.transitions.with_raw_response.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transition = response.parse()
        assert_matches_type(object, transition, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Julep) -> None:
        with client.executions.transitions.with_streaming_response.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transition = response.parse()
            assert_matches_type(object, transition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.transitions.with_raw_response.stream(
                execution_id="",
            )


class TestAsyncTransitions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        transition = await async_client.executions.transitions.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPagination[Transition], transition, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        transition = await async_client.executions.transitions.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[Transition], transition, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.transitions.with_raw_response.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transition = await response.parse()
        assert_matches_type(AsyncOffsetPagination[Transition], transition, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.transitions.with_streaming_response.list(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transition = await response.parse()
            assert_matches_type(AsyncOffsetPagination[Transition], transition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.transitions.with_raw_response.list(
                execution_id="",
            )

    @parametrize
    async def test_method_stream(self, async_client: AsyncJulep) -> None:
        transition = await async_client.executions.transitions.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, transition, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncJulep) -> None:
        transition = await async_client.executions.transitions.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            next_page_token="next_page_token",
        )
        assert_matches_type(object, transition, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.transitions.with_raw_response.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transition = await response.parse()
        assert_matches_type(object, transition, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.transitions.with_streaming_response.stream(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transition = await response.parse()
            assert_matches_type(object, transition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.transitions.with_raw_response.stream(
                execution_id="",
            )

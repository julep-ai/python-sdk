# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import Execution
from tests.utils import assert_matches_type
from julep._streaming import Stream, AsyncStream

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        status = client.executions.status.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Execution, status, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.executions.status.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(Execution, status, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.executions.status.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(Execution, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.status.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_stream(self, client: Julep) -> None:
        status = client.executions.status.stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Stream[Execution], status, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Julep) -> None:
        response = client.executions.status.with_raw_response.stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is False
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(Stream[Execution], status, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Julep) -> None:
        with client.executions.status.with_streaming_response.stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(Stream[Execution], status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stream(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.status.with_raw_response.stream(
                "",
            )


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        status = await async_client.executions.status.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Execution, status, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.status.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(Execution, status, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.status.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(Execution, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.status.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_stream(self, async_client: AsyncJulep) -> None:
        status = await async_client.executions.status.stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncStream[Execution], status, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.status.with_raw_response.stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is False
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(AsyncStream[Execution], status, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.status.with_streaming_response.stream(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(AsyncStream[Execution], status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stream(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.status.with_raw_response.stream(
                "",
            )

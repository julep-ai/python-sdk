# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import Execution
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        execution = client.executions.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        execution = client.executions.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
            error="error",
            metadata={},
            output={},
            transition_count=0,
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.executions.with_raw_response.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.executions.with_streaming_response.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.executions.with_raw_response.create(
                task_id="",
                input={},
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        execution = client.executions.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPagination[Execution], execution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        execution = client.executions.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[Execution], execution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.executions.with_raw_response.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(SyncOffsetPagination[Execution], execution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.executions.with_streaming_response.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(SyncOffsetPagination[Execution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.executions.with_raw_response.list(
                task_id="",
            )

    @parametrize
    def test_method_change_status_overload_1(self, client: Julep) -> None:
        execution = client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_method_change_status_with_all_params_overload_1(self, client: Julep) -> None:
        execution = client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
            status="running",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_raw_response_change_status_overload_1(self, client: Julep) -> None:
        response = client.executions.with_raw_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_streaming_response_change_status_overload_1(self, client: Julep) -> None:
        with client.executions.with_streaming_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_change_status_overload_1(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.with_raw_response.change_status(
                execution_id="",
            )

    @parametrize
    def test_method_change_status_overload_2(self, client: Julep) -> None:
        execution = client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_method_change_status_with_all_params_overload_2(self, client: Julep) -> None:
        execution = client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
            status="cancelled",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_raw_response_change_status_overload_2(self, client: Julep) -> None:
        response = client.executions.with_raw_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_streaming_response_change_status_overload_2(self, client: Julep) -> None:
        with client.executions.with_streaming_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_change_status_overload_2(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.with_raw_response.change_status(
                execution_id="",
            )

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        execution = client.executions.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.executions.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.executions.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.executions.with_raw_response.get(
                "",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
            error="error",
            metadata={},
            output={},
            transition_count=0,
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.create(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.executions.with_raw_response.create(
                task_id="",
                input={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPagination[Execution], execution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[Execution], execution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(AsyncOffsetPagination[Execution], execution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.list(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(AsyncOffsetPagination[Execution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.executions.with_raw_response.list(
                task_id="",
            )

    @parametrize
    async def test_method_change_status_overload_1(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_method_change_status_with_all_params_overload_1(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={},
            status="running",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_raw_response_change_status_overload_1(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_streaming_response_change_status_overload_1(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_change_status_overload_1(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.with_raw_response.change_status(
                execution_id="",
            )

    @parametrize
    async def test_method_change_status_overload_2(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_method_change_status_with_all_params_overload_2(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="reason",
            status="cancelled",
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_raw_response_change_status_overload_2(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_streaming_response_change_status_overload_2(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.change_status(
            execution_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_change_status_overload_2(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.with_raw_response.change_status(
                execution_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        execution = await async_client.executions.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.executions.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.executions.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.executions.with_raw_response.get(
                "",
            )

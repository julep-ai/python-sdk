# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import Task
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.shared import ResourceCreated, ResourceUpdated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        task = client.tasks.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )
        assert_matches_type(ResourceCreated, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        task = client.tasks.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
            description="description",
            inherit_tools=True,
            input_schema={},
            metadata={},
            tools=[
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
            ],
        )
        assert_matches_type(ResourceCreated, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.tasks.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(ResourceCreated, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.tasks.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(ResourceCreated, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.tasks.with_raw_response.create(
                agent_id="",
                main=[{"evaluate": {"foo": "string"}}],
                name="name",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        task = client.tasks.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPagination[Task], task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        task = client.tasks.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[Task], task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.tasks.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(SyncOffsetPagination[Task], task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.tasks.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(SyncOffsetPagination[Task], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.tasks.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_create_or_update(self, client: Julep) -> None:
        task = client.tasks.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )
        assert_matches_type(ResourceUpdated, task, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Julep) -> None:
        task = client.tasks.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
            description="description",
            inherit_tools=True,
            input_schema={},
            metadata={},
            tools=[
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
            ],
        )
        assert_matches_type(ResourceUpdated, task, path=["response"])

    @parametrize
    def test_raw_response_create_or_update(self, client: Julep) -> None:
        response = client.tasks.with_raw_response.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(ResourceUpdated, task, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update(self, client: Julep) -> None:
        with client.tasks.with_streaming_response.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(ResourceUpdated, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_or_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.tasks.with_raw_response.create_or_update(
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
                main=[{"evaluate": {"foo": "string"}}],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.create_or_update(
                task_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                main=[{"evaluate": {"foo": "string"}}],
                name="name",
            )

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        task = client.tasks.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.tasks.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.tasks.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(Task, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.get(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        task = await async_client.tasks.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )
        assert_matches_type(ResourceCreated, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        task = await async_client.tasks.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
            description="description",
            inherit_tools=True,
            input_schema={},
            metadata={},
            tools=[
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
            ],
        )
        assert_matches_type(ResourceCreated, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.tasks.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(ResourceCreated, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.tasks.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(ResourceCreated, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.tasks.with_raw_response.create(
                agent_id="",
                main=[{"evaluate": {"foo": "string"}}],
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        task = await async_client.tasks.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPagination[Task], task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        task = await async_client.tasks.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[Task], task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.tasks.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(AsyncOffsetPagination[Task], task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.tasks.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(AsyncOffsetPagination[Task], task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.tasks.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncJulep) -> None:
        task = await async_client.tasks.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )
        assert_matches_type(ResourceUpdated, task, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncJulep) -> None:
        task = await async_client.tasks.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
            description="description",
            inherit_tools=True,
            input_schema={},
            metadata={},
            tools=[
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {"foo": "string"},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                    },
                    "description": "description",
                    "function": {
                        "description": "description",
                        "name": {},
                        "parameters": {},
                    },
                    "integration": {
                        "provider": "dummy",
                        "arguments": {},
                        "method": "method",
                        "setup": {},
                    },
                    "system": {
                        "call": "call",
                        "arguments": {},
                    },
                },
            ],
        )
        assert_matches_type(ResourceUpdated, task, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.tasks.with_raw_response.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(ResourceUpdated, task, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncJulep) -> None:
        async with async_client.tasks.with_streaming_response.create_or_update(
            task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            main=[{"evaluate": {"foo": "string"}}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(ResourceUpdated, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_or_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.tasks.with_raw_response.create_or_update(
                task_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
                main=[{"evaluate": {"foo": "string"}}],
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.create_or_update(
                task_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                main=[{"evaluate": {"foo": "string"}}],
                name="name",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        task = await async_client.tasks.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.tasks.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(Task, task, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.tasks.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(Task, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.get(
                "",
            )

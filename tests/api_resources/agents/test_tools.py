# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.agents import (
    ToolListResponse,
    ToolResetResponse,
    ToolCreateResponse,
    ToolUpdateResponse,
)
from julep.types.shared import ResourceDeleted

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        tool = client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        tool = client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
            api_call={
                "method": "GET",
                "url": "https://example.com",
                "content": "content",
                "cookies": {"foo": "string"},
                "data": {},
                "files": {},
                "follow_redirects": True,
                "headers": {"foo": "string"},
                "json": {},
                "params": "string",
                "schema": {},
                "timeout": 0,
            },
            bash_20241022={
                "name": "name",
                "type": "bash_20241022",
            },
            computer_20241022={
                "display_height_px": 400,
                "display_number": 1,
                "display_width_px": 600,
                "name": "name",
                "type": "computer_20241022",
            },
            description="description",
            function={
                "description": {},
                "name": {},
                "parameters": {},
            },
            integration={
                "arguments": {},
                "method": "method",
                "provider": "dummy",
                "setup": {},
            },
            system={
                "operation": "create",
                "resource": "agent",
                "arguments": {},
                "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "subresource": "tool",
            },
            text_editor_20241022={
                "name": "name",
                "type": "text_editor_20241022",
            },
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.agents.tools.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.agents.tools.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolCreateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.create(
                agent_id="",
                name="name",
                type="function",
            )

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        tool = client.agents.tools.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Julep) -> None:
        tool = client.agents.tools.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            api_call={
                "content": "content",
                "cookies": {"foo": "string"},
                "data": {},
                "files": {},
                "follow_redirects": True,
                "headers": {"foo": "string"},
                "json": {},
                "method": "GET",
                "params": "string",
                "schema": {},
                "timeout": 0,
                "url": "https://example.com",
            },
            bash_20241022={
                "name": "name",
                "type": "bash_20241022",
            },
            computer_20241022={
                "display_height_px": 400,
                "display_number": 1,
                "display_width_px": 600,
                "name": "name",
                "type": "computer_20241022",
            },
            description="description",
            function={
                "description": {},
                "name": {},
                "parameters": {},
            },
            integration={
                "arguments": {},
                "method": "method",
                "provider": "dummy",
                "setup": {},
            },
            name="name",
            system={
                "arguments": {},
                "operation": "create",
                "resource": "agent",
                "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "subresource": "tool",
            },
            text_editor_20241022={
                "name": "name",
                "type": "text_editor_20241022",
            },
            type="function",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.agents.tools.with_raw_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.agents.tools.with_streaming_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.update(
                tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.update(
                tool_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        tool = client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        tool = client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.agents.tools.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.agents.tools.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(SyncOffsetPagination[ToolListResponse], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        tool = client.agents.tools.delete(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, tool, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.agents.tools.with_raw_response.delete(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ResourceDeleted, tool, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.agents.tools.with_streaming_response.delete(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ResourceDeleted, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.delete(
                tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.delete(
                tool_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_reset(self, client: Julep) -> None:
        tool = client.agents.tools.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )
        assert_matches_type(ToolResetResponse, tool, path=["response"])

    @parametrize
    def test_method_reset_with_all_params(self, client: Julep) -> None:
        tool = client.agents.tools.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
            api_call={
                "method": "GET",
                "url": "https://example.com",
                "content": "content",
                "cookies": {"foo": "string"},
                "data": {},
                "files": {},
                "follow_redirects": True,
                "headers": {"foo": "string"},
                "json": {},
                "params": "string",
                "schema": {},
                "timeout": 0,
            },
            bash_20241022={
                "name": "name",
                "type": "bash_20241022",
            },
            computer_20241022={
                "display_height_px": 400,
                "display_number": 1,
                "display_width_px": 600,
                "name": "name",
                "type": "computer_20241022",
            },
            description="description",
            function={
                "description": {},
                "name": {},
                "parameters": {},
            },
            integration={
                "arguments": {},
                "method": "method",
                "provider": "dummy",
                "setup": {},
            },
            system={
                "operation": "create",
                "resource": "agent",
                "arguments": {},
                "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "subresource": "tool",
            },
            text_editor_20241022={
                "name": "name",
                "type": "text_editor_20241022",
            },
        )
        assert_matches_type(ToolResetResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: Julep) -> None:
        response = client.agents.tools.with_raw_response.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolResetResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: Julep) -> None:
        with client.agents.tools.with_streaming_response.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolResetResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.tools.with_raw_response.reset(
                tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
                name="name",
                type="function",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            client.agents.tools.with_raw_response.reset(
                tool_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="name",
                type="function",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
            api_call={
                "method": "GET",
                "url": "https://example.com",
                "content": "content",
                "cookies": {"foo": "string"},
                "data": {},
                "files": {},
                "follow_redirects": True,
                "headers": {"foo": "string"},
                "json": {},
                "params": "string",
                "schema": {},
                "timeout": 0,
            },
            bash_20241022={
                "name": "name",
                "type": "bash_20241022",
            },
            computer_20241022={
                "display_height_px": 400,
                "display_number": 1,
                "display_width_px": 600,
                "name": "name",
                "type": "computer_20241022",
            },
            description="description",
            function={
                "description": {},
                "name": {},
                "parameters": {},
            },
            integration={
                "arguments": {},
                "method": "method",
                "provider": "dummy",
                "setup": {},
            },
            system={
                "operation": "create",
                "resource": "agent",
                "arguments": {},
                "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "subresource": "tool",
            },
            text_editor_20241022={
                "name": "name",
                "type": "text_editor_20241022",
            },
        )
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.tools.with_raw_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolCreateResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.tools.with_streaming_response.create(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolCreateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.create(
                agent_id="",
                name="name",
                type="function",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            api_call={
                "content": "content",
                "cookies": {"foo": "string"},
                "data": {},
                "files": {},
                "follow_redirects": True,
                "headers": {"foo": "string"},
                "json": {},
                "method": "GET",
                "params": "string",
                "schema": {},
                "timeout": 0,
                "url": "https://example.com",
            },
            bash_20241022={
                "name": "name",
                "type": "bash_20241022",
            },
            computer_20241022={
                "display_height_px": 400,
                "display_number": 1,
                "display_width_px": 600,
                "name": "name",
                "type": "computer_20241022",
            },
            description="description",
            function={
                "description": {},
                "name": {},
                "parameters": {},
            },
            integration={
                "arguments": {},
                "method": "method",
                "provider": "dummy",
                "setup": {},
            },
            name="name",
            system={
                "arguments": {},
                "operation": "create",
                "resource": "agent",
                "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "subresource": "tool",
            },
            text_editor_20241022={
                "name": "name",
                "type": "text_editor_20241022",
            },
            type="function",
        )
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.tools.with_raw_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolUpdateResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.tools.with_streaming_response.update(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolUpdateResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.update(
                tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.update(
                tool_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.tools.with_raw_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.tools.with_streaming_response.list(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AsyncOffsetPagination[ToolListResponse], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.list(
                agent_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.delete(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, tool, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.tools.with_raw_response.delete(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ResourceDeleted, tool, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.tools.with_streaming_response.delete(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ResourceDeleted, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.delete(
                tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.delete(
                tool_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_reset(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )
        assert_matches_type(ToolResetResponse, tool, path=["response"])

    @parametrize
    async def test_method_reset_with_all_params(self, async_client: AsyncJulep) -> None:
        tool = await async_client.agents.tools.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
            api_call={
                "method": "GET",
                "url": "https://example.com",
                "content": "content",
                "cookies": {"foo": "string"},
                "data": {},
                "files": {},
                "follow_redirects": True,
                "headers": {"foo": "string"},
                "json": {},
                "params": "string",
                "schema": {},
                "timeout": 0,
            },
            bash_20241022={
                "name": "name",
                "type": "bash_20241022",
            },
            computer_20241022={
                "display_height_px": 400,
                "display_number": 1,
                "display_width_px": 600,
                "name": "name",
                "type": "computer_20241022",
            },
            description="description",
            function={
                "description": {},
                "name": {},
                "parameters": {},
            },
            integration={
                "arguments": {},
                "method": "method",
                "provider": "dummy",
                "setup": {},
            },
            system={
                "operation": "create",
                "resource": "agent",
                "arguments": {},
                "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "subresource": "tool",
            },
            text_editor_20241022={
                "name": "name",
                "type": "text_editor_20241022",
            },
        )
        assert_matches_type(ToolResetResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.tools.with_raw_response.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolResetResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.tools.with_streaming_response.reset(
            tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            type="function",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolResetResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.tools.with_raw_response.reset(
                tool_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                agent_id="",
                name="name",
                type="function",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_id` but received ''"):
            await async_client.agents.tools.with_raw_response.reset(
                tool_id="",
                agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="name",
                type="function",
            )

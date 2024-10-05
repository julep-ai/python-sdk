# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import (
    History,
    Session,
    SessionChatResponse,
)
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.shared import ResourceCreated, ResourceDeleted, ResourceUpdated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        session = client.sessions.create()
        assert_matches_type(ResourceCreated, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        session = client.sessions.create(
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agents=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
            user="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
        )
        assert_matches_type(ResourceCreated, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ResourceCreated, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ResourceCreated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        session = client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Julep) -> None:
        session = client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ResourceUpdated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.update(
                session_id="",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        session = client.sessions.list()
        assert_matches_type(SyncOffsetPagination[Session], session, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        session = client.sessions.list(
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[Session], session, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SyncOffsetPagination[Session], session, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SyncOffsetPagination[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        session = client.sessions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, session, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ResourceDeleted, session, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ResourceDeleted, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_chat(self, client: Julep) -> None:
        session = client.sessions.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(SessionChatResponse, session, path=["response"])

    @parametrize
    def test_method_chat_with_all_params(self, client: Julep) -> None:
        session = client.sessions.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "continue": True,
                    "name": "name",
                }
            ],
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency_penalty=-2,
            length_penalty=0,
            logit_bias={"foo": -100},
            max_tokens=1,
            min_p=0,
            model="model",
            presence_penalty=-2,
            recall=True,
            repetition_penalty=0,
            response_format={"type": "text"},
            save=True,
            seed=-1,
            stop=["string", "string", "string"],
            stream=True,
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                        "timeout": 0,
                    },
                    "description": "description",
                    "function": {
                        "description": {},
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
                        "operation": "create",
                        "resource": "agent",
                        "arguments": {},
                        "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "subresource": "tool",
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                        "timeout": 0,
                    },
                    "description": "description",
                    "function": {
                        "description": {},
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
                        "operation": "create",
                        "resource": "agent",
                        "arguments": {},
                        "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "subresource": "tool",
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                        "timeout": 0,
                    },
                    "description": "description",
                    "function": {
                        "description": {},
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
                        "operation": "create",
                        "resource": "agent",
                        "arguments": {},
                        "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "subresource": "tool",
                    },
                },
            ],
            top_p=0,
            x_custom_api_key="X-Custom-Api-Key",
        )
        assert_matches_type(SessionChatResponse, session, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionChatResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionChatResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_chat(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.chat(
                session_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

    @parametrize
    def test_method_create_or_update(self, client: Julep) -> None:
        session = client.sessions.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Julep) -> None:
        session = client.sessions.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agents=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
            user="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_raw_response_create_or_update(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ResourceUpdated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_or_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.create_or_update(
                session_id="",
            )

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        session = client.sessions.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_history(self, client: Julep) -> None:
        session = client.sessions.history(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(History, session, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.history(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(History, session, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.history(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(History, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_history(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.history(
                "",
            )

    @parametrize
    def test_method_patch(self, client: Julep) -> None:
        session = client.sessions.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_method_patch_with_all_params(self, client: Julep) -> None:
        session = client.sessions.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_raw_response_patch(self, client: Julep) -> None:
        response = client.sessions.with_raw_response.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    def test_streaming_response_patch(self, client: Julep) -> None:
        with client.sessions.with_streaming_response.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(ResourceUpdated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_patch(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.patch(
                session_id="",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.create()
        assert_matches_type(ResourceCreated, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.create(
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agents=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
            user="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
        )
        assert_matches_type(ResourceCreated, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ResourceCreated, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ResourceCreated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ResourceUpdated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.update(
                session_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.list()
        assert_matches_type(AsyncOffsetPagination[Session], session, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.list(
            direction="asc",
            limit=0,
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[Session], session, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AsyncOffsetPagination[Session], session, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AsyncOffsetPagination[Session], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, session, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ResourceDeleted, session, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ResourceDeleted, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_chat(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )
        assert_matches_type(SessionChatResponse, session, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "continue": True,
                    "name": "name",
                }
            ],
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            frequency_penalty=-2,
            length_penalty=0,
            logit_bias={"foo": -100},
            max_tokens=1,
            min_p=0,
            model="model",
            presence_penalty=-2,
            recall=True,
            repetition_penalty=0,
            response_format={"type": "text"},
            save=True,
            seed=-1,
            stop=["string", "string", "string"],
            stream=True,
            temperature=0,
            tool_choice="auto",
            tools=[
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                        "timeout": 0,
                    },
                    "description": "description",
                    "function": {
                        "description": {},
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
                        "operation": "create",
                        "resource": "agent",
                        "arguments": {},
                        "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "subresource": "tool",
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                        "timeout": 0,
                    },
                    "description": "description",
                    "function": {
                        "description": {},
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
                        "operation": "create",
                        "resource": "agent",
                        "arguments": {},
                        "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "subresource": "tool",
                    },
                },
                {
                    "name": "name",
                    "api_call": {
                        "method": "GET",
                        "url": "https://example.com",
                        "content": "content",
                        "cookies": {"foo": "string"},
                        "data": {},
                        "follow_redirects": True,
                        "headers": {"foo": "string"},
                        "json": {},
                        "params": "string",
                        "timeout": 0,
                    },
                    "description": "description",
                    "function": {
                        "description": {},
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
                        "operation": "create",
                        "resource": "agent",
                        "arguments": {},
                        "resource_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "subresource": "tool",
                    },
                },
            ],
            top_p=0,
            x_custom_api_key="X-Custom-Api-Key",
        )
        assert_matches_type(SessionChatResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionChatResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.chat(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionChatResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_chat(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.chat(
                session_id="",
                messages=[
                    {
                        "content": "string",
                        "role": "user",
                    }
                ],
            )

    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agent="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agents=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
            user="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ],
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.create_or_update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ResourceUpdated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_or_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.create_or_update(
                session_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_history(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.history(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(History, session, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.history(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(History, session, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.history(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(History, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_history(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.history(
                "",
            )

    @parametrize
    async def test_method_patch(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncJulep) -> None:
        session = await async_client.sessions.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_overflow="truncate",
            forward_tool_results=True,
            metadata={},
            render_templates=True,
            situation="situation",
            token_budget=0,
        )
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncJulep) -> None:
        response = await async_client.sessions.with_raw_response.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(ResourceUpdated, session, path=["response"])

    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncJulep) -> None:
        async with async_client.sessions.with_streaming_response.patch(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(ResourceUpdated, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_patch(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.patch(
                session_id="",
            )

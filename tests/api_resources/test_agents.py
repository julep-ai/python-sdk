# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import (
    Agent,
)
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.shared import ResourceDeleted

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        agent = client.agents.create(
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        agent = client.agents.create(
            name="x",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.agents.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.agents.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        agent = client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Julep) -> None:
        agent = client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.agents.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.agents.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        agent = client.agents.list()
        assert_matches_type(SyncOffsetPagination[Agent], agent, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        agent = client.agents.list(
            direction="asc",
            limit=0,
            metadata_filter={"foo": "bar"},
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[Agent], agent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(SyncOffsetPagination[Agent], agent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(SyncOffsetPagination[Agent], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        agent = client.agents.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, agent, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.agents.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(ResourceDeleted, agent, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.agents.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(ResourceDeleted, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_or_update(self, client: Julep) -> None:
        agent = client.agents.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Julep) -> None:
        agent = client.agents.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_raw_response_create_or_update(self, client: Julep) -> None:
        response = client.agents.with_raw_response.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update(self, client: Julep) -> None:
        with client.agents.with_streaming_response.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_or_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.create_or_update(
                agent_id="",
                name="x",
            )

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        agent = client.agents.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.agents.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.agents.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_reset(self, client: Julep) -> None:
        agent = client.agents.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_method_reset_with_all_params(self, client: Julep) -> None:
        agent = client.agents.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_raw_response_reset(self, client: Julep) -> None:
        response = client.agents.with_raw_response.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    def test_streaming_response_reset(self, client: Julep) -> None:
        with client.agents.with_streaming_response.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.reset(
                agent_id="",
                name="x",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.create(
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.create(
            name="x",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.with_raw_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.with_streaming_response.update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.list()
        assert_matches_type(AsyncOffsetPagination[Agent], agent, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.list(
            direction="asc",
            limit=0,
            metadata_filter={"foo": "bar"},
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[Agent], agent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AsyncOffsetPagination[Agent], agent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AsyncOffsetPagination[Agent], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, agent, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(ResourceDeleted, agent, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(ResourceDeleted, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.with_raw_response.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.with_streaming_response.create_or_update(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_or_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.create_or_update(
                agent_id="",
                name="x",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_reset(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_method_reset_with_all_params(self, async_client: AsyncJulep) -> None:
        agent = await async_client.agents.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            about="about",
            canonical_name="canonical_name",
            default_settings={},
            default_system_template="default_system_template",
            instructions="string",
            metadata={},
            model="model",
        )
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncJulep) -> None:
        response = await async_client.agents.with_raw_response.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(Agent, agent, path=["response"])

    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncJulep) -> None:
        async with async_client.agents.with_streaming_response.reset(
            agent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(Agent, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.reset(
                agent_id="",
                name="x",
            )

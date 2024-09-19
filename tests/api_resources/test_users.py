# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import (
    User,
)
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.shared import ResourceCreated, ResourceDeleted, ResourceUpdated

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        user = client.users.create()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        user = client.users.create(
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ResourceCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        user = client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Julep) -> None:
        user = client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.users.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.users.with_streaming_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ResourceUpdated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.update(
                user_id="",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        user = client.users.list()
        assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        user = client.users.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(SyncOffsetPagination[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        user = client.users.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, user, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.users.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ResourceDeleted, user, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.users.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ResourceDeleted, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_or_update(self, client: Julep) -> None:
        user = client.users.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_method_create_or_update_with_all_params(self, client: Julep) -> None:
        user = client.users.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_raw_response_create_or_update(self, client: Julep) -> None:
        response = client.users.with_raw_response.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    def test_streaming_response_create_or_update(self, client: Julep) -> None:
        with client.users.with_streaming_response.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ResourceCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_or_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.create_or_update(
                user_id="",
            )

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        user = client.users.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.users.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.users.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_patch(self, client: Julep) -> None:
        user = client.users.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    def test_method_patch_with_all_params(self, client: Julep) -> None:
        user = client.users.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    def test_raw_response_patch(self, client: Julep) -> None:
        response = client.users.with_raw_response.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    def test_streaming_response_patch(self, client: Julep) -> None:
        with client.users.with_streaming_response.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(ResourceUpdated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_patch(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.patch(
                user_id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create(
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ResourceCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ResourceUpdated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.update(
                user_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.list()
        assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.list(
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(AsyncOffsetPagination[User], user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, user, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ResourceDeleted, user, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ResourceDeleted, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_or_update(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_method_create_or_update_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_raw_response_create_or_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ResourceCreated, user, path=["response"])

    @parametrize
    async def test_streaming_response_create_or_update(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.create_or_update(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ResourceCreated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_or_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.create_or_update(
                user_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_patch(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncJulep) -> None:
        user = await async_client.users.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            about="about",
            metadata={},
            name="name",
        )
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.with_raw_response.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(ResourceUpdated, user, path=["response"])

    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncJulep) -> None:
        async with async_client.users.with_streaming_response.patch(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(ResourceUpdated, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_patch(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.patch(
                user_id="",
            )

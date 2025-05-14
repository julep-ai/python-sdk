# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import Secret, SecretListResponse
from tests.utils import assert_matches_type
from julep.types.shared import ResourceDeleted

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        secret = client.secrets.create(
            name="name",
            value="value",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        secret = client.secrets.create(
            name="name",
            value="value",
            description="description",
            metadata={},
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.secrets.with_raw_response.create(
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.secrets.with_streaming_response.create(
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Julep) -> None:
        secret = client.secrets.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Julep) -> None:
        secret = client.secrets.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
            description="description",
            metadata={},
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Julep) -> None:
        response = client.secrets.with_raw_response.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Julep) -> None:
        with client.secrets.with_streaming_response.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets.with_raw_response.update(
                secret_id="",
                name="name",
                value="value",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        secret = client.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        secret = client.secrets.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        secret = client.secrets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, secret, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.secrets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(ResourceDeleted, secret, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.secrets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(ResourceDeleted, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.secrets.with_raw_response.delete(
                "",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        secret = await async_client.secrets.create(
            name="name",
            value="value",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        secret = await async_client.secrets.create(
            name="name",
            value="value",
            description="description",
            metadata={},
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.secrets.with_raw_response.create(
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.secrets.with_streaming_response.create(
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncJulep) -> None:
        secret = await async_client.secrets.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJulep) -> None:
        secret = await async_client.secrets.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
            description="description",
            metadata={},
        )
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJulep) -> None:
        response = await async_client.secrets.with_raw_response.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(Secret, secret, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJulep) -> None:
        async with async_client.secrets.with_streaming_response.update(
            secret_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(Secret, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets.with_raw_response.update(
                secret_id="",
                name="name",
                value="value",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        secret = await async_client.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        secret = await async_client.secrets.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        secret = await async_client.secrets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, secret, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.secrets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(ResourceDeleted, secret, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.secrets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(ResourceDeleted, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.secrets.with_raw_response.delete(
                "",
            )

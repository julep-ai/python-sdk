# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import File
from tests.utils import assert_matches_type
from julep.types.shared import ResourceDeleted

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        file = client.files.create(
            content="content",
            name="recNPna{}ip}t",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        file = client.files.create(
            content="content",
            name="recNPna{}ip}t",
            description="description",
            mime_type="mime_type",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.files.with_raw_response.create(
            content="content",
            name="recNPna{}ip}t",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.files.with_streaming_response.create(
            content="content",
            name="recNPna{}ip}t",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        file = client.files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(ResourceDeleted, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(ResourceDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Julep) -> None:
        file = client.files.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Julep) -> None:
        response = client.files.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Julep) -> None:
        with client.files.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.get(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        file = await async_client.files.create(
            content="content",
            name="recNPna{}ip}t",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        file = await async_client.files.create(
            content="content",
            name="recNPna{}ip}t",
            description="description",
            mime_type="mime_type",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.files.with_raw_response.create(
            content="content",
            name="recNPna{}ip}t",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.files.with_streaming_response.create(
            content="content",
            name="recNPna{}ip}t",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        file = await async_client.files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(ResourceDeleted, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(ResourceDeleted, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncJulep) -> None:
        file = await async_client.files.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncJulep) -> None:
        response = await async_client.files.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncJulep) -> None:
        async with async_client.files.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.get(
                "",
            )

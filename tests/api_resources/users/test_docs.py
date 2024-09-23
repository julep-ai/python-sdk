# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from julep.types import Doc
from tests.utils import assert_matches_type
from julep.pagination import SyncOffsetPagination, AsyncOffsetPagination
from julep.types.users import DocSearchResponse
from julep.types.shared import ResourceCreated, ResourceDeleted

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Julep) -> None:
        doc = client.users.docs.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
        )
        assert_matches_type(ResourceCreated, doc, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Julep) -> None:
        doc = client.users.docs.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
            metadata={},
        )
        assert_matches_type(ResourceCreated, doc, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Julep) -> None:
        response = client.users.docs.with_raw_response.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(ResourceCreated, doc, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Julep) -> None:
        with client.users.docs.with_streaming_response.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(ResourceCreated, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.docs.with_raw_response.create(
                user_id="",
                content="string",
                title="title",
            )

    @parametrize
    def test_method_list(self, client: Julep) -> None:
        doc = client.users.docs.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPagination[Doc], doc, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Julep) -> None:
        doc = client.users.docs.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(SyncOffsetPagination[Doc], doc, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Julep) -> None:
        response = client.users.docs.with_raw_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(SyncOffsetPagination[Doc], doc, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Julep) -> None:
        with client.users.docs.with_streaming_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(SyncOffsetPagination[Doc], doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.docs.with_raw_response.list(
                user_id="",
            )

    @parametrize
    def test_method_delete(self, client: Julep) -> None:
        doc = client.users.docs.delete(
            doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, doc, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Julep) -> None:
        response = client.users.docs.with_raw_response.delete(
            doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(ResourceDeleted, doc, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Julep) -> None:
        with client.users.docs.with_streaming_response.delete(
            doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(ResourceDeleted, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.docs.with_raw_response.delete(
                doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.users.docs.with_raw_response.delete(
                doc_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_search_overload_1(self, client: Julep) -> None:
        doc = client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_method_search_with_all_params_overload_1(self, client: Julep) -> None:
        doc = client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            lang="en-US",
            limit=1,
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_raw_response_search_overload_1(self, client: Julep) -> None:
        response = client.users.docs.with_raw_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_streaming_response_search_overload_1(self, client: Julep) -> None:
        with client.users.docs.with_streaming_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_overload_1(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.docs.with_raw_response.search(
                user_id="",
                text="text",
            )

    @parametrize
    def test_method_search_overload_2(self, client: Julep) -> None:
        doc = client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_method_search_with_all_params_overload_2(self, client: Julep) -> None:
        doc = client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_raw_response_search_overload_2(self, client: Julep) -> None:
        response = client.users.docs.with_raw_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_streaming_response_search_overload_2(self, client: Julep) -> None:
        with client.users.docs.with_streaming_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_overload_2(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.docs.with_raw_response.search(
                user_id="",
                vector=[0, 0, 0],
            )

    @parametrize
    def test_method_search_overload_3(self, client: Julep) -> None:
        doc = client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_method_search_with_all_params_overload_3(self, client: Julep) -> None:
        doc = client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
            alpha=0,
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_raw_response_search_overload_3(self, client: Julep) -> None:
        response = client.users.docs.with_raw_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    def test_streaming_response_search_overload_3(self, client: Julep) -> None:
        with client.users.docs.with_streaming_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_overload_3(self, client: Julep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.docs.with_raw_response.search(
                user_id="",
                text="text",
                vector=[0, 0, 0],
            )


class TestAsyncDocs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
        )
        assert_matches_type(ResourceCreated, doc, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
            metadata={},
        )
        assert_matches_type(ResourceCreated, doc, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.docs.with_raw_response.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(ResourceCreated, doc, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJulep) -> None:
        async with async_client.users.docs.with_streaming_response.create(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            content="string",
            title="title",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(ResourceCreated, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.docs.with_raw_response.create(
                user_id="",
                content="string",
                title="title",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPagination[Doc], doc, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="asc",
            limit=0,
            metadata_filter="metadata_filter",
            offset=0,
            sort_by="created_at",
        )
        assert_matches_type(AsyncOffsetPagination[Doc], doc, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.docs.with_raw_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(AsyncOffsetPagination[Doc], doc, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJulep) -> None:
        async with async_client.users.docs.with_streaming_response.list(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(AsyncOffsetPagination[Doc], doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.docs.with_raw_response.list(
                user_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.delete(
            doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ResourceDeleted, doc, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.docs.with_raw_response.delete(
            doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(ResourceDeleted, doc, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJulep) -> None:
        async with async_client.users.docs.with_streaming_response.delete(
            doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(ResourceDeleted, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.docs.with_raw_response.delete(
                doc_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                user_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.users.docs.with_raw_response.delete(
                doc_id="",
                user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_search_overload_1(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_method_search_with_all_params_overload_1(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            lang="en-US",
            limit=1,
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_raw_response_search_overload_1(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.docs.with_raw_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_streaming_response_search_overload_1(self, async_client: AsyncJulep) -> None:
        async with async_client.users.docs.with_streaming_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_overload_1(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.docs.with_raw_response.search(
                user_id="",
                text="text",
            )

    @parametrize
    async def test_method_search_overload_2(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_method_search_with_all_params_overload_2(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_raw_response_search_overload_2(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.docs.with_raw_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_streaming_response_search_overload_2(self, async_client: AsyncJulep) -> None:
        async with async_client.users.docs.with_streaming_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_overload_2(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.docs.with_raw_response.search(
                user_id="",
                vector=[0, 0, 0],
            )

    @parametrize
    async def test_method_search_overload_3(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_method_search_with_all_params_overload_3(self, async_client: AsyncJulep) -> None:
        doc = await async_client.users.docs.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
            alpha=0,
            confidence=0,
            lang="en-US",
            limit=1,
        )
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_raw_response_search_overload_3(self, async_client: AsyncJulep) -> None:
        response = await async_client.users.docs.with_raw_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        doc = await response.parse()
        assert_matches_type(DocSearchResponse, doc, path=["response"])

    @parametrize
    async def test_streaming_response_search_overload_3(self, async_client: AsyncJulep) -> None:
        async with async_client.users.docs.with_streaming_response.search(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="text",
            vector=[0, 0, 0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            doc = await response.parse()
            assert_matches_type(DocSearchResponse, doc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_overload_3(self, async_client: AsyncJulep) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.docs.with_raw_response.search(
                user_id="",
                text="text",
                vector=[0, 0, 0],
            )

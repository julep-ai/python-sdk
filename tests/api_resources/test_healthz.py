# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from julep import Julep, AsyncJulep
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHealthz:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_check(self, client: Julep) -> None:
        healthz = client.healthz.check()
        assert_matches_type(object, healthz, path=["response"])

    @parametrize
    def test_raw_response_check(self, client: Julep) -> None:
        response = client.healthz.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthz = response.parse()
        assert_matches_type(object, healthz, path=["response"])

    @parametrize
    def test_streaming_response_check(self, client: Julep) -> None:
        with client.healthz.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthz = response.parse()
            assert_matches_type(object, healthz, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHealthz:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_check(self, async_client: AsyncJulep) -> None:
        healthz = await async_client.healthz.check()
        assert_matches_type(object, healthz, path=["response"])

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncJulep) -> None:
        response = await async_client.healthz.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        healthz = await response.parse()
        assert_matches_type(object, healthz, path=["response"])

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncJulep) -> None:
        async with async_client.healthz.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            healthz = await response.parse()
            assert_matches_type(object, healthz, path=["response"])

        assert cast(Any, response.is_closed) is True

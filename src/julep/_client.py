# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Union, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import docs, jobs, files, tasks, sessions
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import JulepError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.users import users
from .resources.agents import agents
from .resources.executions import executions

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Julep",
    "AsyncJulep",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "dev": "https://dev.julep.ai/api",
    "production": "https://api.julep.ai/api",
    "local_multi_tenant": "http://localhost/api",
    "local": "http://localhost:8080",
}


class Julep(SyncAPIClient):
    agents: agents.AgentsResource
    files: files.FilesResource
    sessions: sessions.SessionsResource
    users: users.UsersResource
    jobs: jobs.JobsResource
    docs: docs.DocsResource
    tasks: tasks.TasksResource
    executions: executions.ExecutionsResource
    with_raw_response: JulepWithRawResponse
    with_streaming_response: JulepWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["dev", "production", "local_multi_tenant", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production", "local_multi_tenant", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous julep client instance.

        This automatically infers the `api_key` argument from the `JULEP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("JULEP_API_KEY")
        if api_key is None:
            raise JulepError(
                "The api_key client option must be set either by passing api_key to the client or by setting the JULEP_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("JULEP_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `JULEP_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "dev"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.agents = agents.AgentsResource(self)
        self.files = files.FilesResource(self)
        self.sessions = sessions.SessionsResource(self)
        self.users = users.UsersResource(self)
        self.jobs = jobs.JobsResource(self)
        self.docs = docs.DocsResource(self)
        self.tasks = tasks.TasksResource(self)
        self.executions = executions.ExecutionsResource(self)
        self.with_raw_response = JulepWithRawResponse(self)
        self.with_streaming_response = JulepWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production", "local_multi_tenant", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncJulep(AsyncAPIClient):
    agents: agents.AsyncAgentsResource
    files: files.AsyncFilesResource
    sessions: sessions.AsyncSessionsResource
    users: users.AsyncUsersResource
    jobs: jobs.AsyncJobsResource
    docs: docs.AsyncDocsResource
    tasks: tasks.AsyncTasksResource
    executions: executions.AsyncExecutionsResource
    with_raw_response: AsyncJulepWithRawResponse
    with_streaming_response: AsyncJulepWithStreamedResponse

    # client options
    api_key: str

    _environment: Literal["dev", "production", "local_multi_tenant", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production", "local_multi_tenant", "local"] | NotGiven = NOT_GIVEN,
        base_url: str | httpx.URL | None | NotGiven = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async julep client instance.

        This automatically infers the `api_key` argument from the `JULEP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("JULEP_API_KEY")
        if api_key is None:
            raise JulepError(
                "The api_key client option must be set either by passing api_key to the client or by setting the JULEP_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("JULEP_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `JULEP_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "dev"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.agents = agents.AsyncAgentsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.sessions = sessions.AsyncSessionsResource(self)
        self.users = users.AsyncUsersResource(self)
        self.jobs = jobs.AsyncJobsResource(self)
        self.docs = docs.AsyncDocsResource(self)
        self.tasks = tasks.AsyncTasksResource(self)
        self.executions = executions.AsyncExecutionsResource(self)
        self.with_raw_response = AsyncJulepWithRawResponse(self)
        self.with_streaming_response = AsyncJulepWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(nested_format="dots", array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["dev", "production", "local_multi_tenant", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class JulepWithRawResponse:
    def __init__(self, client: Julep) -> None:
        self.agents = agents.AgentsResourceWithRawResponse(client.agents)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.sessions = sessions.SessionsResourceWithRawResponse(client.sessions)
        self.users = users.UsersResourceWithRawResponse(client.users)
        self.jobs = jobs.JobsResourceWithRawResponse(client.jobs)
        self.docs = docs.DocsResourceWithRawResponse(client.docs)
        self.tasks = tasks.TasksResourceWithRawResponse(client.tasks)
        self.executions = executions.ExecutionsResourceWithRawResponse(client.executions)


class AsyncJulepWithRawResponse:
    def __init__(self, client: AsyncJulep) -> None:
        self.agents = agents.AsyncAgentsResourceWithRawResponse(client.agents)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.sessions = sessions.AsyncSessionsResourceWithRawResponse(client.sessions)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)
        self.jobs = jobs.AsyncJobsResourceWithRawResponse(client.jobs)
        self.docs = docs.AsyncDocsResourceWithRawResponse(client.docs)
        self.tasks = tasks.AsyncTasksResourceWithRawResponse(client.tasks)
        self.executions = executions.AsyncExecutionsResourceWithRawResponse(client.executions)


class JulepWithStreamedResponse:
    def __init__(self, client: Julep) -> None:
        self.agents = agents.AgentsResourceWithStreamingResponse(client.agents)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.sessions = sessions.SessionsResourceWithStreamingResponse(client.sessions)
        self.users = users.UsersResourceWithStreamingResponse(client.users)
        self.jobs = jobs.JobsResourceWithStreamingResponse(client.jobs)
        self.docs = docs.DocsResourceWithStreamingResponse(client.docs)
        self.tasks = tasks.TasksResourceWithStreamingResponse(client.tasks)
        self.executions = executions.ExecutionsResourceWithStreamingResponse(client.executions)


class AsyncJulepWithStreamedResponse:
    def __init__(self, client: AsyncJulep) -> None:
        self.agents = agents.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.sessions = sessions.AsyncSessionsResourceWithStreamingResponse(client.sessions)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)
        self.jobs = jobs.AsyncJobsResourceWithStreamingResponse(client.jobs)
        self.docs = docs.AsyncDocsResourceWithStreamingResponse(client.docs)
        self.tasks = tasks.AsyncTasksResourceWithStreamingResponse(client.tasks)
        self.executions = executions.AsyncExecutionsResourceWithStreamingResponse(client.executions)


Client = Julep

AsyncClient = AsyncJulep

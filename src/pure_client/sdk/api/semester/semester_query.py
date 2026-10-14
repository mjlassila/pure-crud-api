from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.semester_list_result import SemesterListResult
from ...models.semester_query import SemesterQuery
from ...types import Response


def _get_kwargs(
    *,
    body: SemesterQuery,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/semesters/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | SemesterListResult | None:
    if response.status_code == 200:
        response_200 = SemesterListResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | SemesterListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SemesterQuery,
) -> Response[ProblemDetails | SemesterListResult]:
    """Query operation for semester

     Lists semesters in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (SemesterQuery): Create a query for semester

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | SemesterListResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SemesterQuery,
) -> ProblemDetails | SemesterListResult | None:
    """Query operation for semester

     Lists semesters in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (SemesterQuery): Create a query for semester

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | SemesterListResult
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SemesterQuery,
) -> Response[ProblemDetails | SemesterListResult]:
    """Query operation for semester

     Lists semesters in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (SemesterQuery): Create a query for semester

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | SemesterListResult]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SemesterQuery,
) -> ProblemDetails | SemesterListResult | None:
    """Query operation for semester

     Lists semesters in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (SemesterQuery): Create a query for semester

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | SemesterListResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

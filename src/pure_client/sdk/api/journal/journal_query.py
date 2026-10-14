from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.journal_list_result import JournalListResult
from ...models.journals_query import JournalsQuery
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: JournalsQuery,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/journals/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> JournalListResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = JournalListResult.from_dict(response.json())

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
) -> Response[JournalListResult | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JournalsQuery,
) -> Response[JournalListResult | ProblemDetails]:
    """Query operation for journals

     Lists journals in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (JournalsQuery): Create a query for journals

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JournalListResult | ProblemDetails]
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
    body: JournalsQuery,
) -> JournalListResult | ProblemDetails | None:
    """Query operation for journals

     Lists journals in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (JournalsQuery): Create a query for journals

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JournalListResult | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: JournalsQuery,
) -> Response[JournalListResult | ProblemDetails]:
    """Query operation for journals

     Lists journals in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (JournalsQuery): Create a query for journals

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JournalListResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: JournalsQuery,
) -> JournalListResult | ProblemDetails | None:
    """Query operation for journals

     Lists journals in the Pure instance that matches the provided query, similar to the GET version,
    instead of using parameters to alter the response, an JSON document is posted with the request. The
    JSON document contains fields for all the parameters available for the GET version, but also
    additional filtering options.

    Args:
        body (JournalsQuery): Create a query for journals

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JournalListResult | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

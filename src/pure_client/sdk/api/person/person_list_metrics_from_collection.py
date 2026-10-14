from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.metric_collection import MetricCollection
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    collection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/persons/{uuid}/metrics/{collection_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MetricCollection | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = MetricCollection.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MetricCollection | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MetricCollection | ProblemDetails]:
    """Lists metrics with collection id

     Lists metrics from a specific metrics collection that associated with a person.

    Args:
        uuid (UUID):
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetricCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        collection_id=collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> MetricCollection | ProblemDetails | None:
    """Lists metrics with collection id

     Lists metrics from a specific metrics collection that associated with a person.

    Args:
        uuid (UUID):
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetricCollection | ProblemDetails
    """

    return sync_detailed(
        uuid=uuid,
        collection_id=collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[MetricCollection | ProblemDetails]:
    """Lists metrics with collection id

     Lists metrics from a specific metrics collection that associated with a person.

    Args:
        uuid (UUID):
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetricCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        collection_id=collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> MetricCollection | ProblemDetails | None:
    """Lists metrics with collection id

     Lists metrics from a specific metrics collection that associated with a person.

    Args:
        uuid (UUID):
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetricCollection | ProblemDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            collection_id=collection_id,
            client=client,
        )
    ).parsed

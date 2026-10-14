from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disciplines_association_list_result import (
    DisciplinesAssociationListResult,
)
from ...models.disciplines_associations_query import DisciplinesAssociationsQuery
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    discipline_scheme: str,
    *,
    body: DisciplinesAssociationsQuery,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/awards/disciplines/{discipline_scheme}/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DisciplinesAssociationListResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = DisciplinesAssociationListResult.from_dict(response.json())

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
) -> Response[DisciplinesAssociationListResult | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
    body: DisciplinesAssociationsQuery,
) -> Response[DisciplinesAssociationListResult | ProblemDetails]:
    """Query operation for disciplines associated with awards

     Lists disciplines from the discipline scheme associated with awards in the Pure instance that
    matches the provided query.

    Args:
        discipline_scheme (str):
        body (DisciplinesAssociationsQuery): Create a query for discipline associations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DisciplinesAssociationListResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        discipline_scheme=discipline_scheme,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
    body: DisciplinesAssociationsQuery,
) -> DisciplinesAssociationListResult | ProblemDetails | None:
    """Query operation for disciplines associated with awards

     Lists disciplines from the discipline scheme associated with awards in the Pure instance that
    matches the provided query.

    Args:
        discipline_scheme (str):
        body (DisciplinesAssociationsQuery): Create a query for discipline associations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DisciplinesAssociationListResult | ProblemDetails
    """

    return sync_detailed(
        discipline_scheme=discipline_scheme,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
    body: DisciplinesAssociationsQuery,
) -> Response[DisciplinesAssociationListResult | ProblemDetails]:
    """Query operation for disciplines associated with awards

     Lists disciplines from the discipline scheme associated with awards in the Pure instance that
    matches the provided query.

    Args:
        discipline_scheme (str):
        body (DisciplinesAssociationsQuery): Create a query for discipline associations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DisciplinesAssociationListResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        discipline_scheme=discipline_scheme,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
    body: DisciplinesAssociationsQuery,
) -> DisciplinesAssociationListResult | ProblemDetails | None:
    """Query operation for disciplines associated with awards

     Lists disciplines from the discipline scheme associated with awards in the Pure instance that
    matches the provided query.

    Args:
        discipline_scheme (str):
        body (DisciplinesAssociationsQuery): Create a query for discipline associations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DisciplinesAssociationListResult | ProblemDetails
    """

    return (
        await asyncio_detailed(
            discipline_scheme=discipline_scheme,
            client=client,
            body=body,
        )
    ).parsed

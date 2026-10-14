from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disciplines_association import DisciplinesAssociation
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    discipline_scheme: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{uuid}/disciplines/{discipline_scheme}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DisciplinesAssociation | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = DisciplinesAssociation.from_dict(response.json())

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
) -> Response[DisciplinesAssociation | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DisciplinesAssociation | ProblemDetails]:
    """Get disciplines from the discipline scheme associated with the project

     Get disciplines from the discipline scheme associated with the project with specific UUID.

    Args:
        uuid (UUID):
        discipline_scheme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DisciplinesAssociation | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        discipline_scheme=discipline_scheme,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
) -> DisciplinesAssociation | ProblemDetails | None:
    """Get disciplines from the discipline scheme associated with the project

     Get disciplines from the discipline scheme associated with the project with specific UUID.

    Args:
        uuid (UUID):
        discipline_scheme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DisciplinesAssociation | ProblemDetails
    """

    return sync_detailed(
        uuid=uuid,
        discipline_scheme=discipline_scheme,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DisciplinesAssociation | ProblemDetails]:
    """Get disciplines from the discipline scheme associated with the project

     Get disciplines from the discipline scheme associated with the project with specific UUID.

    Args:
        uuid (UUID):
        discipline_scheme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DisciplinesAssociation | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        discipline_scheme=discipline_scheme,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
) -> DisciplinesAssociation | ProblemDetails | None:
    """Get disciplines from the discipline scheme associated with the project

     Get disciplines from the discipline scheme associated with the project with specific UUID.

    Args:
        uuid (UUID):
        discipline_scheme (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DisciplinesAssociation | ProblemDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            discipline_scheme=discipline_scheme,
            client=client,
        )
    ).parsed

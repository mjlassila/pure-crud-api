from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conflict_problem_details import ConflictProblemDetails
from ...models.keyword_group_configuration import KeywordGroupConfiguration
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    uuid: UUID,
    *,
    body: KeywordGroupConfiguration,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/keyword-group-configurations/{uuid}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = KeywordGroupConfiguration.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ConflictProblemDetails.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KeywordGroupConfiguration,
) -> Response[ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails]:
    """Update keyword group configuration

     Update keyword group configuration with specific UUID.

    Args:
        uuid (UUID):
        body (KeywordGroupConfiguration): A specification of the allowed behavior of a specified
            keyword group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KeywordGroupConfiguration,
) -> ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails | None:
    """Update keyword group configuration

     Update keyword group configuration with specific UUID.

    Args:
        uuid (UUID):
        body (KeywordGroupConfiguration): A specification of the allowed behavior of a specified
            keyword group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KeywordGroupConfiguration,
) -> Response[ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails]:
    """Update keyword group configuration

     Update keyword group configuration with specific UUID.

    Args:
        uuid (UUID):
        body (KeywordGroupConfiguration): A specification of the allowed behavior of a specified
            keyword group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: KeywordGroupConfiguration,
) -> ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails | None:
    """Update keyword group configuration

     Update keyword group configuration with specific UUID.

    Args:
        uuid (UUID):
        body (KeywordGroupConfiguration): A specification of the allowed behavior of a specified
            keyword group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConflictProblemDetails | KeywordGroupConfiguration | ProblemDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            body=body,
        )
    ).parsed

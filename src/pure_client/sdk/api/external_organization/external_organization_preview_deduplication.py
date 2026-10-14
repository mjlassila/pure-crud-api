from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_organization_list import ExternalOrganizationList
from ...models.external_organization_list_result import ExternalOrganizationListResult
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: ExternalOrganizationList,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/external-organizations/preview-deduplication",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExternalOrganizationListResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ExternalOrganizationListResult.from_dict(response.json())

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
) -> Response[ExternalOrganizationListResult | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExternalOrganizationList,
) -> Response[ExternalOrganizationListResult | ProblemDetails]:
    """Preview deduplication of external organizations

     Runs through a list external organizations and returns the deduplicated and merged organizations.
    The operation does not touch the Pure database

    Args:
        body (ExternalOrganizationList): List of organizations external to the institution.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalOrganizationListResult | ProblemDetails]
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
    body: ExternalOrganizationList,
) -> ExternalOrganizationListResult | ProblemDetails | None:
    """Preview deduplication of external organizations

     Runs through a list external organizations and returns the deduplicated and merged organizations.
    The operation does not touch the Pure database

    Args:
        body (ExternalOrganizationList): List of organizations external to the institution.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalOrganizationListResult | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExternalOrganizationList,
) -> Response[ExternalOrganizationListResult | ProblemDetails]:
    """Preview deduplication of external organizations

     Runs through a list external organizations and returns the deduplicated and merged organizations.
    The operation does not touch the Pure database

    Args:
        body (ExternalOrganizationList): List of organizations external to the institution.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalOrganizationListResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExternalOrganizationList,
) -> ExternalOrganizationListResult | ProblemDetails | None:
    """Preview deduplication of external organizations

     Runs through a list external organizations and returns the deduplicated and merged organizations.
    The operation does not touch the Pure database

    Args:
        body (ExternalOrganizationList): List of organizations external to the institution.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalOrganizationListResult | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

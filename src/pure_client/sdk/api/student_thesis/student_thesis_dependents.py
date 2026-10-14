from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_ref_list_result import ContentRefListResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    verbose: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["verbose"] = verbose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/student-theses/{uuid}/dependents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContentRefListResult | None:
    if response.status_code == 200:
        response_200 = ContentRefListResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContentRefListResult]:
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
    verbose: bool | Unset = UNSET,
) -> Response[ContentRefListResult]:
    """Lists all dependents to a student thesis

     Lists all dependents to a student thesis with the specified UUID. If the user does not have access
    to view all the dependent content, an authorization error will be thrown.

    Args:
        uuid (UUID):
        verbose (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentRefListResult]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        verbose=verbose,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    verbose: bool | Unset = UNSET,
) -> ContentRefListResult | None:
    """Lists all dependents to a student thesis

     Lists all dependents to a student thesis with the specified UUID. If the user does not have access
    to view all the dependent content, an authorization error will be thrown.

    Args:
        uuid (UUID):
        verbose (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentRefListResult
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        verbose=verbose,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    verbose: bool | Unset = UNSET,
) -> Response[ContentRefListResult]:
    """Lists all dependents to a student thesis

     Lists all dependents to a student thesis with the specified UUID. If the user does not have access
    to view all the dependent content, an authorization error will be thrown.

    Args:
        uuid (UUID):
        verbose (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentRefListResult]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        verbose=verbose,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    verbose: bool | Unset = UNSET,
) -> ContentRefListResult | None:
    """Lists all dependents to a student thesis

     Lists all dependents to a student thesis with the specified UUID. If the user does not have access
    to view all the dependent content, an authorization error will be thrown.

    Args:
        uuid (UUID):
        verbose (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentRefListResult
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            verbose=verbose,
        )
    ).parsed

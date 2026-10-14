from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignable_role import AssignableRole
from ...types import Response


def _get_kwargs(
    assignable_role_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/roles/{assignable_role_name}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssignableRole | None:
    if response.status_code == 200:
        response_200 = AssignableRole.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssignableRole]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assignable_role_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AssignableRole]:
    """Returns an assignable role

     Returns an assignable role if it is currently available

    Args:
        assignable_role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignableRole]
    """

    kwargs = _get_kwargs(
        assignable_role_name=assignable_role_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assignable_role_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> AssignableRole | None:
    """Returns an assignable role

     Returns an assignable role if it is currently available

    Args:
        assignable_role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignableRole
    """

    return sync_detailed(
        assignable_role_name=assignable_role_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    assignable_role_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AssignableRole]:
    """Returns an assignable role

     Returns an assignable role if it is currently available

    Args:
        assignable_role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssignableRole]
    """

    kwargs = _get_kwargs(
        assignable_role_name=assignable_role_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assignable_role_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> AssignableRole | None:
    """Returns an assignable role

     Returns an assignable role if it is currently available

    Args:
        assignable_role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssignableRole
    """

    return (
        await asyncio_detailed(
            assignable_role_name=assignable_role_name,
            client=client,
        )
    ).parsed

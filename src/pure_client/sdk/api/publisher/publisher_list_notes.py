from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.note_list_result import NoteListResult
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: UUID,
    *,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["size"] = size

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/publishers/{uuid}/notes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> NoteListResult | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = NoteListResult.from_dict(response.json())

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
) -> Response[NoteListResult | ProblemDetails]:
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
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[NoteListResult | ProblemDetails]:
    """Lists notes

     Lists notes associated with a publisher ordered by date (nulls last)

    Args:
        uuid (UUID):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NoteListResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        size=size,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> NoteListResult | ProblemDetails | None:
    """Lists notes

     Lists notes associated with a publisher ordered by date (nulls last)

    Args:
        uuid (UUID):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NoteListResult | ProblemDetails
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        size=size,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[NoteListResult | ProblemDetails]:
    """Lists notes

     Lists notes associated with a publisher ordered by date (nulls last)

    Args:
        uuid (UUID):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NoteListResult | ProblemDetails]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        size=size,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: UUID,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> NoteListResult | ProblemDetails | None:
    """Lists notes

     Lists notes associated with a publisher ordered by date (nulls last)

    Args:
        uuid (UUID):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NoteListResult | ProblemDetails
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            size=size,
            offset=offset,
        )
    ).parsed

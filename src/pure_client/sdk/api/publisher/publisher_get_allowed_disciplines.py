from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disciplines_discipline_list_result import DisciplinesDisciplineListResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    discipline_scheme: str,
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
        "url": f"/publishers/disciplines/{discipline_scheme}/allowed-disciplines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DisciplinesDisciplineListResult | None:
    if response.status_code == 200:
        response_200 = DisciplinesDisciplineListResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DisciplinesDisciplineListResult]:
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
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[DisciplinesDisciplineListResult]:
    """A list of allowed disciplines for a specific discipline scheme

     Get a list of a allowed disciplines for specific discipline scheme for publishers

    Args:
        discipline_scheme (str):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DisciplinesDisciplineListResult]
    """

    kwargs = _get_kwargs(
        discipline_scheme=discipline_scheme,
        size=size,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> DisciplinesDisciplineListResult | None:
    """A list of allowed disciplines for a specific discipline scheme

     Get a list of a allowed disciplines for specific discipline scheme for publishers

    Args:
        discipline_scheme (str):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DisciplinesDisciplineListResult
    """

    return sync_detailed(
        discipline_scheme=discipline_scheme,
        client=client,
        size=size,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[DisciplinesDisciplineListResult]:
    """A list of allowed disciplines for a specific discipline scheme

     Get a list of a allowed disciplines for specific discipline scheme for publishers

    Args:
        discipline_scheme (str):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DisciplinesDisciplineListResult]
    """

    kwargs = _get_kwargs(
        discipline_scheme=discipline_scheme,
        size=size,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    discipline_scheme: str,
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> DisciplinesDisciplineListResult | None:
    """A list of allowed disciplines for a specific discipline scheme

     Get a list of a allowed disciplines for specific discipline scheme for publishers

    Args:
        discipline_scheme (str):
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DisciplinesDisciplineListResult
    """

    return (
        await asyncio_detailed(
            discipline_scheme=discipline_scheme,
            client=client,
            size=size,
            offset=offset,
        )
    ).parsed

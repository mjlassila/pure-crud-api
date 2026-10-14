from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fingerprint_list_result import FingerprintListResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/fingerprints",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FingerprintListResult | None:
    if response.status_code == 200:
        response_200 = FingerprintListResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FingerprintListResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[FingerprintListResult]:
    """Lists all fingerprints

     Lists all fingerprints in the Pure instance. If you need to filter the fingerprints returned, see
    the POST version which supports additional filtering.

    Args:
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FingerprintListResult]
    """

    kwargs = _get_kwargs(
        size=size,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> FingerprintListResult | None:
    """Lists all fingerprints

     Lists all fingerprints in the Pure instance. If you need to filter the fingerprints returned, see
    the POST version which supports additional filtering.

    Args:
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FingerprintListResult
    """

    return sync_detailed(
        client=client,
        size=size,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> Response[FingerprintListResult]:
    """Lists all fingerprints

     Lists all fingerprints in the Pure instance. If you need to filter the fingerprints returned, see
    the POST version which supports additional filtering.

    Args:
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FingerprintListResult]
    """

    kwargs = _get_kwargs(
        size=size,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    size: int | Unset = 10,
    offset: int | Unset = 0,
) -> FingerprintListResult | None:
    """Lists all fingerprints

     Lists all fingerprints in the Pure instance. If you need to filter the fingerprints returned, see
    the POST version which supports additional filtering.

    Args:
        size (int | Unset):  Default: 10.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FingerprintListResult
    """

    return (
        await asyncio_detailed(
            client=client,
            size=size,
            offset=offset,
        )
    ).parsed

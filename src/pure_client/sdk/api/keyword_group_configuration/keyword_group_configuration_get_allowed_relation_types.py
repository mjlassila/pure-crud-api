from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_string_to_string_list_map_result import (
    APIStringToStringListMapResult,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/keyword-group-configurations/allowed-relation-types",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIStringToStringListMapResult | None:
    if response.status_code == 200:
        response_200 = APIStringToStringListMapResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIStringToStringListMapResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[APIStringToStringListMapResult]:
    """A map of allowed relation types

     The map key is the target system name and the value is the list of possible values to assign to
    relation type. Apart from the allowed values here, relation type can also be set to null (see
    description of relationType on KeywordGroupConfiguration).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIStringToStringListMapResult]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> APIStringToStringListMapResult | None:
    """A map of allowed relation types

     The map key is the target system name and the value is the list of possible values to assign to
    relation type. Apart from the allowed values here, relation type can also be set to null (see
    description of relationType on KeywordGroupConfiguration).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIStringToStringListMapResult
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[APIStringToStringListMapResult]:
    """A map of allowed relation types

     The map key is the target system name and the value is the list of possible values to assign to
    relation type. Apart from the allowed values here, relation type can also be set to null (see
    description of relationType on KeywordGroupConfiguration).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIStringToStringListMapResult]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> APIStringToStringListMapResult | None:
    """A map of allowed relation types

     The map key is the target system name and the value is the list of possible values to assign to
    relation type. Apart from the allowed values here, relation type can also be set to null (see
    description of relationType on KeywordGroupConfiguration).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIStringToStringListMapResult
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed

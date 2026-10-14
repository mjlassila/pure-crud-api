from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.classification_ref_list import ClassificationRefList
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    property_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/activities/allowed-custom-defined-field-values/{property_name}/classifications",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClassificationRefList | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ClassificationRefList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClassificationRefList | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    property_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ClassificationRefList | ProblemDetails]:
    """Get allowed classifications for the custom-defined field associated with the activity

     Get allowed classifications for the custom-defined field associated with the activity.

    Args:
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClassificationRefList | ProblemDetails]
    """

    kwargs = _get_kwargs(
        property_name=property_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    property_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> ClassificationRefList | ProblemDetails | None:
    """Get allowed classifications for the custom-defined field associated with the activity

     Get allowed classifications for the custom-defined field associated with the activity.

    Args:
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClassificationRefList | ProblemDetails
    """

    return sync_detailed(
        property_name=property_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    property_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ClassificationRefList | ProblemDetails]:
    """Get allowed classifications for the custom-defined field associated with the activity

     Get allowed classifications for the custom-defined field associated with the activity.

    Args:
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClassificationRefList | ProblemDetails]
    """

    kwargs = _get_kwargs(
        property_name=property_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    property_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> ClassificationRefList | ProblemDetails | None:
    """Get allowed classifications for the custom-defined field associated with the activity

     Get allowed classifications for the custom-defined field associated with the activity.

    Args:
        property_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClassificationRefList | ProblemDetails
    """

    return (
        await asyncio_detailed(
            property_name=property_name,
            client=client,
        )
    ).parsed

import aiohttp
import asyncio
import pydantic
from .exceptions import RequestedResourceError, NoNetworkConnection
from typing import Optional


class HTTPResponse(pydantic.BaseModel):
    status: int
    headers: dict
    body: str | dict
    cookies: dict


class BaseRequest():

    def __init__(self, timeout_seconds: int = 5) -> None:
        self.timeout = aiohttp.ClientTimeout(total=timeout_seconds)

    async def _get(self, url: str, headers:dict, json:bool = True) -> str | dict:
        async with aiohttp.ClientSession(timeout=self.timeout, headers=headers) as session:
            try:
                async with session.get(url) as response:
                    if json: return await response.json(content_type='text/html')
                    return await response.text()
            except aiohttp.client.ServerConnectionError as error:
                raise RequestedResourceError(
                    message=str(error),
                    status_code=500,
                )
            except asyncio.TimeoutError as error:
                raise RequestedResourceError(
                    message=f'Timeout error. The requested resource took a very long time to respond. Timeout = {self.timeout.total} sec.',
                    status_code=500,
                )
            except aiohttp.client.ClientConnectionError as error:
                raise NoNetworkConnection(
                    message=str(error),
                    status_code=500
                )

    async def _post(self, url: str, headers:dict, data:dict={}, json:bool = True) -> str | dict:
        async with aiohttp.ClientSession(timeout=self.timeout, headers=headers) as session:
            try:
                async with session.post(url, data=data) as response:
                    if json: return await response.json(content_type='text/html')
                    return await response.text()
            except aiohttp.client.ServerConnectionError as error:
                raise RequestedResourceError(
                    message=str(error),
                    status_code=500,
                )
            except asyncio.TimeoutError as error:
                raise RequestedResourceError(
                    message=f'Timeout error. The requested resource took a very long time to respond. Timeout = {self.timeout.total} sec.',
                    status_code=500,
                )
            except aiohttp.client.ClientConnectionError as error:
                raise NoNetworkConnection(
                    message=str(error),
                    status_code=500
                )

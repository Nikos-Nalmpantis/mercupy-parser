import asyncio
from typing import List, Tuple, Union, Optional
from time import time

import httpx
import validators
from httpx import Response


class Mercupy:
    def __init__(self, api_endpoint: str = "http://0.0.0.0:4000/parser"):
        self.api_endpoint = api_endpoint

    def parser(self,
               urls: Union[str, List[str]],
               headers: Optional[str] = None,
               content_type: Optional[str] = None) -> Tuple[Response]:
        """ Gathers responses from async requests to mercury parser """
        responses = asyncio.run(self._parser(urls, headers, content_type))
        return responses

    async def _parser(self,
                     urls: Union[str, List[str]],
                     headers: Optional[str] = None,
                     content_type: Optional[str] = None) -> Tuple[Response]:
        """ Convenience method to parse multiple urls """
        if not urls:
            raise AttributeError("urls not provided")

        if isinstance(urls, str):
            urls = [urls]

        start = time()
        responses = await asyncio.gather(*(self.mercury_parser(url, self.api_endpoint, headers, content_type) for url in urls))
        end = time()
        print(f"Inner main Time: {end - start:.2f} sec")

        return responses

    async def mercury_parser(self,
                             url: str,
                             api_endpoint: str,
                             headers: Optional[str] = None,
                             content_type: Optional[str] = None,
                             timeout: int = 20) -> Response:
        """ Async request to mercury parser """
        if not validators.url(url):
            raise AttributeError(f"Invalid url: {url}")

        params = {"url": url, "headers": headers, "contentType": content_type}
        params = {key: value for key, value in params.items() if value}
        async with httpx.AsyncClient() as client:
            r = await client.get(api_endpoint, params=params, timeout=timeout)

        return r

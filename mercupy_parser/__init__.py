import asyncio
import os
from functools import reduce
from time import perf_counter
from typing import List, Tuple, Union, Optional
from urllib.parse import urljoin as join

import httpx
import validators
from httpx import Response


def urljoin(*terms: str) -> str:
    return reduce(join, terms)


class Mercupy:
    def __init__(self, api_endpoint: Optional[str] = None, verbose: bool = False):
        if api_endpoint:
            api_endpoint = api_endpoint
        else:
            api_endpoint = os.environ.get("API_ENDPOINT", "http://0.0.0.0:4000/parser")
        self.api_endpoint = urljoin(api_endpoint, "parser")
        self.verbose = verbose

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
            raise AttributeError("URLS not provided")

        if isinstance(urls, str):
            urls = [urls]

        start = perf_counter()
        responses = await asyncio.gather(*(self.mercury_parser(url, headers, content_type) for url in urls))
        end = perf_counter()
        if self.verbose is True:
            print(f"Response time: {end - start:.2f} sec")

        return responses

    async def mercury_parser(self,
                             url: str,
                             headers: Optional[str] = None,
                             content_type: Optional[str] = None,
                             timeout: int = 20) -> Response:
        """ Async request to mercury parser """
        if not validators.url(url):
            raise AttributeError(f"Invalid url: {url}")

        params = {"url": url, "headers": headers, "contentType": content_type}
        params = {key: value for key, value in params.items() if value}
        async with httpx.AsyncClient() as client:
            r = await client.get(self.api_endpoint, params=params, timeout=timeout)

        return r

from liara.errors import APIError
from liara.types import Results

from typing import Optional
import requests


class API:

    BASE_URL = 'https://api.iran.liara.ir/v1/'

    def __init__(self, client=None):
        self.client = client
        self.headers: dict = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,fa;q=0.6',
            'Authorization': f'Bearer {self.client.api_token}',
            'Origin': 'https://console.liara.ir',
            'Referer': 'https://console.liara.ir/',
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            )
        }

    def execute(self, service: str, method: str, data: Optional[dict] = None):
        """
        Execute HTTP request to Liara API
        """
        path = self.BASE_URL + service
        with requests.request(method=method, url=path, headers=self.headers, data=data) as response:
            response_data = response.json()
            if response.status_code == requests.codes.ok:
                return Results(response_data)
            raise APIError(response_data, response.status_code)

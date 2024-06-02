import requests
from typing import Optional


from liara import errors


class Client:

    def __init__(
            self,
            name: str,
            token: Optional[str] = None,
            timeout: Optional[int] = 20,
            version: Optional[int] = 1
    ):
        self.token = token
        self.version = version
        self.timeout = timeout
        self.session = requests.session()

    @property
    def base_url(self) -> str:
        return f'https://api.iran.liara.ir/v{self.version}/'

    def execute(self, service: str, method: str, data: Optional[dict] = None) -> requests.Response:
        headers: dict = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,fa;q=0.6',
            'Authorization': f'Bearer {self.token}',
            'Origin': 'https://console.liara.ir',
            'Referer': 'https://console.liara.ir/',
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            )
        }
        result = self.session.request(
            method=method, url=self.base_url + service, headers=headers, timeout=self.timeout, json=data
        )
        if result.json().get('error') == 'Unauthorized.':
            raise errors.Unauthorized('Unauthorized account or session!')

        return result

    def get_services(self):
        return self.execute(service='projects', method='get')

    def get_my_account(self):
        return self.execute(service='me', method='get')

import aiohttp

class Client:

    def __init__(self, name: str, timeout: float = 20, version: int = 2):
        self.session = aiohttp.ClientSession(
            base_url=self.base_url
        )
        self.token = token
        self.timeout = timeout
        self.version = version

    @property
    def base_url(self) -> str:
        return 'https://api.iran.liara.ir/' + self.version

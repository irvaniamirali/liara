from typing import Optional
from os.path import exists

from liara.api import API
from liara.method import Methods


class Client(Methods):

    def __init__(self, name: str, api_token: Optional[str] = None, timeout: Optional[int] = 20):
        self.name = name
        self.api_token = api_token
        self.timeout = timeout
        self.api = API(client=self)

        if self.api_token is None:
            self.set_session(session_name=self.name)

        self.api = API(client=self)
        print(f'connect to  the Liara API with `{self.name}` session')

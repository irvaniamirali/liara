from typing import Optional
from os.path import exists
import json

from liara.http import API
from liara.methods import Methods


class Client(Methods):

    def __init__(
            self,
            name: Optional[str] = None,
            api_token: Optional[str] = None,
            timeout: Optional[int] = 20
    ):
        self.name = name
        self.api_token = api_token
        self.timeout = timeout
        self.suffix = ".session"
        self.api = API(client=self)

        if self.api_token is None:
            self.filename = self.name
            if not self.name.endswith(self.suffix):
                self.filename += self.suffix
                if exists(self.filename):
                    self.load(self.filename)
                else:
                    data = self.login(
                        email=input("Enter your email: "),
                        password=input("Enter your password (is displayed on the screen): ")
                    )
                    self.api_token = data.get("api_token")
                    self.dump(data)

        self.api = API(client=self)
        print(f"connect to the Liara API with `{self.name}` session")

    def load(self, file_name):
        with open(file_name, "r") as file:
            data = json.loads(file.read())
            self.api_token = data.get("api_token")

    def dump(self, session):
        with open(self.filename, "w") as file:
            json.dump(session, file, indent=4)

import liara


class Login:

    def login(self: "liara.Client", email: str, password: str):
        params: dict = {
            "email": email,
            "password": password
        }
        result = self.api.execute(service="login", method="post", data=params).json()
        self.api_token = result.get("api_token")

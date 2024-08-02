import liara


class Login:

    def login(self: "liara.Client", email: str, password: str):
        params = {
            "email": email,
            "password": password
        }
        return self.api.execute(service="login", method="POST", data=params)

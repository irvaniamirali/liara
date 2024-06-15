from os.path import exists
import json

import liara


class Session:

    def login(self: "liara.Client", email: str, password: str):
        params: dict = {
            "email": email,
            "password": password
        }
        result = self.api.execute(service="login", method="post", data=params).json()
        self.api_token = result.get("api_token")
        return result

    def set_session(self, session_name: str):
        session_filename = f"{session_name}.session"
        if not exists(session_filename):
            self.email = input("Enter your email: ")
            self.password = input("Enter your password: ")
            user_data = self.login(email=self.email, password=self.password)

            with open(session_filename, "w") as session_file:
                session_file.write(json.dumps(user_data))
        else:
            with open(session_filename, "r") as session_file:
                result = eval(session_file.read())
                self.api_token = result.get("api_token")

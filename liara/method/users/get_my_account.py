import liara


class GetMyAccount:

    def get_my_account(self: "liara.Client"):
        return self.api.execute(service="me", method="get")

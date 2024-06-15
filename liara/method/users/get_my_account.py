import liara


class GetMyAccount:

    def get_my_account(self: "liara.Client"):
        result = self.api.execute(service="me", method="get")
        return result

import liara


class GetMyAccount:

    async def get_my_account(self: "liara.Client"):
        result = await self.api.execute(service="me", method="get")
        return await result

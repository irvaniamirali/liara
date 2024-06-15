import liara


class DeleteApp:

    def delete_app(self: "liara.Client", name: str):
        """
        Delete a app
        """
        return self.api.execute(service="projects/" + name, method="delete")

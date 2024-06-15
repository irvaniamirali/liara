import liara


class DeleteProject:

    def delete_project(self: "liara.Client", name: str):
        """
        Delete a app
        """
        return self.api.execute(service="projects/" + name, method="delete")

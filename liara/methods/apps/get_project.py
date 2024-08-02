import liara


class GetProject:

    def get_project(self: "liara.Client", name: str):
        """
        Get details of a project
        :return:
        """
        path = "projects/" + name
        return self.api.execute(service=path, method="GET")

import liara


class GetProject:

    def get_project(self: "liara.Client", name: str):
        """
        Get details of a project
        :return:
        """
        return self.api.execute(service="projects/" + name, method="get")

import liara


class GetProjects:

    def get_projects_info(self: "liara.Client"):
        """
        Get all details of all projects that user owns
        """
        return self.api.execute(service="projects", method="get")

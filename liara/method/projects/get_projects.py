import liara


class GetProjects:

    def get_projects_info(self: "liara.Client"):
        return self.api.execute(service="projects", method="get")

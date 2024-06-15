from .create_app import CreateApp
from .get_projects import GetProjects
from .get_project import GetProject
from .delete_app import DeleteApp


class Apps(CreateApp, GetProjects, GetProject, DeleteApp):
    pass

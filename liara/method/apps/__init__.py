from .create_project import CreateProject
from .get_projects import GetProjects
from .get_project import GetProject
from .delete_project import DeleteProject


class Projects(CreateProject, GetProjects, GetProject, DeleteProject):
    pass

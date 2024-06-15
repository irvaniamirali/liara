from .users import Users
from .apps import Apps
from .session import StringSession


class Methods(Users, Apps, StringSession):
    pass

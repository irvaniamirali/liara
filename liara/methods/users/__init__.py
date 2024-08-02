from .get_my_account import GetMyAccount
from .login import Login


class Users(GetMyAccount, Login):
    pass

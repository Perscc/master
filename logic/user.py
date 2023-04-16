from db.models.db import Sqlite


class User:
    def __init__(self):
        self.db = Sqlite()

    # get_user 获取用户信息
    def get_user(self, name, role_type):
        return self.db.get_user(name, role_type)

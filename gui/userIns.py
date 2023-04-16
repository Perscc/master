import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from resource.ui.user import Ui_user_main


class user_instance(QMainWindow, Ui_user_main):
    def __init__(self, user, role_type, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.init_default_config(user, role_type)
        self.setWindowFlags(Qt.FramelessWindowHint)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from resource.ui.login import Ui_loginMain


# login_instance 登陆界面实例
class login_instance(QMainWindow, Ui_loginMain):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

import sys

from PyQt5.QtWidgets import *
from absl import app

from resource.ui.user import Ui_user_main


class user_instance(QMainWindow, Ui_user_main):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

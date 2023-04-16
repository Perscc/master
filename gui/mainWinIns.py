from PyQt5.QtWidgets import QMainWindow

from resource.ui.mainWin import Ui_MainWindow


class main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, user, role_type, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.init_default_config(user, role_type)
        self.setupUi(self)

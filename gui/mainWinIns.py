from PyQt5.QtWidgets import QMainWindow

from resource.ui.mainWin import Ui_MainWindow


class main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

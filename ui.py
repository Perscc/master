import sys
from PyQt5.QtWidgets import *

from gui.mainWinIns import main_window
from gui.userIns import user_instance

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # uIns = user_instance()
    # uIns.show()
    mainWin = main_window()
    mainWin.show()
    sys.exit(app.exec_())

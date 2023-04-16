import sys
from PyQt5.QtWidgets import *

from gui.loginIns import login_instance

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # uIns = user_instance()
    # uIns.show()
    loginIns = login_instance()
    loginIns.show()
    # mainWin = main_window()
    # mainWin.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QButtonGroup
from matplotlib.backends.backend_qt import MainWindow


class Ui_user_main(object):
    def setupUi(self, user_main):
        user_main.setObjectName("user_main")
        user_main.setEnabled(True)
        user_main.resize(900, 500)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.action_container = QtWidgets.QWidget(user_main)
        self.action_container.setEnabled(True)
        self.action_container.setObjectName("action_container")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.action_container)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 430, 800, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.operation = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.operation.setContentsMargins(0, 0, 0, 0)
        self.operation.setObjectName("operation")
        self.left_click = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_click.sizePolicy().hasHeightForWidth())
        self.left_click.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setBold(True)
        font.setWeight(75)
        self.left_click.setFont(font)
        self.left_click.setCheckable(True)
        self.left_click.setChecked(False)
        self.left_click.setAutoExclusive(True)
        self.left_click.setObjectName("left_click")
        self.operation.addWidget(self.left_click)
        self.right_click = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_click.sizePolicy().hasHeightForWidth())
        self.right_click.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setBold(True)
        font.setWeight(75)
        self.right_click.setFont(font)
        self.right_click.setObjectName("right_click")
        self.operation.addWidget(self.right_click)
        self.drag = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.drag.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setBold(True)
        font.setWeight(75)
        self.drag.setFont(font)
        self.drag.setChecked(False)
        self.drag.setObjectName("drag")
        self.operation.addWidget(self.drag)
        self.move_mouse = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setBold(True)
        font.setWeight(75)
        self.move_mouse.setFont(font)
        self.move_mouse.setObjectName("move_mouse")
        self.operation.addWidget(self.move_mouse)
        self.down = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setBold(True)
        font.setWeight(75)
        self.down.setFont(font)
        self.down.setObjectName("down")
        self.operation.addWidget(self.down)
        self.up = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setBold(True)
        font.setWeight(75)
        self.up.setFont(font)
        self.up.setObjectName("up")
        self.operation.addWidget(self.up)
        self.control_vol = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setBold(True)
        font.setWeight(75)
        self.control_vol.setFont(font)
        self.control_vol.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.control_vol.setObjectName("control_vol")
        self.operation.addWidget(self.control_vol)
        self.cap_img = QtWidgets.QLabel(self.action_container)
        self.cap_img.setGeometry(QtCore.QRect(138, -20, 700, 450))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cap_img.sizePolicy().hasHeightForWidth())
        self.cap_img.setSizePolicy(sizePolicy)
        self.cap_img.setText("")
        self.cap_img.setObjectName("cap_img")
        user_main.setCentralWidget(self.action_container)
        self.statusbar = QtWidgets.QStatusBar(user_main)
        self.statusbar.setObjectName("statusbar")
        user_main.setStatusBar(self.statusbar)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.left_click, 1)
        self.button_group.addButton(self.right_click, 2)
        self.button_group.addButton(self.drag, 3)
        self.button_group.addButton(self.move_mouse, 4)
        self.button_group.addButton(self.down, 5)
        self.button_group.addButton(self.up, 6)
        self.button_group.addButton(self.control_vol, 7)

        self.retranslateUi(user_main)
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.frame_rate = 50
        self.start()
        self.show()
        QtCore.QMetaObject.connectSlotsByName(user_main)

    def retranslateUi(self, user_main):
        _translate = QtCore.QCoreApplication.translate
        user_main.setWindowTitle(_translate("user_main", "MainWindow"))
        self.left_click.setText(_translate("user_main", "left_click"))
        self.right_click.setText(_translate("user_main", "right_click"))
        self.drag.setText(_translate("user_main", "drag"))
        self.move_mouse.setText(_translate("user_main", "move_mouse"))
        self.down.setText(_translate("user_main", "down"))
        self.up.setText(_translate("user_main", "up"))
        self.control_vol.setText(_translate("user_main", "control_vol"))

    def start(self):
        try:
            rate = int(1000.0 / self.frame_rate)
            self.timer.setTimerType(Qt.PreciseTimer)
            self.timer.timeout.connect(self.next_frame_slot)
            self.timer.start(rate)
        except:
            self.release_cap()

    def next_frame_slot(self):
        try:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.flip(frame, flipCode=1)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                img = img.scaled(640, 480, Qt.KeepAspectRatio)
                pix = QPixmap.fromImage(img)
                self.check_focus()
                self.cap_img.setPixmap(pix)
        except:
            self.release_cap()

    def release_cap(self):
        self.cap.release()
        self.timer.stop()
        cv2.destroyAllWindows()
        sys.exit(0)

    def check_focus(self):
        buttons = self.button_group.buttons()
        for btn in buttons:
            if btn.isChecked():
                print(btn.isChecked())

    def reset_focus(self):
        buttons = self.button_group.buttons()
        for btn in buttons:
            if btn.isChecked():
                btn.setChecked(False)

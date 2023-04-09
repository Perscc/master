import cv2
import numpy as np
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from gui.userIns import user_instance


class Video():
    def __init__(self, capture):
        self.capture = capture
        self.currentFrame = np.array([])

    def captureFrame(self):
        ret, readFrame = self.capture.read()
        return readFrame

    def captureNextFrame(self):
        ret, readFrame = self.capture.read()
        if (ret == True):
            self.currentFrame = cv2.cvtColor(readFrame, cv2.COLOR_BGR2RGB)

    def convertFrame(self):
        try:
            height, width = self.currentFrame.shape[:2]
            img = QImage(self.currentFrame, width, height, QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None


class win(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setGeometry(250, 80, 800, 600)  # 从屏幕(250，80)开始建立一个800*600的界面
        self.setWindowTitle('camera')
        self.video = Video(cv2.VideoCapture(0))
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
        self.videoFrame = QLabel('VideoCapture')
        self.videoFrame.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.videoFrame)
        self.ret, self.capturedFrame = self.video.capture.read()

    def play(self):
        try:
            self.video.captureNextFrame()
            self.videoFrame.setPixmap(self.video.convertFrame())
            self.videoFrame.setScaledContents(True)
        except TypeError:
            print('No Frame')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    uIns = user_instance()
    uIns.show()
    sys.exit(app.exec_())



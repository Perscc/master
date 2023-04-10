import time
import numpy as np
import autopy
import cv2
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL

def release_resource(cap):
    # 释放视频资源
    cap.release()
    cv2.destroyAllWindows()


# def get_volume_info():
#     devices = AudioUtilities.GetSpeakers()
#     interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#     volume = cast(interface, POINTER(IAudioEndpointVolume))
#     return volume


class Operation:
    """
    用于处理mediapipe捕获到手部信息后，根据用户定义的手势动作执行不同的鼠标操作
    """

    def __init__(self):
        self.wScr, self.hScr = autopy.screen.size()
        self.wCam = 1280  # 视频显示窗口的宽
        self.hCam = 720  # 视频显示窗口的高
        self.leftUpPoint = (100, 100)  # 鼠标移动的最左上坐标
        self.rightDownPoint = (1000, 500)  # 鼠标移动的最右下角坐标
        self.pTime = 0  # 上一帧的处理时间
        self.pLocx, self.pLocy = 0, 0  # 上一帧时的鼠标所在位置
        self.smooth = 5  # 自定义平滑系数，让鼠标移动平缓一些
        self.frame = 0  # 初始化累计帧数
        self.upframe = 0  # 上键处理的间隔帧率计数
        self.downframe = 0  # 下键处理的间隔帧率计数
        self.toggle = False  # 标志变量
        self.prev_state = [1, 1, 1, 1, 1]  # 初始化上一帧状态
        self.current_state = [1, 1, 1, 1, 1]  # 初始化当前正状态

    # get_video_capture 获取摄像头
    def get_video_capture(self, capType=0):
        """
        capType: 标识摄像头连接类型
        """
        cap = cv2.VideoCapture(capType)  # 0代表自己电脑的摄像头
        cap.set(3, self.wCam)
        cap.set(4, self.hCam)
        return cap

    # release_mouse 释放鼠标左键
    def release_mouse(self, fingers):
        """
        fingers: 手指状态
        """
        if fingers != [0, 0, 0, 0, 0] and self.toggle:
            autopy.mouse.toggle(None, False)
            self.toggle = False

    # move_mouse 移动鼠标
    def move_mouse(self, fingers, cLocx, cLocy):
        if fingers == [1, 1, 1, 0, 0] and sum(fingers) == 3:
            # 移动鼠标到指定位置
            autopy.mouse.move(cLocx, cLocy)
            self.pLocx, self.pLocy = cLocx, cLocy

    # left_click 鼠标左键
    def left_click(self, img, fingers, distance, x, y):
        """
        img: 摄像头获取的当前帧
        fingers： 当前帧手指状态
        distance：食指与中指的距离
        (x, y)：当前食指指尖的关键点
        """
        if distance < 43 and fingers == [0, 1, 1, 0, 0] and sum(fingers) == 2:
            # 在食指尖画个绿色的圆，表示点击鼠标
            cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
            # 左击鼠标
            autopy.mouse.click(button=autopy.mouse.Button.LEFT, delay=0)
            cv2.putText(img, "left_click", (150, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    def right_click(self, img, fingers, x, y):
        """
        img: 摄像头获取的当前帧
        fingers： 当前帧手指状态
        (x, y)：当前中指指尖的关键点
        """
        if fingers == [0, 1, 0, 0, 0] and sum(fingers) == 1:
            # 中指指尖画圆
            cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
            # 右击鼠标
            autopy.mouse.click(button=autopy.mouse.Button.RIGHT, delay=0)
            cv2.putText(img, "rigth_click", (150, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    def drag(self, img, fingers, cLocx, cLocy):
        if fingers == [0, 0, 0, 0, 0]:
            if not self.toggle:
                autopy.mouse.toggle(None, True)
                # x, y = pag.position()
                self.toggle = True
                # self.pLocx, self.pLocy = index_finger_range_xpoint, index_finger_range_ypoint
            else:
                autopy.mouse.move(cLocx, cLocy)
                self.pLocx, self.pLocy = cLocx, cLocy
                cv2.putText(img, "drag", (150, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    def press_up(self, img, fingers, active_window_process_name):
        if fingers == [1, 0, 0, 0, 0]:
            if self.upframe % 10 != 0 or self.upframe == 0:
                self.upframe += 1
            else:
                self.upframe = 0
                cv2.putText(img, "UP", (150, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
                if active_window_process_name == "cloudmusic.exe":
                    autopy.key.toggle(autopy.key.Code.LEFT_ARROW, True, [autopy.key.Modifier.CONTROL])
                    autopy.key.toggle(autopy.key.Code.LEFT_ARROW, False, [autopy.key.Modifier.CONTROL])
                else:
                    autopy.key.toggle(autopy.key.Code.UP_ARROW, True, [])
                    autopy.key.toggle(autopy.key.Code.UP_ARROW, False, [])

    def press_down(self, img, fingers, active_window_process_name):
        if fingers == [0, 1, 1, 1, 1]:
            # 10帧 处理一次 键盘操作 防止操作频率过快
            if self.downframe % 10 != 0 or self.downframe == 0:
                self.downframe += 1
            else:
                self.downframe = 0
                cv2.putText(img, "Down", (150, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
                if active_window_process_name == "cloudmusic.exe":
                    autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, True, [autopy.key.Modifier.CONTROL])
                    autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, False, [autopy.key.Modifier.CONTROL])
                else:
                    autopy.key.toggle(autopy.key.Code.DOWN_ARROW, True, [])
                    autopy.key.toggle(autopy.key.Code.DOWN_ARROW, False, [])

    def control_colume_level(self, img, fingers, cLocx, cLocy, volume):
        if fingers == [1, 0, 1, 1, 1]:
            autopy.mouse.move(cLocx, cLocy)  # 给出鼠标移动位置坐标
            length = cLocx - self.pLocx
            self.pLocx = cLocx
            self.pLocy = cLocy
            current_volume_level = volume.GetMasterVolumeLevelScalar()
            current_volume_level += length / 50.0
            if current_volume_level > 1.0:
                current_volume_level = 1.0
            elif current_volume_level < 0.0:
                current_volume_level = 0.0
            volume.SetMasterVolumeLevelScalar(current_volume_level, None)
            set_volume = volume.GetMasterVolumeLevelScalar()
            # volPer = setVolume
            volBar = 350 - int(set_volume * 200)
            cv2.rectangle(img, (20, 150), (50, 350), (255, 0, 255), 2)
            cv2.rectangle(img, (20, int(volBar)), (50, 350), (255, 0, 255), cv2.FILLED)
            cv2.putText(img, f'{int(set_volume * 100)}%', (10, 380), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    def info_print(self, img):
        # 查看FPS
        cTime = time.time()  # 处理完一帧图像的时间
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime  # 重置起始时·
        # 在视频上显示fps信息，先转换成整数再变成字符串形式，文本显示坐标，文本字体，文本大小
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('frame', img)

    def detect(self, detector):
        cap = self.get_video_capture()
        while True:
            # 图片是否成功接收、img帧图像
            success, img = cap.read()
            # 翻转图像，使自身和摄像头中的自己呈镜像关系
            img = cv2.flip(img, flipCode=1)  # 1代表水平翻转，0代表竖直翻转
            # 在图像窗口上创建一个矩形框，在该区域内移动鼠标
            cv2.rectangle(img, self.leftUpPoint, self.rightDownPoint, (0, 255, 255), 5)
            # 判断当前的活动窗口的进程名字
            # try:
            #     pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
            #     active_window_process_name = psutil.Process(pid[-1]).name()
            # except:
            #     pass
            active_window_process_name = ""
            # 传入每帧图像, 返回手部关键点的坐标信息(字典)，绘制关键点后的图像
            hands, img = detector.findHands(img, flipType=False, draw=True)  # 上面反转过了，这里就不用再翻转了
            # 如果能检测到手那么就进行下一步
            if hands:
                # 获取手部信息hands中的21个关键点信息
                lmList = hands[0]['lmList']  # hands是由N个字典组成的列表，字典包括每只手的关键点信息,此处代表第0个手
                # 获取食指指尖坐标，和中指指尖坐标
                index_finger_xpoint, index_finger_ypoint, index_finger_zpoint = lmList[8]  # 食指尖的关键点索引号为8
                middle_finger_xpoint, middle_finger_ypoint, middle_finger_zpoint = lmList[12]  # 中指指尖索引12
                # （5）检查哪个手指是朝上的
                # 传入手部信息
                fingers = detector.fingersUp(hands[0])
                # 计算食指尖和中指尖之间的距离distance,绘制好了的图像img,指尖连线的信息info
                distance, info, img = detector.findDistance((index_finger_xpoint, index_finger_ypoint),
                                                            (middle_finger_xpoint, middle_finger_ypoint), img)  # 会画圈
                # 确定鼠标移动的范围
                # 将食指指尖的移动范围从预制的窗口范围，映射到电脑屏幕范围
                index_finger_range_xpoint = np.interp(index_finger_xpoint,
                                                      (self.leftUpPoint[0], self.rightDownPoint[0]), (0, self.wScr))
                index_finger_range_ypoint = np.interp(index_finger_ypoint,
                                                      (self.leftUpPoint[1], self.rightDownPoint[1]), (0, self.hScr))
                # 平滑，使手指在移动鼠标时，鼠标箭头不会一直晃动
                cLocx = self.pLocx + (index_finger_range_xpoint - self.pLocx) / self.smooth  # 当前的鼠标所在位置坐标
                cLocy = self.pLocy + (index_finger_range_ypoint - self.pLocy) / self.smooth
                self.release_mouse(fingers)
                self.move_mouse(fingers, cLocx, cLocy)
                self.left_click(img, fingers, distance, index_finger_xpoint, index_finger_ypoint)
                self.right_click(img, fingers, middle_finger_xpoint, middle_finger_ypoint)
                self.drag(img, fingers, cLocx, cLocy)
                self.press_up(img, fingers, active_window_process_name)
                self.press_down(img, fingers, active_window_process_name)
                # self.control_colume_level(img, fingers, cLocx, cLocy, get_volume_info())
            # 显示图像，输入窗口名及图像数据
            self.info_print(img)
            if cv2.waitKey(1) & 0xFF == 27 or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1.0:  # 每帧滞留20毫秒后消失，ESC键退出或鼠标关闭窗口
                break
        release_resource(cap)

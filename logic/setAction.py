from logic.HandTrackingModule import HandDetector


class SetAction:
    def __init__(self):
        # hand_map 手势字典
        self.hand_map = {}
        self.detector = HandDetector(mode=False,  # 视频流图像
                                     maxHands=1,  # 最多检测一只手
                                     detectionCon=0.8,  # 最小检测置信度
                                     minTrackCon=0.5)  # 最小跟踪置信度
        self.pre_frame = None
        self.frame = None
        self.frame_number = 0

    # set_hand_map 设置手势字典
    def set_hand_map(self, action, img):
        hands, _ = self.detector.findHands(img, flipType=False, draw=True)
        flag = True
        if hands:
            fingers = self.detector.fingersUp(hands[0])
            self.frame = fingers
            # 10 帧以内 手势不变录入成功
            if self.pre_frame != self.frame:
                self.frame_number = 0
            if self.pre_frame == self.frame and self.frame_number % 10 == 0:
                # 判断手势是否已经添加
                for hand_act in self.hand_map:
                    if fingers == self.hand_map[hand_act] and hand_act != action:
                        return not flag
                # 未使用的手势则添加
                self.hand_map[action] = fingers
                self.reset_params()
                return flag
            self.pre_frame = self.frame
            self.frame_number += 1
        return flag

    def reset_params(self):
        self.frame_number = 0
        self.pre_frame = None
        self.frame = None

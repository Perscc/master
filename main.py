from HandTrackingModule import HandDetector
from operation import Operation

if __name__ == '__main__':
    detector = HandDetector(mode=False,  # 视频流图像
                            maxHands=1,  # 最多检测一只手
                            detectionCon=0.8,  # 最小检测置信度
                            minTrackCon=0.5)  # 最小跟踪置信度
    operation = Operation()
    operation.detect(detector)

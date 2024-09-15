import cv2
import numpy as np


class CircleCoordinateProvider:
    def __init__(self):
        pass

    def getMask(self, MIN_HSV, MAX_HSV, frame):
        # HSVに変換
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array(MIN_HSV)
        upper = np.array(MAX_HSV)
        mask = cv2.inRange(hsv, lower, upper)

        return cv2.bitwise_and(frame, frame, mask=mask)

    def getCorners(self, frame, t):
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)

        # cv2.findContours の戻り値がOpenCVのバージョンによって異なる
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # タプルをリストに変換する必要がある
        contours = list(contours)
        # 初期化
        radius_frame = frame

        # 一番大きい輪郭を抽出
        if len(contours) > 0:
            # Sort contours by area and keep the largest one
            largest_contour = max(contours, key=cv2.contourArea)
            # 最小外接円を描く
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)
            center = (int(x), int(y))
            radius = int(radius)
        else:
            center = (0, 0)
            radius = 0

        return center, radius

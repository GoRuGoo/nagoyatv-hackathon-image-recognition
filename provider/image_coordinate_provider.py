import cv2
import numpy as np
from typing import List, Tuple


class ImageCoordinateProvider:
    def __init__(self, lower_color_range: Tuple[int, int, int], upper_color_range: Tuple[int, int, int]):
        """
        初期化
        :param lower_color_range: 色検出のためのHSVの下限値
        :param upper_color_range: 色検出のためのHSVの上限値
        """
        self.lower_color_range = lower_color_range
        self.upper_color_range = upper_color_range

    def get_coordinates(self, frame: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """
        画像内の指定された色の領域の座標を検出し、最大の矩形領域の座標を返す
        :param frame: 画像フレーム（BGR形式）
        :return: 最大の矩形領域の座標 [(x, y, w, h)]（見つからない場合は空リスト）
        """
        # BGRからHSVに変換
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 色をマスクする
        mask = cv2.inRange(hsv, self.lower_color_range, self.upper_color_range)

        # 輪郭を検出
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 最大の矩形領域を保存するための変数
        largest_contour = None
        max_area = 0

        # 輪郭に対して座標を取得
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # ノイズを除去するために面積でフィルタリング
                area = cv2.contourArea(contour)
                if area > max_area:
                    max_area = area
                    largest_contour = contour

        # 最大の矩形領域が見つかった場合
        coordinates: List[Tuple[int, int, int, int]] = []
        if largest_contour is not None:
            x, y, w, h = cv2.boundingRect(largest_contour)
            coordinates.append((x, y, w, h))

        return coordinates

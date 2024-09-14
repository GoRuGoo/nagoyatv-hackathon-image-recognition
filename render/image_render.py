import cv2

class ImageRenderer:
    def __init__(self, color=(0, 255, 0), thickness=2):
        """
        初期化
        :param color: 矩形の色 (BGR形式)
        :param thickness: 矩形の線の太さ
        """
        self.color = color
        self.thickness = thickness

    def render_rectangles(self, frame, coordinates):
        """
        フレームに矩形を描画する
        :param frame: 画像フレーム（BGR形式）
        :param coordinates: 矩形領域の座標リスト [(x, y, w, h), ...]
        :return: 描画されたフレーム
        """
        for (x, y, w, h) in coordinates:
            cv2.rectangle(frame, (x, y), (x+w, y+h), self.color, self.thickness)
        return frame

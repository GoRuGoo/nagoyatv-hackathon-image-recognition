from typing import List, Tuple


class DistanceProvider:
    def __init__(self) -> None:
        pass

    def calculate_areas(self, coordinates: List[Tuple[int, int, int, int]]) -> List[int]:
        """
        検出された矩形領域の座標を使って面積を計算する
        :param coordinates: 矩形領域の座標リスト [(x, y, w, h), ...]
        :return: 各矩形領域の面積リスト [area, area, ...]
        """
        areas: List[int] = []

        for (x, y, w, h) in coordinates:
            # 面積を計算 (幅 × 高さ)
            area = w * h
            areas.append(area)

        return areas

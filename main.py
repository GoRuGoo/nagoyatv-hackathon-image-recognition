import cv2
from model.image_coordinate_model_provider import ImageCoordinateProvider
from render.image_render import ImageRenderer
from util.green_hsv_ranges import LOWER_GREEN, UPPER_GREEN

def main():
    # 座標提供用のクラスのインスタンスを生成
    coordinate_provider = ImageCoordinateProvider(LOWER_GREEN, UPPER_GREEN)

    # 描画用のクラスのインスタンスを生成
    renderer = ImageRenderer()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 座標を取得
        coordinates = coordinate_provider.get_coordinates(frame)

        # 座標に基づいて矩形を描画
        frame = renderer.render_rectangles(frame, coordinates)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
from model.image_coordinate_model_provider import ImageCoordinateProvider
from render.image_render import ImageRenderer

def main():
    # 緑色のHSV範囲を定義
    lower_green = (35, 100, 100)
    upper_green = (85, 255, 255)

    # ImageCoordinateProviderクラスのインスタンスを作成
    coordinate_provider = ImageCoordinateProvider(lower_green, upper_green)

    # ImageRendererクラスのインスタンスを作成
    renderer = ImageRenderer()

    # カメラから映像を取得
    cap = cv2.VideoCapture(0)

    while True:
        # カメラからフレームを読み込む
        ret, frame = cap.read()
        if not ret:
            break

        # 座標を取得
        coordinates = coordinate_provider.get_coordinates(frame)

        # 座標に基づいて矩形を描画
        frame = renderer.render_rectangles(frame, coordinates)

        # フレームを表示
        cv2.imshow("Frame", frame)

        # 'q'キーが押されたら終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # カメラ解放とウィンドウの終了
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

import cv2
from render.image_render import CircleRender
from util.yellow_hsv_ranges import LOWER_YELLOW, UPPER_YELLOW

from provider.circle_coordinate_provider import CircleCoordinateProvider


def main():
    circle_coordinate_provider = CircleCoordinateProvider()

    # 描画用のクラスのインスタンスを生成
    render = CircleRender()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        mask = circle_coordinate_provider.getMask(LOWER_YELLOW, UPPER_YELLOW, frame)

        center, radius = circle_coordinate_provider.getCorners(mask, 50)

        radius_frame = cv2.circle(frame, center, radius, (0, 255, 0), 2)

        radius_frame = render.draw_circle(frame, center, radius)

        cv2.imshow("radius_frame", radius_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

import cv2


class CircleRender:
    def __init__(self, circle):
        self.circle = circle

    def draw_circle(self, frame, center, radius):
        radius_frame = cv2.circle(frame, center, radius, (0, 255, 0), 2)
        return radius_frame

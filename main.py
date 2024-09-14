import cv2
import numpy as np

# カメラから映像を取得（もしくは画像ファイルのパスを指定）
cap = cv2.VideoCapture(0)

while True:
    # カメラからフレームを読み込む
    ret, frame = cap.read()
    
    # BGRからHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 緑色のHSV範囲を定義
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])
    
    # 緑色をマスクする
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # マスクを使って元のフレームから緑色部分を抽出
    green = cv2.bitwise_and(frame, frame, mask=mask)
    
    # 輪郭を検出
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # 輪郭に対して座標を取得
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # ノイズを除去するために面積でフィルタリング
            # 輪郭に最小外接矩形を描画
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # 座標を表示
            print(f"緑色の座標: x={x}, y={y}")
    
    # フレームを表示
    cv2.imshow("Frame", frame)
    
    # 'q'キーが押されたら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラ解放とウィンドウの終了
cap.release()
cv2.destroyAllWindows()

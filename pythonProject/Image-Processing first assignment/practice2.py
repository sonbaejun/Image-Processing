import numpy as np, cv2
import math

def onMouse(event, x, y, flags, param):
    global title, line, pt


    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)  # 시작 좌표 지정
        else:
            # 첫 클릭좌표와 두번째 클릭좌표의 차이의 절대값이 각각 dx, dy
            dx = (pt[0] - x)
            dy = (pt[1] - y)
            dx = abs(dx)
            dy = abs(dy)
            # x 꼭짓점 좌표
            if pt[0] < x:
                qx = abs(x - dx * 2)
            else:
                qx = abs(x + dx * 2)
            # y 꼭짓점 좌표
            if pt[1] < y:
                qy = abs(y - dy * 2)
            else:
                qy = abs(y + dy * 2)

            pt = (qx, qy)

            cv2.rectangle(img, pt, (x, y), (255, 0, 0), line)
            cv2.imshow(title, img)
            pt = (-1, -1)  # 시작 좌표 초기화

    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            a = pt[0] - x  # x좌표 간 차이
            b = pt[1] - y  # y좌표 간 차이
            radius = int(math.sqrt((a * a) + (b * b))) // 2  # 피타고라스 정리를 사용해 두 좌표 사이의 거리를 계산(반지름)
            center = np.add(pt, (x,y)) // 2 # 원의 중심
            cv2.circle(img, center, radius, (0, 255, 0), -1)
            cv2.imshow(title, img)
            pt = (-1, -1)  # 시작 좌표 초기화

    cv2.imshow(title, img)

title = 'Draw Event'
img = np.full((400, 600, 3), (255, 255, 255), np.uint8)

cv2.imshow(title, img)

line = 2  # 기본 선 굵기는 2

def line_bar(value):
    global line
    line = value


# 선 굵기 설정 트랙바 생성
pt = (-1, -1)
cv2.createTrackbar('thickness', title, 2, 10, line_bar)
cv2.setTrackbarMin('thickness', title, 1)  # 최솟값 설정

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
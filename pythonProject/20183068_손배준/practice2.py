import cv2 as cv
import numpy as np


def on_trackbar(x):
    pass


cv.namedWindow('test')
cap = cv.VideoCapture(0)

while True:

    ret, img = cap.read()

    img_result = img.copy()

    #색의 평균 구할 위치를 trackbar로 조정
    center_x = (400-320) // 2
    center_y = (400-240) // 2

    #해당영역을 사각형 처리
    cv.rectangle(img_result, (center_x, center_y),
                 (center_x+320, center_y+240), (100, 100, 230), 2)

    #선택 영역의 mat 객체를 가져오고 평균내기
    img_roi = img[center_y:center_y+240, center_x:center_x+320]

    cv.imshow('test', img_result)
    cv.imshow('roi', img_roi)

    if cv.waitKey(1) == 27:
        break
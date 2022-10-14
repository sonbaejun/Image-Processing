import numpy as np, cv2

logo = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)  # 로고 영상 읽기
if logo is None: raise Exception("영상파일 읽기 오류")      # 예외처리

blue, green, red = cv2.split(logo)  # 채널 분리

img_zero = np.zeros_like(blue)  # 빈 채널 생성
blue_img = cv2.merge([blue, img_zero, img_zero])    # 채널 합성(BGR 영역 중 Blue 만 색 값을 주고 나머지는 빈 채널로 구성)
green_img = cv2.merge([img_zero, green, img_zero])  # 채널 합성(BGR 영역 중 Green 만 색 값을 주고 나머지는 빈 채널로 구성)
red_img = cv2.merge([img_zero, img_zero, red])      # 채널 합성(BGR 영역 중 Red 만 색 값을 주고 나머지는 빈 채널로 구성)

cv2.imshow("logo", logo)    # logo 이미지 윈도우에 영상 표시
cv2.imshow("blue_img", blue_img)    # BGR 영역 중 blue만 색 값을 주어 합성한 채널 이미지 윈도우에 영상 표시
cv2.imshow("green_img", green_img)  # BGR 영역 중 green만 색 값을 주어 합성한 채널 이미지 윈도우에 영상 표시
cv2.imshow("red_img", red_img)  # BGR 영역 중 red만 색 값을 주어 합성한 채널 이미지 윈도우에 영상 표시
cv2.waitKey()


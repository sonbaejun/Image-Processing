import cv2
import numpy as np

height = input("높이: ")                  # 키보드로 높이 입력받기
width = input("너비: ")                   # 키보드로 너비 입력받기

width = int(width)                       # 입력받은 너비 int형으로 변환
height = int(height)                     # 입력받은 높이 int형으로 변환
widthCenter = (width - 320) // 2                   # 윈도우 중심에 위치시키기 위해 (윈도우너비-관심영역크기)/2 진행(추후 계산에 사용)
heightCenter = (height - 240) // 2                  # 윈도우 중심에 위치시키기 위해 (윈도우높이-관심영역크기)/2 진행(추후 계산에 사용)

blue, red =(255, 0, 0), (0, 0, 255)      # 파랑, 빨강 bgr값 생성
capture = cv2.VideoCapture(0)            # 0번째 비디오를 capture 변수에 저장
if capture.isOpened() == False:          # 예외처리
    raise Exception("카메라 연결 안됨")

while True:
    cv2.namedWindow("ex11 - mainWindow")                           # 윈도우 이름 변경
    cv2.resizeWindow("ex11 - mainWindow", width, height)           # 윈도우 사이즈 키보드 입력값으로 변경
    ret, frame = capture.read()                             # ret, frame 변수에 비디오 정보 read
    mask = np.full((height, width, 3), blue, np.uint8)      # mask 행렬 선언, 입력받은 크기 + 파랑색으로 채우기
    mask[heightCenter:heightCenter+240, widthCenter:widthCenter+320] = frame[120:360, 160:480]        # mask 행렬의 특정 영역에(윈도우의 중앙) 카메라 프레임의 중앙영역 대입
    if not ret: break                                       # 예외처리
    if cv2.waitKey(30) >= 0: break                          # 키 입력 시 종료

    title = "ex11 - mainWindow"                                    # title 변수 선언
    cv2.rectangle(mask, (widthCenter, heightCenter), (widthCenter+320, heightCenter+240), red)        # 사각형 생성(빨강색 테두리)
    cv2.imshow(title, mask)                                 # 윈도우에 화면 출력

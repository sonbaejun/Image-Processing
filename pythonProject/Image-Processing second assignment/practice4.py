import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)                # GRAYSCALE로 영상읽기
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)                # GRAYSCALE로 영상읽기
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생") # 예외 처리

proportion = [50, 50]                                                       # 초기값 설정
title = "dst"                                                               # title 선언


def desolve():
    synthesis = cv2.addWeighted(image1, proportion[0], image2, proportion[1], 0)    # image1, image2 addWeight 실행
    concated = cv2.hconcat([image1, synthesis, image2])                             # image1, image2 연결
    cv2.imshow(title, concated)                                                     # 윈도우 화면 출력

def onChange0(value):
    proportion[0] = value * 0.01                                                    # image1 비율 값 % 단위 변경
    desolve()                                                                       # desolve 함수 실행

def onChange1(value):
    proportion[1] = value * 0.01                                                    # image2 비율 값 % 단위 변경
    desolve()                                                                       # desolve 함수 실행

cv2.namedWindow(title)                                                              # 윈도우 이름 재설정
cv2.createTrackbar("image1", title, proportion[0], 100, onChange0)                  # 트랙바 생성(image1 비율과 연결)
cv2.createTrackbar("image2", title, proportion[1], 100, onChange1)                  # 트랙바 생성(image2 비율과 연결)
onChange0(proportion[0])                                                            # 비율값으로 변경
onChange1(proportion[1])                                                            # 비율값으로 변경
cv2.waitKey(0)                                                                      # 키 입력대기
cv2.destroyAllWindows()                                                             # 모든 윈도우 소멸
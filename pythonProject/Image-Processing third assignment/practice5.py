import cv2


def bar(value):
    global nameOfWindow, image

    # 이중임계값 트랙바로 표현
    threshold1 = cv2.getTrackbarPos('th1', nameOfWindow)
    threshold2 = cv2.getTrackbarPos('th2', nameOfWindow)

    # 구한 임계값으로 캐네 에지 검출하기
    resultOfcannyedge = cv2.Canny(image, threshold1, threshold2)

    cv2.imshow(nameOfWindow, resultOfcannyedge)


# 영상 읽기
image = cv2.imread("images/cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")
nameOfWindow = 'cannay edge'

# 캐니 에지 검출하기
resultOfcannyedge = cv2.Canny(image, 100, 150)

cv2.imshow(nameOfWindow, resultOfcannyedge)

# 초기값 각각 50, 100
cv2.createTrackbar('th1', nameOfWindow, 50, 255, bar)
cv2.createTrackbar('th2', nameOfWindow, 100, 255, bar)

cv2.waitKey(0)

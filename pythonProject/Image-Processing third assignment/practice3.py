import numpy as np, cv2

image = cv2.imread("images/10.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일 읽기 오류")

#hsv변수에 color convert 버전 삽입
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

dim_histogram = np.zeros((image.shape[:2]), np.uint8)

# 2차원 히스토그램 계산
for row in range(hsv.shape[0]):
    for col in range(hsv.shape[1]):
        dim_histogram[hsv[row, col, 0], hsv[row, col, 1]] += 1

# uint8
frequency = 50
dim_histogram = (dim_histogram/frequency) * 255

color_histogram = np.zeros((180, 256, 3), np.uint8)

# color histogram 계산
for row in range(color_histogram.shape[0]):
    for col in range(color_histogram.shape[1]):
        color_histogram[row, col] = [row, col, dim_histogram[row, col]]

# HSV to BGR convert
color_histogram = cv2.cvtColor(color_histogram, cv2.COLOR_HSV2BGR)
# 원본 영상과 크기 싱크 동기화
width, height = dim_histogram.shape
color_histogramResize = cv2.resize(color_histogram, (height, width))

cv2.imshow("image", image)
cv2.imshow("dst", color_histogramResize)

cv2.waitKey(0)
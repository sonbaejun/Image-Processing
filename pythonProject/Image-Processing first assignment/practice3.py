import cv2

# 컬러 영상 파일을 적재한 후
image = cv2.imread("images/arsenal.jpg", cv2.IMREAD_GRAYSCALE)

if image is None :
    raise Exception("영상 파일 읽기 에러")

# 행렬을 윈도우에 명암도 영상으로 표시하고
cv2.imshow('test', image)

#png 파일의 압축률정도(9가 최대)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]
#jpg 파일의 화질설정 (0~100)
params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 0)

# "test.jpg"와 "test.png" 피일로 각각 저장하시오.
# 이때, 영상 파일을 가장 적은 용량을 가지도록 저장하시오.
cv2.imwrite("images/test.jpg", image, params_jpg)
cv2.imwrite("images/test.png", image, params_png)

cv2.waitKey(0)
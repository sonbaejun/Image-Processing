import numpy as np, cv2
import Common.filters

filter = Common.filters.filter


# 블러링 처리를 위한 함수 (책 발췌)
def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)  # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1] // 2, mask.shape[0] // 2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1  # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1  # 관심영역 너비 범위
            roi = image[y1:y2, x1:x2].astype("float32")  # 관심영역 형변환

            tmp = cv2.multiply(roi, mask)  # 회선 적용 - OpenCV 곱셈
            dst[i, j] = cv2.sumElems(tmp)[0]  # 출력화소 저장
    return dst


image = cv2.imread("images/filter_sharpen.jpg", cv2.IMREAD_COLOR)  # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

img_b, img_g, img_r = cv2.split(image)  # 원본 이미지를 rgb 3채널로 분리

# 샤프닝 마스크 원소 지정
data2 = [[-1, -1, -1],
         [-1, 9, -1],
         [-1, -1, -1]]

# 블러링 마스크 원소 지정
data3 = [1 / 9, 1 / 9, 1 / 9,
         1 / 9, 1 / 9, 1 / 9,
         1 / 9, 1 / 9, 1 / 9]

# 샤프닝 배열 생성
mask2 = np.array(data2, np.float32)

# 블러링 원소 생성
mask3 = np.array(data3, np.float32).reshape(3, 3)

# 분리된 채널들을 각각 샤프닝 하는 과정
sharpen3 = filter(img_r, mask2)
sharpen3 = cv2.convertScaleAbs(sharpen3)

sharpen4 = filter(img_b, mask2)
sharpen4 = cv2.convertScaleAbs(sharpen4)

sharpen5 = filter(img_g, mask2)
sharpen5 = cv2.convertScaleAbs(sharpen5)

# 분리된 채널들을 각각 블러링 하는 과정
blurring2 = filter2(img_g, mask3)
blurring2 = blurring2.astype('uint8')

blurring3 = filter2(img_b, mask3)
blurring3 = blurring3.astype('uint8')

blurring4 = filter2(img_r, mask3)
blurring4 = blurring4.astype('uint8')

# 분리된 채널들 병합
image_result = cv2.merge((sharpen4, sharpen5, sharpen3))
image_result2 = cv2.merge((blurring3, blurring2, blurring4))

# 블러링, 샤프닝 배열 생성
kernal = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]) * (1 / 9)

sharp_mask = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

# filter2D 함수를 이용한 블러링과 샤프닝
blur1 = cv2.filter2D(image, -1, kernal)
sharp1 = cv2.filter2D(image, -1, sharp_mask)

cv2.imshow("bluring OpenCV", blur1)
cv2.imshow("sharpen OpenCV", sharp1)
cv2.imshow("sharpen User", image_result)
cv2.imshow("bluring User", image_result2)
cv2.imshow("image", image)
cv2.waitKey(0)

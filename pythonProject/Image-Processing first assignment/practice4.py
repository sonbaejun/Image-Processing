import numpy as np, cv2

# 흰 배경 3채널 영상 생성
image = np.full((400, 600, 3), (255, 255, 255), np.uint8)

# 색 지정
red, blue = (0, 0, 255), (255, 0, 0)

# 큰 반원의 설정
pt1 = (int(image.shape[1]/2), int(image.shape[0]/2))   # 원의 중심
size1 = (int(image.shape[1]/8), int(image.shape[1]/8))  # 반지름 == 높이의 1/4

# 빨간 큰 반원 그리기
cv2.ellipse(image, pt1, size1,  0, 0, -180, red, -1)
# 파란 큰 반원 그리기
cv2.ellipse(image, pt1, size1,  0, 0, 180, blue, -1)

# 빨간 작은 반원의 설정
pt2 = (int(image.shape[1]/2) - int(size1[1]/2), int(image.shape[0]/2))   # 원의 중심
size2 = (int(image.shape[1]/16), int(image.shape[1]/16))  # 큰 원의 반지름의 반
# 빨간 작은 반원 그리기
cv2.ellipse(image, pt2, size2,  0, 0, 180, red, -1)

# 파란 작은 반원의 설정
pt3 = (int(image.shape[1]/2) + int(size1[1]/2), int(image.shape[0]/2))   # 원의 중심
# 파란 작은 반원 그리기
cv2.ellipse(image, pt3, size2,  0, 0, -180, blue, -1)

cv2.imshow('test', image)
cv2.waitKey(0)
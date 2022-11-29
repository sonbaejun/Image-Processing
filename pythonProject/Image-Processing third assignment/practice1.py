import numpy as np,cv2

image = cv2.imread("images/affine_test1.jpg", cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")

def draw_histo(hist, shape=(256,256)):
    hist_img =np.full(shape, 0, np.uint8)
    gap = hist_img.shape[1]/hist.shape[0]  # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))  # 막대 사각형 시작 x 좌표
        w = int(round(gap))
        roi = (x, 0, w, int(h[0]))
        cv2.rectangle(hist_img, roi, 255, -1)

    return hist_img

# reduce함수 = 각 방향으로 더해서 평균을 낸 함수
histo_v = cv2.reduce(image, dim=0 , rtype=cv2.REDUCE_AVG,dtype=cv2.CV_32F)
histo_v_transpose= np.transpose(histo_v)
histo_h = cv2.reduce(image, dim=1 , rtype=cv2.REDUCE_AVG,dtype=cv2.CV_32F)

# 정규화 진행
cv2.normalize(histo_v, histo_v, 0, 256, cv2.NORM_MINMAX)
cv2.normalize(histo_h, histo_h, 0, 256, cv2.NORM_MINMAX)

# 히스토그램 그리기 함수실행
histo_v_image = draw_histo(histo_v_transpose)
histo_h_image = draw_histo(histo_h)

# 제출양식에 맞춰 히스토그램 회전
histo_v_image = cv2.flip(histo_v_image,0)
histo_h_image = cv2.rotate(histo_h_image, cv2.ROTATE_90_COUNTERCLOCKWISE)[::-1]

# 윈도우 실행
cv2.imshow("image", image)
cv2.imshow("hist_ver", histo_v_image)
cv2.imshow("hist_hor", histo_h_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np, cv2

image = cv2.imread("images/iu4.png", cv2.IMREAD_UNCHANGED)      # UNCHANGED로 받아 alpha 채널을 포함한 4채널로 받음
if image is None: raise Exception("영상 파일 읽기 오류 발생")        # 예외처리

bgra = cv2.split(image)                                         # image 4채널을 각각 분리
imageAvg = cv2.mean(image)                                      # image의 평균값 구해 tuple에 저장

x=0; y=0; w=201; h=303             # 관심영역 시작좌표(x,y) 지정 + 범위(w,h) 지정
roi1 = image[y:y+h, x:x+w]         # image의 관심영역을 roi에 지정(y = 0~303, x = 0~201)
leftTop = cv2.split(roi1)          # 좌측상단부분을 4채널로 분리
leftTopavg = cv2.mean(roi1)        # 좌측상단부분의 평균값 획득

x=201; y=304; w=199; h=295;                      # 관심영역 시작좌표(x,y) 지정
roi2 = image[y:y+h, x:x+w]         # image의 관심영역을 roi에 지정(y = 304~599, x = 201~400)
rightBottom = cv2.split(roi2)      # 우측하단부분을 4채널로 분리
rightBottomavg = cv2.mean(roi2)    # 우측하단부분의 평균값 획득

x=0; y=304; w=201;               # 관심영역 시작좌표(x,y) 지정
roi3 = image[y:y+h, x:x+w]         # image의 관심영역을 roi에 지정(y = 304~599, x = 0~201)
leftBottom = cv2.split(roi3)       # 좌측하단부분을 4채널로 분리
leftBottomavg = cv2.mean(roi3)     # 좌측하단부분의 평균값 획득

x=201; y=0; w=199; h=303;          # 관심영역 시작좌표(x,y) 지정
roi4 = image[y:y+h, x:x+w]         # image의 관심영역을 roi에 지정(y = 0~303, x = 201~400)
rightTop = cv2.split(roi4)         # 우측상단부분을 4채널로 분리
rightTopavg = cv2.mean(roi4)       # 우측상단부분의 평균값 획득

sum = leftTopavg[3] + leftBottomavg[3] + rightTopavg[3] + rightBottomavg[3]
print("전체영역 화소 값 평균 : ", imageAvg[3])              # 전체영역의 투명도 평균값 출력
print("좌측상단 영역 화소값 : ", leftTopavg[3])        # 좌측상단 영역의 투명도 출력
print("좌측하단 영역 화소값 : ", leftBottomavg[3])     # 좌측하단 영역의 투명도 출력
print("우측상단 영역 화소값 : ", rightTopavg[3])       # 우측상단 영역의 투명도 출력
print("우측하단 영역 화소값 : ", rightBottomavg[3])    # 우측하단 영역의 투명도 출력

print("알파채널 4개 부분 화소값의 합 : ", sum)  #알파채널 4개 부분 화소값의 합

cv2.imshow("image", image)                               # 원본영상 출력
cv2.imshow("imageA", bgra[3])                            # alpha채널(투명도) 윈도우에 출력


cv2.waitKey(0)
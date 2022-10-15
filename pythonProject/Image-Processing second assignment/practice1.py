import numpy as np, cv2

def print_rects(rects):
    print("-" * 46)                             	# '-' 라인 출력
    print("사각형 원소\t\t랜덤 사각형 정보\t\t   넓이")   # '설명 출력'
    print("-" * 46)                                # '-' 라인 출력
    for i, (x,y, w,h, a, k) in enumerate(rects):		# 사각형 정보 출력
         print("rects[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" %(k, w, h, x, y, a))
    print()                                         # 공백 출력(한 줄 띄우기)

    rects = rects[idx.astype('int')]                # rects를 넓이 + 내림차순으로 정렬

    print("-" * 46)                                # '-' 라인 출력
    print("사각형 원소\t\t랜덤 사각형 정보\t\t   넓이")   # '설명 출력'
    print("-" * 46)                                # '-' 라인 출력
    for i, (x, y, w, h, a, k) in enumerate(rects):  # 넓이 +  내림차순 순으로 정렬된 사각형 정보 출력
        print("rects[%i] = [(%3d,%3d) from (%3d,%3d)] %5d" % (k, w, h, x, y, a))
    print()                                         # 공백 출력(한 줄 띄우기)

rands = np.zeros((10, 6), np.uint16)        		    # 10행 6열 행렬 생성

starts = cv2.randn(rands[:, :2 ], 100, 50)     		# 시작좌표  랜덤생성
ends = cv2.randn(rands[:, 2:4:1], 300, 50)       	# 종료좌표 랜덤 생성

sizes = cv2.absdiff(starts, ends)					# 시작좌표와 종료좌표간 차분 절대값

areas = sizes[:, 0] * sizes[:, 1]                   # 첫 원소(너비)와 두 번째 원소(높이)를 곱하여 각 사각형의 넓이 계산
rects = rands.copy()                                # 결과 사각형으로 복사
rects[:, 2:4:1] = sizes                             # 2~3열에 크기(가로, 세로) 저장
rects[:,4] = areas                                  # 5열에 넓이 저장

# 6열에 순번 저장
for i in range(0,10):
    rects[i:i+1:1, 5] = i

idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN + cv2.SORT_DESCENDING).flatten() # 사각형의 넓이 순 + 내림차순 정렬을 위해서 areas 행렬에 cv2.sortIdx()함수를 수행해서 정렬 원소의 원본 첨자를 idx에 저장,
                                                                                # 반환 결과가 열벡터 이기에 1차원으로 전개한다

print_rects(rects)  #print_rects()함수를 호출한다, 이때 파라미터값은 rects.



import numpy as np, cv2

img1 = np.full((200, 300), 100, np.uint8)
img2 = np.full((200, 300), 100, np.uint8)

title1, title2 = 'win_mode1', 'win_mode2'   # 윈도우 이름

w, h = img1.shape

cv2.imshow(title1, img1)
cv2.imshow(title2, img2)

cv2.moveWindow(title1, 0, 0)    # 윈도우 이동
cv2.moveWindow(title2, h, w)

cv2.waitKey(0)      # 키 이벤트(key event) 대기
cv2.destroyAllWindows()
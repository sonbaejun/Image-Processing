import numpy as z, cv2
from Common import utils
a=cv2.imread('images/10.jpg', cv2.IMREAD_COLOR)
h, w, c =a.shape
b=a[..., 0]
g=a[..., 1]
r=a[..., 2]
Y=z.zeros((h, w), dtype=z.float_)
C=z.zeros((h, w), dtype=z.float_)
D=z.zeros((h, w), dtype=z.float_)
utils.ck_time(0)
for i in range(h):
    for j in range(w):
        Y[i][j]=0.299*r[i][j]+0.587*g[i][j]+0.114*b[i][j]
        C[i][j]=(r[i][j]-Y[i][j])*0.713+128
        D[i][j]=(b[i][j]-Y[i][j])*0.564+128
m = (z.dstack((Y, C, D))).astype(z.uint8)
cv2.imshow('og', a)
cv2.imshow('YCbCr', m)
b1 = z.zeros((h, w), dtype=z.float_)
g1 = z.zeros((h, w), dtype=z.float_)
r1 = z.zeros((h, w), dtype=z.float_)
for i in range(h):
    for j in range(w):
        b1[i][j]=Y[i][j]+1.773*(D[i][j]-128)
        g1[i][j]=Y[i][j]-0.714*(C[i][j]-128)-0.344*(D[i][j]-128)
        r1[i][j]=Y[i][j]+1.403*(C[i][j]-128)
v = (z.dstack((b1, g1, r1))).astype(z.uint8)
utils.ck_time(1)
cv2.imshow('view', v.astype(z.uint8))
cv2.waitKey(0)
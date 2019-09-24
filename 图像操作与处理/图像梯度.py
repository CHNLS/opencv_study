import cv2
import numpy as np


# Sobel算子
# 3X3矩阵，分左右和上下，靠近中位的权重大于其他，右减左，下减上
#      -1 0 1             -1 -2 -1
# Gx = -2 0 2  * A   Gy=   0  0  0  *A
#      -1 0 1              1  2  1
# 例如
# a1  a2  a3
# a4  a5  a6   Gx=a3-a1+2a6-2a4+a9-a7
# a7  a8  a9   Gy=a7-a1+2a8-2a2+a9-a3
# cv2.Sobel(src, ddepth, dx, dy, ksize)
#     ddepth:图像的深度,通常指定为 1
#     dx和dy分别表示水平和竖直方向
#     ksize是Sobel算子的大小

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('../media/pie.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("img", img)
# 作计算后，有些元素可能为负数，cv2默认将负数置为0，使用cv2.CV_64F取消置为0，使之为计算后的正常数
# 如：白(255)到黑(0)是正数，黑到白就是负数了，所有的负数会被截断成0，所以要取绝对值
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
# cv2.imshow('sobelx', sobelx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
sobelx = cv2.convertScaleAbs(sobelx)  # 取绝对值
cv2.imshow('sobelx', sobelx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 再取Gy
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow('sobely', sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 将Gx和Gy求和
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)  # 权重可自行分配
cv_show('sobelxy', sobelxy)

# 以下方法不建议使用,效果不佳，可能会有重影
# sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
# sobelxy = cv2.convertScaleAbs(sobelxy)
# cv_show('sobelxy', sobelxy)

# 例
img1 = cv2.imread('../media/lena.jpg', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(img1, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(img1, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
# cv_show('sobelxy', sobelxy)

# 如果使用直接计算效果如下
sobelxy1 = cv2.Sobel(img1, cv2.CV_64F, 1, 1, ksize=3)
sobelxy1 = cv2.convertScaleAbs(sobelxy1)
new_sobelxy = np.hstack((sobelxy, sobelxy1))
# cv_show('sobelxy', sobelxy)
cv_show('sobelxy', new_sobelxy)

# Scharr算子,同sobel算子，只是矩阵中权重数值不同
# Sobel算子中权重数值为1，2，1（或-1，-2，-1），Scharr算子中权重数值为3,10,3（或-3，-10，-3）


# laplacian算子
# 对噪音比较敏感，因此通常不单独使用
#     0   1  0
# G = 1  -4  1
#     0   1  0

# 不同算子的差异
img = cv2.imread('../media/lena.jpg', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((sobelxy, scharrxy, laplacian))
cv_show('SobelScharrLaplacian', res)

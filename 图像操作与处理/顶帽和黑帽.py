import cv2
import numpy as np

img = cv2.imread('../media/dige.png')
kernel = np.ones((3, 3), np.uint8)

# 顶帽 = 原始输入-开运算结果
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 黑帽 = 闭运算-原始输入
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat ', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread("../media/dige.png")
cv2.imshow("origin", img)

kernel = np.ones((3, 3), np.uint8)  # 3X3 数组，数组越大，腐蚀度越高
erosion = cv2.erode(img, kernel, iterations=1)  # 进行腐蚀操作，迭代次数为1次，迭代次数越多，腐蚀度越高
cv2.imshow('erosion', erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# pie = cv2.imread('../media/pie.png')
# cv2.imshow('pie', pie)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# kernel = np.ones((30, 30), np.uint8)
# erosion_1 = cv2.erode(pie, kernel, iterations=1)
# erosion_2 = cv2.erode(pie, kernel, iterations=2)
# erosion_3 = cv2.erode(pie, kernel, iterations=3)
# res = np.hstack((erosion_1, erosion_2, erosion_3))
# cv2.imshow('res', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 膨胀操作
# dige_erosion = cv2.erode(img, kernel, iterations=1)
dige_dilate = cv2.dilate(erosion, kernel, iterations=1)
cv2.imshow('dilate', dige_dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()

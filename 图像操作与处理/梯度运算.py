import cv2
import numpy as np

# 梯度 = 膨胀 - 腐蚀
pie = cv2.imread('../media/pie.png')
# kernel = np.ones((3, 3), np.uint8)
kernel = np.ones((5, 5), np.uint8)
# dilate = cv2.dilate(pie, kernel, iterations=1)
# erosion = cv2.erode(pie, kernel, iterations=1)

gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
自适应均衡化
将原有图像分成若干小块，每个小块进行均衡化，再进行合成；
但将图像分块，会有图像边界等因素产生，opencv也提供了方法解决这些问题
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../media/clahe.jpg', 0)  # 0表示灰度图 #clahe
plt.hist(img.ravel(), 256)
plt.show()

equ = cv2.equalizeHist(img)  # 全图均衡化
plt.hist(equ.ravel(), 256)
plt.show()

# res = np.hstack((img, equ))
# cv2.imshow("res", res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 图像分块
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

res_clahe = clahe.apply(img)
res = np.hstack((img, equ, res_clahe))
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()

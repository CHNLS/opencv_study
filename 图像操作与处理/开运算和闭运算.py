import cv2
import numpy as np


img = cv2.imread("../media/dige.png")
kernel = np.ones((3, 3), np.uint8)

# 开运算cv2.MORPH_OPEN：先腐蚀，在膨胀。可消除噪音
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('opening', opening)

# 闭运算cv2.MORPH_CLOSE：先膨胀，再腐蚀。消除前景对象内的小孔或对象上的小黑点
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("close", close)
cv2.waitKey(0)
cv2.destroyAllWindows()

zao = cv2.imread("../media/zaoyin.png")
kernel = np.ones((5, 5), np.uint8)
noise = cv2.morphologyEx(zao, cv2.MORPH_CLOSE, kernel)
cv2.imshow("zao", zao)
cv2.imshow("noise", noise)
cv2.waitKey(0)
cv2.destroyAllWindows()

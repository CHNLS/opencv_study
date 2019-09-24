"""
Canny边缘检测
步骤：
1. 使用高斯滤波器，以平滑图像，滤除噪声。
2. 计算图像中每个像素点的梯度强度和方向。
3. 应用非极大值（Non-Maximum Suppression）抑制，以消除边缘检测带来的杂散响应。
4. 应用双阈值（Double-Threshold）minValue 和 maxValue，检测来确定真实的和潜在的边缘。
    梯度值 > maxVal，处理为边界
    minVal < 梯度值 < maxVal，连有边界保留，否则舍弃
    梯度值 < minVal，舍弃
5. 通过抑制孤立的弱边缘最终完成边缘检测。
"""
import cv2
import numpy as np


def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("../media/lena.jpg", cv2.IMREAD_GRAYSCALE)

v1 = cv2.Canny(img, 80, 150)  # 设置minVal 和 maxVal
v2 = cv2.Canny(img, 50, 100)

res = np.hstack((v1, v2))
cv_show("res", res)


img = cv2.imread("../media/car.png", cv2.IMREAD_GRAYSCALE)
# print(img.shape)
img = cv2.resize(img, (475, 275))

v1 = cv2.Canny(img, 120, 250)  # 设置边界值不一样，效果不一样，越小边界越多
v2 = cv2.Canny(img, 50, 100)

res = np.hstack((v1, v2))
cv_show('res', res)

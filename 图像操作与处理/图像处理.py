import cv2
import matplotlib.pyplot as plt

# 图像阈值
"""
ret, dst = cv2.threshold(src, thresh, maxval, type)
    src： 输入图，只能输入单通道图像，通常来说为灰度图
    dst： 输出图
    thresh： 阈值
    maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
    type：二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV
    
    cv2.THRESH_BINARY 超过阈值部分取maxval（最大值），否则取0
    cv2.THRESH_BINARY_INV THRESH_BINARY的反转
    cv2.THRESH_TRUNC 大于阈值部分设为阈值，否则不变
    cv2.THRESH_TOZERO 大于阈值部分不改变，否则设为0
    cv2.THRESH_TOZERO_INV THRESH_TOZERO的反转
"""
# img = cv2.imread("./cat.jpg", 0)
# cv2.imshow("cat",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # print(img.shape)
# # img = img[:, :, ::-1]  # 彩图为BGR
# ret1, threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret2, threshold2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# ret3, threshold3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# ret4, threshold4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# ret5, threshold5 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#
# titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# media = [img, threshold1, threshold2, threshold3, threshold4, threshold5]
#
# for i in range(6):
#     plt.subplot(2, 3, i + 1), plt.imshow(media[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])  # 不显示坐标刻度
# plt.show()


# 图像平滑去噪
img_noise = cv2.imread("../media/lenaNoise.png")
cv2.imshow('img', img_noise)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 滤波去噪
# 1. 均值滤波：简单的平均卷积操作
# 取 3X3 矩阵，得其平均值
blur = cv2.blur(img_noise, (3, 3))
cv2.imshow('blur', blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 2. 方框滤波:基本和均值一样，可以选择归一化
box = cv2.boxFilter(img_noise, -1, (3, 3), normalize=True)
cv2.imshow('box', box)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 高斯滤波:高斯模糊的卷积核里的数值是满足高斯分布，相当于更重视中间的
aussian = cv2.GaussianBlur(img_noise, (5, 5), 1)
cv2.imshow('aussian', aussian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 中值滤波:相当于用中值代替
# 取 3X3 矩阵，得其中位数
median = cv2.medianBlur(img_noise, 5)  # 中值滤波
cv2.imshow('median', median)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 展示所有的
import numpy as np

res = np.hstack((blur, aussian, median))
# print (res)
cv2.imshow('median vs average', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

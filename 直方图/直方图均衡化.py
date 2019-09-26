import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
映射后灰度值计算方式：
分别统计每一个像素点的灰度值，计算器概率数，除以255得到映射后的灰度值；
当灰度值不是最小时，统计所有小于等于该灰度值的累计概率，再除以255得到该灰度值对应的映射后灰度值
"""

# cv2.calcHist(images,channels,mask,histSize,ranges)
#     images: 原图像图像格式为 uint8 或 ﬂoat32。当参数传入时必须用中括号[]括起来，如[img]
#     channels: 同样用中括号括来它会告函数我们统幅图 像的直方图。如果入图像是灰度图它的值就是 [0]如果是彩色图像 的传入的参数可以是 [0][1][2] 它们分别对应着 BGR。
#     mask: 掩模图像。统整幅图像的直方图就把它为 None。但是如果想统计图像某一部分的直方图的就制作一个掩模图像并使用它。
#     histSize:BIN 的数目。也应用中括号括来
#     ranges: 像素值范围常为 [0256]

img = cv2.imread('../media/cat.jpg', 0)
img = img[..., ::-1]
hist = cv2.calcHist([img], [0], None, [256], [0, 256])  # 参数需加[]
# print(hist.shape)
plt.hist(img.ravel(), 256)
plt.show()

img1 = cv2.imread('../media/cat.jpg', 1)
# img = img[..., ::-1]
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img1], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# mask操作
img2 = cv2.imread('../media/cat.jpg', 0)
# mask = np.zeros(img.shape[:2], np.uint8)
mask = np.zeros_like(img2, np.uint8)
print(mask.shape)
mask[100:300, 100:400] = 255
# plt.imshow(mask)
# plt.show()
cv2.imshow("mask", mask)

masked_img = cv2.bitwise_and(img2, img2, mask=mask)  # 与操作
cv2.imshow('masked_img', masked_img)
cv2.waitKey(0)
# plt.imshow(masked_img)
# plt.show()
mask_data = cv2.calcHist([img2], [0], None, [256], [0, 256])
img_data = cv2.calcHist([img2], [0], mask, [256], [0, 256])
# plt.hist(hist_mask, 256)
plt.plot(img_data), plt.plot(mask_data)
plt.show()



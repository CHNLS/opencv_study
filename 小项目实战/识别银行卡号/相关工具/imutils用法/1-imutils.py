"""
进行基本的图像处理功能，如平移，旋转，缩放，骨架，matplotlib图像显示，排序的轮廓，边缘检测
"""
import cv2
import imutils
import numpy as np

# 1. 查询opencv中的函数方法
# funcs = imutils.find_function("contour")
# funcs = imutils.find_function("read")
# print(funcs)

# 图像平移translation
# x轴和y轴平移距离
from imutils import perspective, contours

img = cv2.imread("../images/ocr_a_reference.png")
translated = imutils.translate(img, 10, 30)
# cv2.imshow("translated", translated)
# cv2.waitKey(0)

# 图像旋转
# 旋转图像和旋转角度（逆时针旋转）
rotated = imutils.rotate(img, 90)
# cv2.imshow("rotated", rotated)
# cv2.waitKey(0)

# 图像大小
# 在保持原图像长宽比例不变的情况下，改变图像大小。也可单独设置长或宽，同时设置长和宽时，以长为标准
resized_w = imutils.resize(img, width=400)
resized_h = imutils.resize(img, height=100)
resized_wh = imutils.resize(img, width=400, height=50)
# cv2.imshow("resized_w", resized_w)
# cv2.imshow("resized_h", resized_h)
# cv2.imshow("resized_wh", resized_wh)
# cv2.waitKey(0)

# 骨架化 Skeletonization
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# size是结构化元素内核的大小
skeleton = imutils.skeletonize(gray, size=(5, 5))
# cv2.imshow("gray", gray)
# cv2.imshow("Skeleton", skeleton)
res = np.hstack((gray, skeleton))
# cv2.imshow("res", res)
# cv2.waitKey(0)


# 使用Matplotlib展示图片
import matplotlib.pyplot as plt

plt.imshow(imutils.opencv2matplotlib(img))
# plt.show()


# url转为image
url = "https://www.baidu.com/img/baidu_resultlogo@2.png"
logo = imutils.url_to_image(url)
# cv2.imshow("URL to Image", logo)
# cv2.waitKey(0)

# 自动边缘检测
edgeMap = imutils.auto_canny(gray)
# cv2.imshow("Original", img)
# cv2.imshow("Automatic Edge Map", edgeMap)
# cv2.waitKey(0)


# 4点透视变换
# 即将一个图片转换为俯视图
notecard = cv2.imread("./notecard.png")
clone = notecard.copy()
print(clone.shape)
pts = np.array([(73, 239), (356, 117), (475, 265), (187, 443)])
# 循环并在复制图上画圆
for (x, y) in pts:
    cv2.circle(clone, (x, y), 5, (0, 255, 0), -1)

warped = perspective.four_point_transform(notecard, pts)
# cv2.imshow("Original", clone)
# cv2.imshow("Warped", warped)
# cv2.waitKey(0)


# 排序轮廓
# 垂直方向排序时，同水平的图像，从右往左开始排序；
# 水平方向排序时，同垂直方向的图像，从下往上排序
# image = cv2.imread("./shapes.png")
# image = cv2.imread("./sort.png")
image = cv2.imread("./sort1.png")
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = imutils.auto_canny(gray)

# find contours in the edge map
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the (unsorted) contours and label them
for (i, c) in enumerate(cnts):
    orig = contours.label_contour(orig, c, i, color=(240, 0, 159))

# show the original image
cv2.imshow("Original", orig)

# loop over the sorting methods
for method in ("left-to-right", "right-to-left", "top-to-bottom", "bottom-to-top"):
    # sort the contours
    (cnts, boundingBoxes) = contours.sort_contours(cnts, method=method)
    clone = image.copy()

    # loop over the sorted contours and label them
    for (i, c) in enumerate(cnts):
        sortedImage = contours.label_contour(clone, c, i, color=(240, 0, 159))

    # show the sorted contour image
    cv2.imshow(method, sortedImage)

# wait for a keypress
cv2.waitKey(0)

# 返回图像列表
from imutils import paths

for image_path in paths.list_images("./"):
    print(image_path)

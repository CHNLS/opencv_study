"""
模板匹配和卷积原理很像，模板在原图像上从原点开始滑动，计算模板与（图像被模板
覆盖的地方）的差别程度，这个差别程度的计算方法在opencv里有6种，然后将每次计
算的结果放入一个矩阵里，作为结果输出。假如原图形是AxB大小，而模板是axb大小，
则输出结果的矩阵是(A-a+1)x(B-b+1)
    TM_SQDIFF：计算平方不同，计算出来的值越小，越相关
    TM_CCORR：计算相关性，计算出来的值越大，越相关
    TM_CCOEFF：计算相关系数，计算出来的值越大，越相关
    TM_SQDIFF_NORMED：计算归一化平方不同，计算出来的值越接近0，越相关
    TM_CCORR_NORMED：计算归一化相关性，计算出来的值越接近1，越相关
    TM_CCOEFF_NORMED：计算归一化相关系数，计算出来的值越接近1，越相关
    注：尽量选择使用归一化的计算方法
"""
import cv2

# 模板匹配
img = cv2.imread('../media/lena.jpg', 1)
template = cv2.imread('../media/face.jpg', 1)
h, w = template.shape[:2]  # 模板高和宽
print(img.shape)
print(template.shape)
print(h, w)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
# 匹配模板,返回对应像素点的匹配程度
# res = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
# print(res.shape)  # img - template + 1

# 取得匹配位置的最小值，最大值及对应位置的坐标
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

for method in methods:
    img2 = img.copy()
    method = eval(method)  # 参数不能是字符串
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        print(min_loc)
    else:
        top_left = max_loc
        print(max_loc)
    # 获取右下定点坐标
    bottom_right = (top_left[0] + w, top_left[1] + h)
    # 使用绘图画矩形
    cv2.rectangle(img2, top_left, bottom_right, (0, 0, 255), 2)
    cv2.imshow("img2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 匹配多个对象
import numpy as np
img_rgb = cv2.imread('../media/mario.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # 转灰度图
template = cv2.imread('../media/mario_coin.jpg', 0)
h, w = template.shape[:2]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
# print(res)
threshold = 0.8
# 取匹配程度大于%80的坐标
loc = np.where(res >= threshold)
# print(loc)
for pt in zip(*loc[::-1]):  # *号表示可选参数，进行翻转。loc为array数组，输出第一个为列，第二个为行。
    bottom_right = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img_rgb, pt, bottom_right, (0, 0, 255), 1)

cv2.imshow('img_rgb', img_rgb)
cv2.waitKey(0)

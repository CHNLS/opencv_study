"""
cv2.findContours(img,mode,method)
    mode:轮廓检索模式
        RETR_EXTERNAL ：只检索最外面的轮廓；
        RETR_LIST：检索所有的轮廓，并将其保存到一条链表当中；
        RETR_CCOMP：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界;
        RETR_TREE：经常使用的模式。检索所有的轮廓，并重构嵌套轮廓的整个层次;
    method:轮廓逼近方法
        CHAIN_APPROX_NONE：以Freeman链码的方式输出轮廓，所有其他方法输出多边形（顶点的序列）。
        CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。
"""
# 为了更高的准确率，使用二值图像。
import cv2


def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# img = cv2.imread('../media/contours.png')
# img = cv2.imread('../media/car.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图
# ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 设置阈值
# cv_show('thresh', thresh)
#
# binary, contours, hierarchy = cv2.findContours(thresh,
#                                                cv2.RETR_TREE,  # 检索所有轮廓
#                                                cv2.CHAIN_APPROX_NONE)
# binary为返回的图像，contours为轮廓像素数组，hierarchy为层级
# print(binary)
# print(contours)
# print(hierarchy)

# 绘制轮廓
# 如果不拷贝，则原图会改变
# draw_img = img.copy()
# draw_img = gray.copy()
# 参数为
#   绘制图像：被画轮廓的图像，
#   轮廓：画哪一个轮廓，
#   轮廓索引：-1表示全部轮廓，其他值会按某个顺序绘制外轮廓或内轮廓
#   颜色模式：BGR格式，(0, 0, 255)表示红色，
#   线条宽度
# res = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
# cv_show('res', res)
#
# # 轮廓特征
# # print(len(contours))
# cnt = contours[0]
# # 面积
# area = cv2.contourArea(cnt)
# # 周长，True表示闭合的
# length = cv2.arcLength(cnt, True)
# print(area, length)


# 轮廓近似
img = cv2.imread('../media/contours2.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

draw_img = img.copy()
res = cv2.drawContours(draw_img, [cnt], -1, (0, 0, 255), 2)
cv_show('res', res)

# epsilon = 0.01 * cv2.arcLength(cnt, True)  # 取周长倍数，数值越小，轮廓越接近原图边界。
epsilon = 0.11 * cv2.arcLength(cnt, True)
# cnt为输入点集。
# epsilon为输出的精度，越小，折线的形状越接近曲线。即判断曲线上某点到相对应两端点直线的距离，距离大于阈值则舍弃，小于阈值则保留
# True表示为闭合区域。
# 输出点集默认为None
approx = cv2.approxPolyDP(cnt, epsilon, True)

# draw_img = img.copy()
res = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 2)
cv_show('res', res)

# 边界矩形
img = cv2.imread('../media/contours.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret1, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary1, contours, hierarchy1 = cv2.findContours(thresh, cv2.RETR_TREE,
                                                 cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv_show('img', img)

area = cv2.contourArea(cnt)
x, y, w, h = cv2.boundingRect(cnt)
rect_area = w * h
extent = float(area) / rect_area
print('轮廓面积与边界矩形比', extent)

# 外接圆
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (0, 255, 0), 2)
cv_show('img', img)

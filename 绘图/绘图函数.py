"""
opencv 的绘图函数都需要一些几个参数：
    img：你想要绘制图形的那幅图像。
    color：形状的颜色。需要传入一个元组，如RGB：(255,0,0)。对于灰度图只需要传入灰度值。
    thickness：线条的粗细。如果给一个闭合图形设置为-1，那么这个图形就会被填充。默认值是1.
    linetype：线条的类型，8-connected(8连接)，anti-aliased线条(抗锯齿)等。默认情况是8 连接。cv2.LINE_AA为抗锯齿，这样看起来会非常平滑
    直线还需以下参数
    pt1，直线起点坐标
    pt2，直线终点坐标
    无返回值
"""
import cv2
import numpy as np


def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 1. 画线 cv2.line()
img = np.zeros((512, 512, 3), np.uint8)  # 相当于创建了个背景图
img1 = img.copy()
cv2.line(img, (0, 0), (511, 511), (255, 0, 0),
                5)  # (0,0),(511,511)表示起始和终止位置
# cv_show("img", img)

# 2. 画矩形 cv2.rectang()
# 传入左上角顶点和右下角顶点的坐标
# 如果没有拷贝ndarray数组，所有的绘图都会在一个画板上绘图
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# cv2.rectangle(img1, (384, 0), (510, 128), (0, 255, 0), 3)
# cv_show("img", img)

# 3. 画圆 cv2.circle()
# 指定圆心坐标和半径大小
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# # cv_show("img", img)

# 4. 画椭圆 cv2.ellipse()
# 输入几个参数
#     1. 中心点的位置坐标
#     2. 长轴和短轴的长度
#     3. 椭圆沿逆时针方向旋转的角度
#     4. 椭圆弧沿顺时针方向起始的角度和结束角度，如果是0 和 360，就是整个椭圆
# ellipse = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (0, 255, 0), -1, cv2.LINE_AA)
# # cv_show("img", img)

# 5. 画多边形 cv2.polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]])
# isClosed: 多边形是否闭合
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 这里reshape 的第一个参数,表明这一维的长度是根据后面的维度的计算出来的。
cv2.polylines(img, [pts], True, (0, 255, 0), 5, cv2.LINE_AA)

# 在图片上添加文字
# cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
#     img，图片
#     text，想要输出到图像上的的文本
#     org，文字的起始坐标（左下角为起点）
#     position，输出位置的坐标
#     Font type，字体，可以用cv2.putText()函数文档查看支持的字体,
#     Font Scale，指定字体大小，文字大小（缩放比例）
#     其他，如颜色，线宽，线型等，推荐使用lineType = cv2.LINE_AA
# 添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)
cv2.putText(img, 'OpenCV', (20, 450), font, 4, (255, 255, 255), 2, lineType=cv2.LINE_AA)

# total = np.hstack((line, rectangle, circle, ellipse))
cv2.imshow("total", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

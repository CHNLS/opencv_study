import cv2
import numpy as np

"""
cv2.getTrackbarPos()
    第一个参数是滑动条名字，
    第二个时所在窗口名
cv2.createTrackbar()
    第一个参数是滑动条的名字
    第二个参数是滑动条被放置窗口的名字
    第三个参数是滑动条的默认位置
    第四个参数是滑动条的最大值
    第五个函数是回调函数，每次滑动条的滑动都会调用回调函数，通常都会含有一个默认参数，就是滑动条的位置

滑动条也可以用作转换按钮，只有当装换按钮指向ON 时，滑动条的滑动才有用，否则窗户口都是黑的。
"""


def callback(c):
    pass


# 创建一副黑色图像
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, callback)
cv2.createTrackbar('G', 'image', 0, 255, callback)
cv2.createTrackbar('B', 'image', 0, 255, callback)
# 创建一个开关滑动条，只有两个值，起开关按钮作用
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, callback)
while 1:
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
        cv2.imshow('image', img)
    else:
        img[:] = [b, g, r]
        cv2.imshow('image', img)
cv2.destroyAllWindows()

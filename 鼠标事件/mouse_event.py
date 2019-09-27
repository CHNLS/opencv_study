# 查看所有鼠标事件
import cv2
import numpy as np

"""
cv2.EVENT_FLAG_ALTKEY    # 按住alt不放
cv2.EVENT_FLAG_CTRLKEY   # 按住ctrl不放 
cv2.EVENT_FLAG_LBUTTON   # 鼠标左键按下不放
cv2.EVENT_FLAG_MBUTTON   # 中键不放
cv2.EVENT_FLAG_RBUTTON   # 鼠标右键按下不放
cv2.EVENT_FLAG_SHIFTKEY  # 鼠标shift键按下不放
cv2.EVENT_LBUTTONDBLCLK   # 鼠标双击
cv2.EVENT_LBUTTONDOWN     # 左键按下
cv2.EVENT_LBUTTONUP       # 左键释放
cv2.EVENT_MBUTTONDBLCLK   # 中键双击
cv2.EVENT_MBUTTONDOWN     # 中键按下
cv2.EVENT_MBUTTONUP       # 中键释放
cv2.EVENT_MOUSEHWHEEL     # 横向滚轮滑动
cv2.EVENT_MOUSEMOVE       # 鼠标移动
cv2.EVENT_MOUSEWHEEL      # 滚轮滑动
cv2.EVENT_RBUTTONDBLCLK   # 右键双击
cv2.EVENT_RBUTTONDOWN     # 右键按下
cv2.EVENT_RBUTTONUP       # 右键释放
"""

events = [i for i in dir(cv2) if 'EVENT' in i]
# for i in events:
#     print(i)


def draw_circle(event, x, y, flags, param):
    # 双击地方画圆
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        # return (x, y)


# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(2) & 0xFF == 27:
        break
cv2.destroyAllWindows()
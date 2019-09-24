import numpy as np
import cv2

# 图片路径，灰度：0为无色彩，即灰度图，1位原图色。读取的格式为 GBR
# cv2.IMREAD_COLOR：同1，彩色图像
# cv2.IMREAD_GRAYSCALE：同,0，灰度图像
img = cv2.imread("../media/cat.jpg", 1)

# 可先设置窗口
# cv2.WINDOW_AUTOSIZE  初始
# cv2.WINDOW_NORMAL  # 可自动调整窗口大小
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow("cat", img)  # 第一个参数是窗口的名字，第二个为图像
# # 键盘绑定函数。单位毫秒，参数为0，将会无限期的等待键盘任意键输入
# # cv2.waitKey(2000)  # 2秒
# cv2.waitKey(0)
# cv2.destroyAllWindows()   # 删除任何已建立的窗口
# cv2.destroyWindow("cat")   # 删除指定窗口名的已建立的窗口

# def cv_show(name, img):
#     # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#     cv2.imshow(name, img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# cv_show("cat", img)

# 保存图像
# cv2.imwrite("new_cat.png", img)

# cv2.imshow("image", img)
# k = cv2.waitKey(0)
# # k = cv2.waitKey(0)&0xFF  # 64位系统
# if k == 27:   # 键盘ESC键
#     cv2.destroyAllWindows()
# if k == ord("s"):  # 键盘s键
#     cv2.imwrite("new_cat.png", img)
#     cv2.destroyAllWindows()

# opencv读取为BGR matplotlib为RGB，解决matplotlib不能正常显示问题
# img = img[..., ::-1]  # 同img[:, :, ::-1]
# cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # 修改坐标轴数字，为空则没有
# plt.show()

# 提取颜色通道, 即索引分别为0， 1， 2
b, g, r = cv2.split(img)
# print("b:", b)
# print(b.shape)
# print("g:", g)
# print("r:", r)

# 合并
# img2 = cv2.merge((b, g, r))
# cv2.imshow("img2_cat", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 只保留一色：如R
cop_img = img.copy()
cop_img[:, :, 0] = 0
cop_img[:, :, 1] = 0
cv2.imshow("R", cop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

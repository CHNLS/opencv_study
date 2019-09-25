import cv2


def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("../../media/AM.png")
# cv_show("img", img)
print(img.shape)

# 向上采样法
up = cv2.pyrUp(img)
cv_show('up', up)
print(up.shape)
# 向下采样法
down = cv2.pyrDown(img)
cv_show('down', down)
print(down.shape)

# 采样方法可以进行连续调用，但是先上后下或先下后上，并不能还原图像，其中有0数据填充和数据丢失

# 拉普拉斯金字塔, 最后将图像还原为原shape
down = cv2.pyrDown(img)
down_up = cv2.pyrUp(down)
l_1 = img - down_up
cv_show('l_1', l_1)
print(l_1.shape)

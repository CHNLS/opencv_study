import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("../media/cat.jpg", 1)
img2 = cv2.imread("../media/cat.jpg", 1)
# print(img1)
print(img1.shape)
# 图片type是numpy.ndarray格式，但是计算方式并不与numpy相同，没饿像素点都在0~255之间，
# 因此相加时超过值255就会用两值和取余256，即 %256得到的结果
imgs = img1 + img2
# print(imgs)
# print(img1[:5,:,0])
# cv2.add() 方法相加，当超过255时取255，没超过则取相应 的数值
imgs2 = cv2.add(img1, img2)
# print(imgs2)

# 图像融合
# 两个shape不同的图片不能直接相加
img_dog = cv2.imread("../media/dog.jpg", 1)
print(img_dog.shape)
img_dog = cv2.resize(img_dog, (500, 414))  # 转换图片shape,shape内元组为(列，行)
print(img_dog.shape)
img1 = img1[..., ::-1]   # 将BRG转为RGB
# resize 也可以拉伸和压缩图像，参数fx将横轴拉伸或压缩，fy将纵轴拉伸或压缩
resize_img = cv2.resize(img1, (0, 0), fx=2, fy=3)
plt.imshow(resize_img)
plt.show()



# 公式ax**2 + bx**2 + c = 0
res = cv2.addWeighted(img1, 0.4, img_dog, 0.6, 0)

cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
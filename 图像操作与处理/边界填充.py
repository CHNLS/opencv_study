import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../media/cat.jpg", 1)

# BORDER_REPLICATE：复制法，也就是复制最边缘像素。如：aaaaaa|abcdefgh|hhhhhhh
# BORDER_REFLECT：反射法，对感兴趣的图像中的像素在两边进行复制例如：fedcba|abcdefgh|hgfedcb
# BORDER_REFLECT_101：反射法，也就是以最边缘像素为轴，对称，gfedcb|abcdefgh|gfedcba
# BORDER_WRAP：外包装法cdefgh|abcdefgh|abcdefg
# BORDER_CONSTANT：常量法，常数值填充。

# 填充值
top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)

# 复制法，也就是复制最边缘像素
replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size,
                               right_size, borderType=cv2.BORDER_REPLICATE)
# 反射法，对感兴趣的图像中的像素在两边进行复制例如：fedcba|abcdefgh|hgfedcb
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                             cv2.BORDER_REFLECT)
# 反射法，也就是以最边缘像素为轴，对称，gfedcb|abcdefgh|gfedcba
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size,
                                right_size, cv2.BORDER_REFLECT_101)
# 外包装法cdefgh|abcdefgh|abcdefg
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                          cv2.BORDER_WRAP)
# 常量法，常数值填充。
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,
                              cv2.BORDER_CONSTANT, value=1)  # 0 为黑色

# cv2.waitKey(0)
# cv2.imshow("replicate", replicate)
# cv2.imshow("reflect", reflect)
# cv2.imshow("reflect101", reflect101)
# cv2.imshow("wrap", wrap)
# cv2.imshow("constant", constant)
# cv2.destroyAllWindows()

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()

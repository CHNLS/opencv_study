# 视频文件
import cv2

# 参数可以是设备索引号 也可以是视频文件。
# 设备索引号就是在指定要使用的摄像头。一般的笔记本电脑都有内置摄像头。所以参数就是0。可以设置1或其他值
# cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("./test.mp4")
# # cap 可能不能成功初始化摄像头设备
# # if cap.isOpened():  # 判断是否成功初始化，成功返回True
# #     is_open, frame = cap.read()
# # else:
# #     is_open = False
# # while is_open:
# while cap.isOpened():
#     # 返回值为布尔值和数据,读帧正确返回True
#     ret, frame = cap.read()
#     if frame is None:
#         break
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('video', gray)
#     if cv2.waitKey(25) & 0xFF == ord('q') or cv2.waitKey(25) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)
# FourCC 就是一个4 字节码，用来确定视频的编码格式，通常使用XVID
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame = cv2.flip(frame, 0)  # 翻转（上下）
        out.write(frame)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

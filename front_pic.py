import cv2
import time
import numpy as np

# 选取摄像头，0为笔记本内置的摄像头，1,2···为外接的摄像头
camera = cv2.VideoCapture(0)
first_frame = None  # 初始化背景
new_frame = None
input("get static background:")
while True:
    (grabbed, frame) = camera.read()
    # 对帧进行预处理，先转灰度图，再进行高斯滤波。
    # 用高斯滤波对图像处理，避免亮度、震动等参数微小变化影响效果
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (5, 5), 0)
    new_frame = np.zeros(gray.shape[:2], np.uint8)
    # 将第一帧设置为整个输入的背景
    if first_frame is None:
        first_frame = gray
        input("type anything start:")
        continue
    row, col = gray.shape
    for i in range(row):
        for j in range(col):
            if gray[i, j] == first_frame[i, j]:
                new_frame[i, j] = gray[i, j]
            else:
                new_frame[i, j] = 0
    cv2.imshow("living", new_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


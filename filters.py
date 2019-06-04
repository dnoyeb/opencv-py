import cv2 as cv
import numpy as np


def blur(image):
    """均值模糊，用来去噪声"""
    dst = cv.blur(image, (5, 5))  # ksize=(1,3),均值模糊，stride=1
    cv.namedWindow("mean_blur", 0)
    cv.resizeWindow("mean_blur", 300, 400)
    cv.imshow("mean_blur", dst)


def median_blur(image):
    """中值模糊，平滑椒盐噪声"""
    dst = cv.medianBlur(image, 5)  # ksize=5
    cv.namedWindow("median_blur", 0)
    cv.resizeWindow("median_blur", 300, 400)
    cv.imshow("median_blur", dst)


def custom_blur(image):
    """自定义模糊"""
    kernel = np.ones([5, 5], np.float32) / 25  # 防止溢出255
    kernel1 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化算子
    dst = cv.filter2D(image, -1, kernel=kernel1)  # -1，表示默认的ddepth
    cv.namedWindow("custom_blur", 0)
    cv.resizeWindow("custom_blur", 300, 400)
    cv.imshow("custom_blur", dst)


src = cv.imread("img/test.jpg")
cv.namedWindow("src", 0)
cv.resizeWindow("src", 300, 400)
cv.imshow("src", src)
blur(src)
median_blur(src)
custom_blur(src)
cv.waitKey(0)
cv.destroyAllWindows()

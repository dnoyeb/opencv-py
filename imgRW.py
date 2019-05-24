#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    图片的读取和保存
'''
import numpy
import cv2

img = cv2.imread("img/test.png")
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
#0xFF  64位系统中使用
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("img/test1.png", img)
    cv2.destroyAllWindows()

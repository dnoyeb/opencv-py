#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    轮廓
'''
import numpy as np
import cv2

im = cv2.imread("img/test.png")
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(image, contours, 3, (0,255,0), 3)
cv2.imshow("image", img)
#0xFF  64位系统中使用
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("img/test1.png", img)
    cv2.destroyAllWindows()

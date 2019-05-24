#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    线 圆 文字的绘制
'''
import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.ellipse(img,(256,256),(100,50),0,0,90,255,-1)

pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
pts=pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 255, 255))
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow("image", img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
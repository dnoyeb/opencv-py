#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    使用matplotlib预览保存图片
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("img/test.png")
plt.imshow(img,cmap="Greys",interpolation='bicubic')
#去除xy轴标注
plt.xticks([]),plt.yticks([])
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:44:26 2019

@author: thuli
"""
import cv2
import numpy as np

img=cv2.imread('13.png',0)
edges=cv2.Canny(img,5,30)
cv2.imwrite('13_e_5_30.png',edges)


ret,thresh1 = cv2.threshold(img,3,255,cv2.THRESH_BINARY)
cv2.imwrite('13_t.png',thresh1)
edges=cv2.Canny(thresh1,5,30)
cv2.imwrite('13_e_t.png',edges)
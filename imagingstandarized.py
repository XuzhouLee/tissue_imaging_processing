# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:02:25 2019

@author: thuli
"""
"""
This script is designed for standardlized the fluoresence emission intensity.
"""
import cv2
import numpy as np
class standard():
    def __init__(self):
        self.shadow=np.ones((3,3))
        
    def set_cali(self,calishadow):
        self.shadow=calishadow
        print("Shadow is updated and the size is",self.shadow.shape)
    
    def standarized(self,image):
        outimage=np.true_divide(image,self.shadow)
        print("Image has been standarized")
        return outimage
        
if __name__=="__main__":
    image=cv2.imread('13.png')
    calishadow=0.5*np.ones(image.shape)
    s=standard()
    s.set_cali(calishadow)
    output=s.standarized(image)
    cv2.imwrite('13_s.png',output)

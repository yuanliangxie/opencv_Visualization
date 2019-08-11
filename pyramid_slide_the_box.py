# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:13:24 2019

@author: 渊良
"""
import cv2
import numpy as np

def resize(img, scaleFactor):
    return cv2.resize(img, (int(img.shape[1]*(1/scaleFactor)),
                               int(img.shape[0]*(1/scaleFactor))),
    interpolation = cv2.INTER_AREA)
img=cv2.imread('000007.jpg')
'''###########################resize实验############################
for i in range(1,1000,1):
    cv2.waitKey(1)
    cv2.imshow('resize', resize(img, 1+i/2000))
cv2.destroyAllWindows()
'''###################################金字塔生成器函数####################
def pyramid(image, scale = 1.25 ,minsize = (100, 50)):
    yield image
    while True:
        image = resize(image, scale)
        if image.shape[0] <minsize[1] or image.shape[1] < minsize[0]:
            break
        yield image
##########################金字塔生成器实验########################
'''for x in pyramid(img):
    cv2.waitKey(2000)
    cv2.imshow('pyramid', x)
cv2.destroyAllWindows()
'''
##########################金字塔生成器加滑动窗口###################

def sliding_window(image, stepsize_h, stepsize_w, windowsize):
   for h in range(0, image.shape[0], stepsize_h):
       for w in range(0, image.shape[1], stepsize_w):
           yield(h, w, h+windowsize[0], w+windowsize[1])
            


for reduce_img in pyramid(img):
    for (x, y, x1, y1) in sliding_window(reduce_img, 40, 100, (40, 100)):
        if x1 <= reduce_img.shape[0] and y1 <= reduce_img.shape[1]:
            reduce_img_copy = np.copy(reduce_img)
            cv2.rectangle(reduce_img_copy, (int(y), int(x)), (int(y1), int(x1)), (0, 255, 0), 2)
            cv2.imshow('silding_window', reduce_img_copy)
            #cv2.rectangle(reduce_img, (int(y), int(x)), (int(y1), int(x1)), (255, 255, 255), 2)
            cv2.waitKey(200)
        else:
            pass
cv2.destroyAllWindows()


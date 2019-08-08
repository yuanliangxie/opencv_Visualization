# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:48:10 2019

@author: 渊良
"""
import cv2
img = cv2.imread('000007.jpg')

def cut_the_picture(image, x1, x2, color, line_width):
    h, w, _ = image.shape
    for i in range(x1-1):
        line_h = int((i+1)*h/x1)
        cv2.line(image, (0, line_h), (w, line_h), color, line_width)
    for i in range(x2-1):
        line_w = int((i + 1) * w / x2)
        cv2.line(image, (line_w, 0), (line_w, h), color, line_width)
    return image


def mark_rectangle(image, leftup_corner, rightdown_corner, color, line_width):
    center_corner = (int((rightdown_corner[0]+leftup_corner[0])/2), \
                     int((rightdown_corner[1]+leftup_corner[1])/2))
    cv2.rectangle(img, leftup_corner, rightdown_corner, color, line_width)
    cv2.line(image, leftup_corner, rightdown_corner, color, line_width)
    cv2.line(image, (rightdown_corner[0], leftup_corner[1], ),\
             (leftup_corner[0], rightdown_corner[1]), color, line_width)
    cv2.circle(image, center_corner, 10, (0, 0, 213), -1)
    return image

img = mark_rectangle(img, (462,37),(635,231),(0,255,0),2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
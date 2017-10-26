# -*- coding: utf-8 -*-
"""
@author xiaodong2012
@time 2017-10-25
@information take a note about the OpenCV-Python-Tutorial book
"""
#Today i mainly learn that how to  read a picture and show a picture

import cv2
import  numpy as np
from  matplotlib import pyplot as plt

#practice1:
#cv2.imread();cv2.imshow();cv2.imwrite()
#example1
# img = cv2.imread('denglijun.jpg',0)
# cv2.imshow('DENGLIJUN',img)   #第一个参数窗口的名字，第二个参数是图片
# cv2.waitKey(0)                #键盘绑定函数，设置参数为0，将会无限期的等待键盘输入
# cv2.destroyAllWindows()       #删除创建的窗口，加窗口名
# cv2.imwrite('denglijun1.jpg',img)     #保存图像

#example2
#先创建一个窗口，之后再加载图像，使用cv2.namedWindow(),  初始设置函数标签为cv2.WINDOW_AUTOSIZE/改为cv2.WINDOW_NORMAL  可调整大小
# img = cv2.imread('denglijun.jpg')
# cv2.namedWindow('denglijun.jpg',cv2.WINDOW_NORMAL)
# cv2.imshow('DENGLIJUN',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #example3
# img = cv2.imread('denglijun.jpg')
# cv2.imshow('denglijun',img)
# k = cv2.waitKey(0)
# if k==27:    #按下esc直接退出
#     cv2.destroyAllWindows()
# elif k =='s':
#     cv2.imwrite('denglijun2.jpg',img)
#     cv2.destroyAllWindows()

#example4
img = cv2.imread('denglijun.jpg')
plt.imshow(img,cmap ='gray',interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()

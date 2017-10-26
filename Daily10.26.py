# -*- coding: utf-8 -*-
"""
@author xiaodong2012
@time 2017-10-26
@information take a note about the OpenCV-Python-Tutorial book
"""
# How to read a video 、show a video and save it.
# cv2.VideoCapture()    cv2.VideoWrite()

import  numpy as np
import cv2
# 为了获取视频，先创建一个VideoCapture对象。参数设备索引号或视频文件。 默认笔记本参数0

# #example1   从摄像头中捕获视频
# cap = cv2.VideoCapture(0)
# while True:
#     #capture frame by frame
#     """
#     cap.read()返回一个布尔值True/False ，如果帧读取的是正确的，就是Truej
#     可以使用cap.isOpened()检查是否成功初始化。True，正确；也可以使用cap.open()
#     """
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

# # example2 从文件中读取视频
# """
# 把设备索引号改为文件名字，使用cv2.waiKey()设置播放速度。25毫秒就行。
# """
# cap = cv2.VideoCapture(0)
# #define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
# while(cap.isOpened()):
#     ret,frame = cap.read()
#     if ret == True:
#         frame = cv2.flip(frame,0)
#         out.write(frame)
#         cv2.imshow('frame',frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# cap.release()
# out.release()
# cv2.destroyAllWindows()

# example3  how to save a video
"""
首先创建一个VideoWriter的对象。确定输出文件名字。指定FourCC编码。isColor标签，如果是True，则为彩色图
"""
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()


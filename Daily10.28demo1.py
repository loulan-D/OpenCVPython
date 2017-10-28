# -*- coding: utf-8 -*-
"""
@author xiaodong2012
@time 2017-10-28
@information take a note about the OpenCV-Python-Tutorial book
"""
"""
opencv中的绘图函数：
注意所有的绘图函数的返回值都是none，故不能有赋值
cv2.line();cv2.circle();cv2.rectangle();cv2.ellipse()画椭圆;cv2.putText();
上面所有的这些绘图函数需要设置下面这些参数：
• img：你想要绘制图形的那幅图像。
• color：形状的颜色。以 RGB 为例，需要传入一个元组，例如：（ 255,0,0）
代表蓝色。对于灰度图只需要传入灰度值。
• thickness：线条的粗细。如果给一个闭合图形设置为 -1，那么这个图形
就会被填充。默认值是 1.
• linetype：线条的类型， 8 连接，抗锯齿等。默认情况是 8 连接。 cv2.LINE_AA
为抗锯齿，这样看起来会非常平滑。
"""
import numpy as np
import cv2

# make a blue line
img = np.zeros((522,522,3),dtype='int32')   #create a black image
cv2.line(img,(0,0),(511,511),(255,0,0),5)     # Draw a diagonal blue line with thickness of 5 px

# make a rectangle
# 画一个矩形，你需要告诉函数的左上角顶点和右下角顶点的坐标
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#make a circle
cv2.circle(img,(447,63),(63),(0,0,255),-1)

#在图片上显示文字
"""
在图片上添加文字，设置下列参数：
绘制的文字，绘制的位置，字体类型，字体大小，字体颜色 推荐linetype = cv2.LINE_AA
"""
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv',(10,500),font,4,(255,255,255),2)

winname = "test"
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyAllWindows(winname)

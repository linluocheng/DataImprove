import cv2
import numpy as np

def Toushi(img,abs,text):
    img = cv2.imread(img)
    text_pro = text.split(',')

    left1 = int(text_pro[0])
    left2 = int(text_pro[1])
    left3 = int(text_pro[2])
    left4 = int(text_pro[3])
    right1 = int(text_pro[4])
    right2 = int(text_pro[5])
    right3 = int(text_pro[6])
    right4 = int(text_pro[7])

    width, height = 200, 200  # 所需图像大小

    pts1 = np.float32([[left1, right1], [left2, right2], [left3, right3], [left4, right4]])  # 所需图像部分四个顶点的像素点坐标
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # 定义对应的像素点坐标
    matrix = cv2.getPerspectiveTransform(pts1, pts2)  # 使用getPerspectiveTransform()得到转换矩阵
    img_pro = cv2.warpPerspective(img, matrix, (width, height))  # 使用warpPerspective()进行透视变换

    cv2.imwrite(abs,img_pro)
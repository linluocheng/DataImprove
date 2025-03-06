import cv2
import numpy as np

def Dilate(img,abs):
    img = cv2.imread(img,0)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(img,kernel,iterations = 1)
    cv2.imwrite(abs,dilation)
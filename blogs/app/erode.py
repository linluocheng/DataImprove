import cv2
import numpy as np

def Erode(img,abs):
    img = cv2.imread(img,0)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite(abs,erosion)
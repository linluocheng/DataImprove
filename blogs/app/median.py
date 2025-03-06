import cv2

def Median(img,abs):
    img = cv2.imread(img)
    img_median = cv2.medianBlur(img, 5)
    cv2.imwrite(abs,img_median)
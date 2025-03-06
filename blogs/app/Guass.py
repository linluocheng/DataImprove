import cv2

def Guass(img,abs):
    img = cv2.imread(img)
    img = cv2.GaussianBlur(img, (3, 3), 1)
    cv2.imwrite(abs,img)
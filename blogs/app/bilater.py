import cv2

def Bilater(img,abs):
    img = cv2.imread(img)
    img_bilater = cv2.bilateralFilter(img,9,75,75)
    cv2.imwrite(abs,img_bilater)
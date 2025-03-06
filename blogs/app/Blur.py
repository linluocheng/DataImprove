import cv2

def Blur(img,abs):
    img = cv2.imread(img)
    img_mean = cv2.blur(img, (5,5))
    cv2.imwrite(abs,img_mean)
import cv2

def HSV(img,abs):
    img = cv2.imread(img)
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite(abs,HSV_img)
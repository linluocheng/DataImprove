import cv2

def Gray(img,abs):
    img = cv2.imread(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cv2.imwrite(abs,img)
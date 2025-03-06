import cv2

def Canny(img,abs):
    img = cv2.imread(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    img = cv2.Canny(img, 128, 200)
    cv2.imwrite(abs,img)
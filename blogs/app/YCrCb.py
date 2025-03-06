import cv2

def YCrCb(img,abs):
    img = cv2.imread(img)
    YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    cv2.imwrite(abs,YCrCb)
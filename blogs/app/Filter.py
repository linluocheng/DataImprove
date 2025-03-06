import cv2

def Filter(img,abs):
    img = cv2.imread(img)
    res = cv2.boxFilter(img, -1, (10, 10), normalize=1)
    cv2.imwrite(abs,res)
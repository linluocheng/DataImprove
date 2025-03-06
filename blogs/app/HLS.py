import cv2

def HLS(img,abs):
    img = cv2.imread(img)
    HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    cv2.imwrite(abs,HLS)
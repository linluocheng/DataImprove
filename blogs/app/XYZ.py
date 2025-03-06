import cv2

def XYZ(img,abs):
    img = cv2.imread(img)
    XYZ = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
    cv2.imwrite(abs,XYZ)
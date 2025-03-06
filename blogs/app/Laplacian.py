import cv2

def Laplacian(img,abs):
    img = cv2.imread(img,0)
    gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
    dst = cv2.convertScaleAbs(gray_lap)
    cv2.imwrite(abs,dst)
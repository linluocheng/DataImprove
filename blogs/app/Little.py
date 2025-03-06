import cv2
import numpy as np

def Little(img,abs,beilv):
    img = cv2.imread(img)
    beilv = float(beilv)
    width = img.shape[0]
    height = img.shape[1]
    img_white = np.ones((width, height, 3), dtype=np.uint8)
    promax = cv2.resize(img, (0, 0), fx=beilv, fy=beilv, interpolation=cv2.INTER_NEAREST)
    print(promax.shape)
    max_width = promax.shape[0]
    max_height = promax.shape[1]
    img_white[0:max_width, 0:max_height] = promax
    cv2.imwrite(abs,img_white)
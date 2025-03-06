import cv2

def Revole(img,abs,choice):
    img = cv2.imread(img)

    if choice == '0':
        img = cv2.flip(img,0)
    elif choice == '1':
        img = cv2.flip(img,1)
    elif choice == '2':
        img = cv2.flip(img,-1)
    else:
        pass

    cv2.imwrite(abs,img)
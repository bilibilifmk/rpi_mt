import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,320) # set Width
cap.set(4,240) # set Height

while True:
    ret, img = cap.read()
    # img = cv2.flip(img, -1) #180°旋转加镜像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5
        ,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        

    cv2.imshow('人脸追踪',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # 按esc 退出
        break

cap.release()
cv2.destroyAllWindows()

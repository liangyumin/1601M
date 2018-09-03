import numpy as np
import cv2
import os

# os.chdir(r'F:\飞秋\MV')
# cap=cv2.VideoCapture('少女时代 - You Think.mp4')
cap=cv2.VideoCapture('output.avi')
while (cap.isOpened()):
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.imshow('frame',gray)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()
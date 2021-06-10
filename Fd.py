# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:07:48 2020

@author: india
"""

import cv2

face_cascade=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('./haarcascade_eye.xml')

cap=cv2.VideoCapture(0)
while True:
    ret,image=cap.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),4)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=image[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.circle(roi_color,(ex+int(ew/2),ey+int(eh/2)),int(ew/2),(0,0,255),2)
          
        cv2.imshow('img',image)
        k=cv2.waitKey(30)& 0xff
        if k==27:
            break
cap.release()
cap.destroyAllWindows()
    
 
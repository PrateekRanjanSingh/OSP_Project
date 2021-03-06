import cv2,os
import numpy as np
from PIL import Image 
import pickle

def detect():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "Classifiers/face.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    path = 'dataSet'

    cam = cv2.VideoCapture(0)
    #font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
            print nbr_predicted
            if(nbr_predicted in range(0,11)):
                 nbr_predicted='Prateek'
            elif(nbr_predicted in range(11,22)):
                 nbr_predicted='Saurav'
            cv2.putText(im,str(nbr_predicted)+"--"+str(conf), (x,y+h),font,1.0, (255, 255, 255), lineType=cv2.LINE_AA) #Draw the text
            cv2.imshow('im',im)
            cv2.waitKey(10)
    cam.release()
    cv2.destroyAllWindows()










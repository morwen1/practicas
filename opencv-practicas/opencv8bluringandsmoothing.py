import cv2 
import numpy as np 


cap = cv2.VideoCapture(0)

while True:
    _,  frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #hsv Value  

    # color in HSV
    
    lower_red = np.array(cv2.cvtColor(np.uint8([[[172,57,50]]]),cv2.COLOR_RGB2HSV))
    upper_red = np.array(cv2.cvtColor(np.uint8([[[255,136,129]]]),cv2.COLOR_BGR2HSV))
  
    mask = cv2.inRange(hsv,lower_red,upper_red)  
    res = cv2.bitwise_and(frame, frame , mask = mask)
    
    
    median = cv2.medianBlur(res,15)
    bilateral = cv2.bilateralFilter(res,15,75,75)


    kernel = np.ones((15,15),np.float32)/255
    smooted = cv2.filter2D(res ,-1,kernel)

    cv2.imshow('frame',frame)
    cv2.imshow('blur', median)
    cv2.imshow('smooted', smooted)
    cv2.imshow('bilateral',bilateral)


    cv2.imshow('res',res)
    cv2.imshow("mas",mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27 :
        break

cv2.destroyAllWindows()
cap.release()
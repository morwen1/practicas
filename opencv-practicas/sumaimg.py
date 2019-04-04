import cv2 
import numpy 


img = cv2.imread("recurso/globovision.jpg")
salida= 0 
for i in range (200):
    salida += img
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
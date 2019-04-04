import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

#cargar un a imagen 
ruta = "recurso/"
#img = cv2.imread(ruta de la imagen)
img = cv2.imread(ruta +"/yop.jpg",cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1 
#IMREAD_UNCHANGED= -1 
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('yogris.png', img)
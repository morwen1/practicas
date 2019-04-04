
import cv2


ruta = "recurso/"
img = cv2.imread(ruta + 'yop.jpg' ,cv2.IMREAD_COLOR)

cv2.line(img ,(0,0) , (200,150), (200,0,0), 3 )
cv2.rectangle(img , (15,15) ,(200,150), (200,0,0),5)
cv2.circle(img ,(100,63), 55 , (200,0,0) -1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

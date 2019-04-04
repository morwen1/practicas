import cv2 
import numpy as np 
import matplotlib.pyplot as plt 


img = cv2.imread("recurso/my_photo-6.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

background = np.zeros ((1,65), np.float64)
front  = np.zeros((1,65),np.float64)


rect = (5,2,459,479)

cv2.grabCut(img,mask,rect,background,front,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==1),0,1).astype('uint8')

img= img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
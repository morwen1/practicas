import cv2 
import numpy as  np 
import matplotlib.pyplot as plt 



img1 = cv2.imread('recurso/my_photo-6.jpg')
img2 = cv2.imread('recurso/my_photo-2.jpg')


mask = np.zeros(img2.shape[:2], np.uint8)
print(img2.shape[:2])

background = np.zeros ((1,65), np.float64)
front  = np.zeros((1,65),np.float64)


rect = (2,2,640,480)

cv2.grabCut(img2,mask,rect,background,front,6,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==1),0,1).astype('uint8')

img2= img2*mask2[:,:,np.newaxis]
#img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
#keypoints ,

kp1 , des1 = orb.detectAndCompute(img1,None)
kp2 , des2 = orb.detectAndCompute(img2,None)
print(des2)


bf = cv2.BFMatcher(cv2.NORM_HAMMING2 , crossCheck = True)

matches = bf.match(des1,des2)
matches= sorted(matches,key=lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1 , img2 , kp2 ,matches[:10], None,flags = 2)


plt.imshow(img3)
plt.show()
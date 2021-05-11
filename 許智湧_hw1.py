import cv2
import numpy as np
cv2.namedWindow("showhw1")
cv2.namedWindow("hw1")
img =cv2.imread("d:\\pme22_project\\opencv-Training\\hw1\\Bird.tif")
c = 255/(np.arctan((np.max(img)-128)/32))
transformed = c * np.arctan((img-128)/32)
transformed = np.array(transformed, dtype = np.uint8)
cv2.imwrite("hw_1_tranformed.jpg", transformed)
cv2.imshow("showhw1", img)
cv2.imshow("hw1", transformed)
cv2.waitKey(0)
import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt







img = cv2.imread("ok.png", 0)

blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
blank_image[0:img.shape[0], 0:img.shape[1]] = 0, 0, 0


_, thresh = cv2.threshold(img, 24, 255, 0)


contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)


liste_x = []
liste_y = []

for x in range(thresh.shape[0]):
    for y in range(thresh.shape[1]):

        blank_image[x, y] = thresh[x, y]
        
        if thresh[x, y] == 255:
            
            blank_image[x + 1, y] = 0, 0, 255
            blank_image[x + 2, y] = 0, 0, 255
            blank_image[x - 1, y] = 0, 0, 255
            blank_image[x - 2, y] = 0, 0, 255

            blank_image[x, y - 1] = 0, 0, 255
            blank_image[x, y - 2] = 0, 0, 255
            blank_image[x, y + 1] = 0, 0, 255
            blank_image[x, y + 2] = 0, 0, 255

            blank_image[x - 1, y - 1] = 0, 0, 255
            blank_image[x + 1, y + 1] = 0, 0, 255
            blank_image[x - 1, y + 1] = 0, 0, 255
            blank_image[x + 1, y - 1] = 0, 0, 255
            
            liste_x.append(x)
            liste_y.append(y)




            blank_image[x, y] = 0, 0, 255

            cv2.imshow("blank_image.png", blank_image)
            cv2.imshow("thresh.png", thresh)
            cv2.waitKey(0)
    






##for x in range(thresh.shape[0]):
##    for y in range(thresh.shape[1]):
##    ##im = Image.open("ok.png")
##    ##im.rotate(90).show()





















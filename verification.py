import os
import cv2
import numpy as np
import matplotlib.pyplot as plt



from main_function import main_color


liste = os.listdir(r"C:\Users\jeanbaptiste\Desktop\resolveur de captchat\picture")
liste_result = os.listdir(r"C:\Users\jeanbaptiste\Desktop\resolveur de captchat\result1")
path = "result1\{}"

c = 0
nonetype = []
for i in liste_result:
    number_black = 0
    img = cv2.imread(path.format(i), 0)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x, y] != 0:
                number_black += 1

    print(c, number_black)
    if number_black == 0:
        nonetype.append(c)


    _, thresh = cv2.threshold(img, 100, 255, 0)
    cv2.imshow("thresh.png", thresh)
    cv2.waitKey(0)

    
    c+=1


print(nonetype)

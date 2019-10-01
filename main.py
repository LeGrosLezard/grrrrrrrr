import joblib,cv2
import numpy as np
import os

import operator
from PIL import Image
from collections import defaultdict


def switch_background(img):

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j][0] == 0 and\
               img[i, j][0] == 0 and\
               img[i, j][0] == 0:
                img[i, j] = 255, 255, 255
    return img



def main_color(image):
    dico = {}

    im = Image.fromarray(image)
    for value in im.getdata():
        if value in dico.keys():
            dico[value] += 1
        else:
            dico[value] = 1

    max_value = 0
    color = []
    for key, value in dico.items():
        if value > max_value:
            max_value = value
            color = key

    liste = []
    for key, value in dico.items():
        if value > 100:
            liste.append(key)


    return color, liste




model = joblib.load("models/captchat_recognition")


for i in range(0, 9):
    
    liste = os.listdir(r"C:\Users\jeanbaptiste\Desktop\resolveur de captchat\picture\train\{}".format(str(i)))
    path = "picture/train/{}/{}"

    for im in liste:

        img = cv2.imread(path.format(str(i), im))

        background_picture, colors = main_color(img)

        if background_picture == (0, 0, 0):
            img = switch_background(img)


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        thresh = cv2.resize(thresh, (28, 28))

        cv2.imwrite("treatment.png", thresh)

        rows, cols = thresh.shape


        def to_list(thresh):

            data = []
            for i in range(thresh.shape[0]):
                for j in range(thresh.shape[1]):
                    if thresh[i, j] > 120:
                        nb = 1
                    else:
                        nb = 0
                
                    data.append(nb)

            return data


        X = to_list(thresh)

        predictions = model.predict([X])      
        print("Prediction: ", predictions[0])

        cv2.imshow("image", thresh)
        cv2.waitKey(0)

















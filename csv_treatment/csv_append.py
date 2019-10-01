import csv
import os


def csv_write():
    with open('../csv/test.csv', 'w') as file:
        writer = csv.writer(file)
        file.write("label;")
        for i in range(0, 784):
            file.write("pixel"+str(i)+";")

        file.write("\n")


import cv2
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


def reshape_thresh(thresh):
    thresh = cv2.resize(thresh, (28, 28))
    return thresh


def data_treatment(number, label):

    path_list = r"C:\Users\jeanbaptiste\Desktop\resolveur de captchat\picture\train\{}" 
    liste = os.listdir(path_list.format(number))
    path = "../picture/train/{}/{}"


    for i in liste:
        print(path.format(number, i))
        img = cv2.imread(path.format(number, i))

        background_picture, colors = main_color(img)

        if background_picture == (0, 0, 0):
            img = switch_background(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 120, 255, 0)
        thresh = reshape_thresh(thresh)

##        cv2.imshow("image", thresh)
##        cv2.waitKey(0)


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


        data = to_list(thresh)
        print(data)


        def write_data_into_csv(data, label):

            with open('../csv/test.csv', 'a') as file:
                writer = csv.writer(file)
                file.write(label+";")
                for i in data:
                    file.write(str(i)+";")
  
                file.write("\n")
 
        write_data_into_csv(data, label)


csv_write()

for i in range(0, 10):
    print(i)
    data_treatment(str(i), str(i))







































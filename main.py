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




def img_to_thresh(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    return thresh

def reshape_tresh(thresh):

    thresh = cv2.resize(thresh, (28, 28))
    return thresh



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

def prediction(thresh):
    thresh = reshape_tresh(thresh)
    rows, cols = thresh.shape

    X = to_list(thresh)

    predictions = model.predict([X])      
    print("PREDICTION: ", predictions[0])

    cv2.imshow("image", thresh)
    cv2.waitKey(0)







model = joblib.load("models/captchat_recognition")

liste = os.listdir(r"C:\Users\jeanbaptiste\Desktop\resolveur de captchat\picture")
print(liste)
path = "picture/{}"

for element in liste:
    if element == "train":
        pass
    else:

        img = cv2.imread(path.format(element))


        def replace_background(img):
            background_picture, colors = main_color(img)

            if background_picture == (0, 0, 0):
                img = switch_background(img)

            return img, colors

        
        img, colors = replace_background(img)
        for i in colors:
            if i == (0,0,0) or i == (255, 255, 255):
                colors.remove(i)

        def croping_y_picture(img):

            y1 = int(img.shape[0] /6.5)
            crop = img[y1:img.shape[0]-50, 200:img.shape[1]-150]

            return crop

        img = croping_y_picture(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, 0)

        cv2.imshow("image", thresh)
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



        def create_blank(img):
            blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
            blank_image[0:img.shape[0], 0:img.shape[1]] = 0, 0, 0
            return blank_image


        blank_image = create_blank(img)

        for pos1 in range(img.shape[0]):
            for pos2 in range(img.shape[1]):
                for coul in colors:
                    if img[pos1, pos2][0] == coul[0] and\
                        img[pos1, pos2][1] == coul[1] and\
                        img[pos1, pos2][2] == coul[2]:
                        blank_image[pos1, pos2] = 255, 255, 255


        gray = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
        _, thresh_blanck = cv2.threshold(gray, 200, 255, 0)

        cv2.imshow("thresh_blanck", thresh_blanck)
        cv2.waitKey(0)

        contours, _ = cv2.findContours(thresh_blanck, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

        for i in contours:
            if cv2.contourArea(i) > 0.0:
            
                x,y,w,h = cv2.boundingRect(i)
                detection = thresh[y-5:y+h+5, x-5:x+w+5]
                try:
                    cv2.imshow("detection", detection)
                    cv2.waitKey(0)
                except:
                    pass












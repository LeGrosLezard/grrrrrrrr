import joblib, cv2
import numpy as np
import os

import operator
from PIL import Image
from collections import defaultdict

from main_function import detect_operande_cap



def switch_background(img):
    """if color of background is black:
    we transform it into white background"""

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j][0] == 0 and\
               img[i, j][0] == 0 and\
               img[i, j][0] == 0:
                img[i, j] = 255, 255, 255
    return img



def main_color(image):
    """We recup the main colors
    of the picture like the background
    or the lines or numbers colors"""

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
    """Binarisation of the picture"""

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

    return thresh



def reshape_tresh(thresh):
    """Reshape the thresh picture for
    it corresponding with our model who's 28*28"""

    thresh = cv2.resize(thresh, (28, 28))
    return thresh


def to_list(thresh):
    """transform our picture to 0/1
    byscal better ? uint8/16"""

    data = []
    for i in range(thresh.shape[0]):
        for j in range(thresh.shape[1]):
            if thresh[i, j] > 120:
                nb = 1
            else:
                nb = 0
        
            data.append(nb)

    return data


def prediction(thresh, model):
    """Call prediction with last operation
    of reshape and flatted"""

    thresh = reshape_tresh(thresh)
    rows, cols = thresh.shape

    X = to_list(thresh)

    predictions = model.predict([X])


    if predictions[0] == "a":
        print("PREDICTION ligne")
    elif predictions[0] == "b":
        print("PREDICTION interro")
    elif predictions[0] == "c":
        print("PREDICTION multiplication")
    elif predictions[0] == "d":
        print("PREDICTION addition")
    else:
        print("PREDICTION ", predictions[0])

    return predictions[0]

    cv2.imshow("image", thresh)
    cv2.waitKey(0)



def create_blank(img):
    """Create a empty white picture
    for a futur mask and for del lines"""

    blank_image = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
    blank_image[0:img.shape[0], 0:img.shape[1]] = 0, 0, 0
    return blank_image



def replace_background(img):
    """Transform black to white background"""

    background_picture, colors = main_color(img)

    if background_picture == (0, 0, 0):
        img = switch_background(img)

    return img, colors


def croping_y_picture(img):
    """We croping picture for have only the numbers"""

    y1 = int(img.shape[0] /6.5)
    crop = img[y1:img.shape[0]-50, 200:img.shape[1]-150]

    return crop



def main():
    """Lunch and call all last functions"""

    #Our model
    model = joblib.load("models/captchat_recognitionV2")

    #Path of pictures
    liste = os.listdir(r"C:\Users\jeanbaptiste\Desktop\resolveur de captchat\picture")
    path = "picture/{}"


    for element in liste:
        #Folder of train picture
        if element == "train":
            pass
        else:
            #read picture
            img = cv2.imread(path.format(element))

            #replace background
            img, colors = replace_background(img)
            for i in colors:
                if i == (0,0,0) or i == (255, 255, 255):
                    colors.remove(i)

            #croping picture to threshold
            img = croping_y_picture(img)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 150, 255, 0)

##            cv2.imshow("image", thresh)
            cv2.imshow("img", img)
            cv2.waitKey(0)


            #Create black picture
            blank_image = create_blank(img)

            #Recup main colors for create a mask and del lines
            for pos1 in range(img.shape[0]):
                for pos2 in range(img.shape[1]):
                    for coul in colors:
                        if img[pos1, pos2][0] == coul[0] and\
                            img[pos1, pos2][1] == coul[1] and\
                            img[pos1, pos2][2] == coul[2]:
                            blank_image[pos1, pos2] = 255, 255, 255

            #thresholding the mask
            gray = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
            _, thresh_blanck = cv2.threshold(gray, 200, 255, 0)

##            cv2.imshow("thresh_blanck", thresh_blanck)
##            cv2.waitKey(0)


            #find contour in the mask (with that we recup number position)
            contours, _ = cv2.findContours(thresh_blanck, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)


            liste_X = []
            liste_Y = []
            liste_W = []
            liste_H = []
            
            liste_P = []

            #Remove noise
            for i in contours:
                if cv2.contourArea(i) > 1.0:

                    #recup area into a rectangle
                    x, y, w, h = cv2.boundingRect(i)
                    detection = thresh[y-6:y+h+6, x-6:x+w+4]
                    detection1 = img[y-6:y+h+6, x-6:x+w+4]

                    try:
                        #predict the current area
                        predicting = prediction(detection, model)
                        #recup this predict into a rectangle
                        liste_X.append(x)
                        liste_Y.append(y)
                        liste_W.append(x+w)
                        liste_H.append(y+h)
                        liste_P.append(predicting)
                    except:
                        pass
            #treating data for the current position of detections
            out = detect_operande_cap(liste_X,
                                      liste_Y,
                                      liste_W,
                                      liste_H,
                                      liste_P)



if __name__ == "__main__":
    main()







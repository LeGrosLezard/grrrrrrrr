import operator
from PIL import Image
from collections import defaultdict



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
            

    a = sorted(dico.items(), key=lambda t: t[1])



    liste = []
    for i in a:
        if i[1] > 100:
            liste.append(i)


    return color, liste





















































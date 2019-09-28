from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plt
import cv2
import numpy as np

def data():
    digits = datasets.load_digits()
    clf = svm.SVC(gamma=0.0001, C=100)

    x,y = digits.data[:-1], digits.target[:-1]
    clf.fit(x,y)

    return clf


def treatment_picture_threshold(contour):


    img = cv2.imread("treatment.png", 0);img = cv2.resize(img, (34, 64))

    #len(contour)
    if contour <= 60:
        _, thresh = cv2.threshold(img, 120, 255, 0)
    else:
        _, thresh = cv2.threshold(img, 200, 255, 0)

    cv2.imwrite("test.png", thresh)
    cv2.imshow("crop", thresh)
    cv2.waitKey(0)


def treatment_picture_to_dataset_form():

    img1 = cv2.imread("test.png", 0);img1 = cv2.resize(img1, (8, 8))
    img = img1.astype("float64")
    print(type(img))
    print(img)

    img16 = []
    liste_w = []
    for i in img:
        for j in i:
            j = int(j/16); j = float(j)
            img16.append(j)

    img16 = np.array(img16, dtype=np.float32)
    img16 = img16.reshape(1, -1)
    print(img16)

    return img16, img1


def main(contour):
    clf = data()
    treatment_picture_threshold(contour)
    img16, img1 = treatment_picture_to_dataset_form()

    print('Prediction:',clf.predict(img16))
    plt.imshow(img1, cmap="gray")
    plt.show()

    return clf.predict(img16)[0]



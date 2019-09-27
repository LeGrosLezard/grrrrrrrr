import cv2
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.0001, C=100)
print(len(digits.data))


x, y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)


plt.imshow(digits.images[-2], cmap="gray")
plt.show()
print("pred", clf.predict(digits.data[-2].reshape(1, -1)))

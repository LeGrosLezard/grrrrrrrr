import joblib,cv2
import numpy as np

model = joblib.load("svm_6label_linear_1_0")



img = cv2.imread("treatment.png", 0)
_, thresh = cv2.threshold(img, 80, 255, 0)
thresh = cv2.resize(thresh, (28, 28), interpolation=cv2.INTER_AREA)
cv2.imshow("daz", thresh)
rows,cols = thresh.shape

X=[]
for i in range(rows):
    for j in range(cols):
        k = thresh[i,j]
        if k>100:
            k=1
        else: 
            k=0	
        X.append(k)


predictions = model.predict([X])   
print(predictions[0])





import cv2
import numpy as np

a = [146, 140, 99, 43, 13, 85, 100, 77, 127, 137, 73, 77, 64, 27, 15, 120, 110, 81, 71, 42, 32, 64, 76, 77, 64, 15, 76] 
b = [160, 159, 152, 143, 120, 115, 114, 113, 111, 109, 105, 95, 95, 95, 95, 82, 82, 81, 81, 80, 80, 77, 73, 66, 66, 66, 44] 
c = [150, 145, 104, 48, 23, 95, 109, 84, 132, 150, 84, 84, 72, 35, 22, 138, 115, 99, 78, 60, 41, 72, 84, 83, 68, 22, 84] 
d = [162, 162, 155, 146, 122, 117, 116, 121, 113, 112, 108, 97, 97, 97, 97, 84, 84, 83, 83, 82, 82, 79, 79, 72, 75, 75, 57] 
e = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'd', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '1', '5', '5', '1', 'c', '5']



##a = [103, 19, 19, 85, 82, 44, 32, 56, 82, 34, 79, 18, 110, 124, 83, 68, 80, 68, 79, 68, 81, 67, 24, 65, 92] 
##b = [150, 112, 108, 106, 103, 87, 87, 86, 85, 70, 66, 65, 63, 62, 61, 60, 57, 57, 40, 40, 34, 34, 34, 29, 23] 
##c = [123, 29, 29, 89, 88, 51, 39, 64, 88, 39, 88, 27, 114, 127, 88, 75, 87, 73, 87, 74, 87, 75, 28, 69, 104] 
##d = [152, 114, 110, 111, 107, 89, 89, 88, 87, 72, 70, 69, 65, 64, 65, 67, 60, 61, 47, 43, 39, 38, 36, 31, 27] 
##e = ['a', 'a', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'a', '3', 'd', 'a', 'a', '3', '8', '3', '8', '3', '9', '3', '9', 'a', 'a', 'a']




blank_image = np.zeros((200,200,3), np.uint8)
blank_image[0:200, 0:200] = 255, 255, 255

blank_image2 = np.zeros((200,200,3), np.uint8)
blank_image2[0:200, 0:200] = 255, 255, 255

a = a[:len(e)]
b = b[:len(e)]
c = c[:len(e)]
d = d[:len(e)]

for i in range(len(c)):
    if e[i] == "c":
        e[i] = "multiplication"
    elif e[i] == "d":
        e[i] =  "addition"



sing = []
position = []
for i in range(10):
    position.append([])

for i in range(len(e)):
    if e[i] == "a" or e[i] == "b":
        pass
    elif e[i] == "multiplication" or e[i] == "addition":
        sing.append([b[i],d[i], a[i],c[i], e[i]])

    else:
        position[int(e[i])].append([b[i], a[i], d[i], c[i]])



for i in range(10):
    count = 0
    for i in position:
        if i == []:
            pass
        else:
            print(count)
            for j in range(len(i)):
                try:
                    print(i[j])
                    if abs(i[j+1][0] - i[j][0]) < 15:
                        del i[j]
                except:
                    pass
        print("")

        count += 1



count = 0
for i in position:
    if i == []:
        pass
    else:
        for j in i:
            print(j, count)
    count += 1



















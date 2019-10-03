import cv2
import numpy as np


#---------------------------In case of bug and for work we save this data list

##a = [146, 140, 99, 43, 13, 85, 100, 77, 127, 137, 73, 77, 64, 27, 15, 120, 110, 81, 71, 42, 32, 64, 76, 77, 64, 15, 76] 
##b = [160, 159, 152, 143, 120, 115, 114, 113, 111, 109, 105, 95, 95, 95, 95, 82, 82, 81, 81, 80, 80, 77, 73, 66, 66, 66, 44] 
##c = [150, 145, 104, 48, 23, 95, 109, 84, 132, 150, 84, 84, 72, 35, 22, 138, 115, 99, 78, 60, 41, 72, 84, 83, 68, 22, 84] 
##d = [162, 162, 155, 146, 122, 117, 116, 121, 113, 112, 108, 97, 97, 97, 97, 84, 84, 83, 83, 82, 82, 79, 79, 72, 75, 75, 57] 
##e = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'd', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '1', '5', '5', '1', 'c', '5']


##a = [103, 19, 19, 85, 82, 44, 32, 56, 82, 34, 79, 18, 110, 124, 83, 68, 80, 68, 79, 68, 81, 67, 24, 65, 92] 
##b = [150, 112, 108, 106, 103, 87, 87, 86, 85, 70, 66, 65, 63, 62, 61, 60, 57, 57, 40, 40, 34, 34, 34, 29, 23] 
##c = [123, 29, 29, 89, 88, 51, 39, 64, 88, 39, 88, 27, 114, 127, 88, 75, 87, 73, 87, 74, 87, 75, 28, 69, 104] 
##d = [152, 114, 110, 111, 107, 89, 89, 88, 87, 72, 70, 69, 65, 64, 65, 67, 60, 61, 47, 43, 39, 38, 36, 31, 27] 
##e = ['a', 'a', 'a', 'b', 'b', 'a', 'a', 'a', 'a', 'a', '3', 'd', 'a', 'a', '3', '8', '3', '8', '3', '9', '3', '9', 'a', 'a', 'a']


##a = [139, 73, 19, 10, 85, 64, 54, 30, 41, 19, 89, 52, 32, 100, 96, 111, 129, 144, 140, 80, 68, 68, 68, 68, 79, 67] 
##b = [118, 113, 112, 108, 106, 100, 99, 90, 87, 87, 86, 86, 86, 85, 85, 84, 83, 82, 82, 57, 57, 63, 58, 38, 34, 34] 
##c = [142, 79, 29, 16, 89, 68, 58, 33, 51, 29, 92, 63, 40, 106, 99, 117, 136, 150, 143, 87, 76, 76, 75, 75, 87, 74] 
##d = [120, 115, 114, 111, 111, 102, 101, 92, 91, 92, 88, 92, 91, 87, 87, 86, 85, 84, 84, 65, 70, 69, 63, 47, 47, 36] 
##e = ['a', 'a', 'a', 'a', '2', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '7', '8', '8', '8', '5', '2', '5']


##a = [26, 19, 82, 44, 19, 69, 56, 81, 126, 54, 38, 24, 21, 77, 80, 68, 79, 67] 
##b = [112, 112, 103, 87, 87, 86, 86, 85, 73, 71, 71, 70, 65, 61, 63, 57, 34, 34] 
##c = [29, 24, 89, 51, 27, 76, 64, 86, 144, 61, 47, 29, 26, 94, 88, 75, 87, 75] 
##d = [114, 114, 111, 89, 89, 88, 88, 87, 75, 73, 73, 72, 67, 74, 69, 66, 44, 47] 
##e = ['a', 'a', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', '8', '8', '2', '4', '3']




def resize_list(a, b, c, d, e):
    """Sometimes there are bug with an empty threshold
    so we resize all list in function of prediction list"""

    a = a[:len(e)] #X
    b = b[:len(e)] #Y
    c = c[:len(e)] #X+W
    d = d[:len(e)] #Y+H

    #Transform label a, b, c , d to real label
    for i in range(len(c)):
        if e[i] == "c":
            e[i] = "multiplication"
        elif e[i] == "d":
            e[i] =  "addition"


    return a, b, c, d, e


def put_points_on_list(a, b, c, d, e):
    """We recup signs and number into a list of list in range 11
    0-9 for numbers to 0 to 9 and the 10 for sign"""

    sign = []
    position = []
    for i in range(11):
        position.append([])

    for i in range(len(e)):
        if e[i] == "a" or e[i] == "b":
            pass
        elif e[i] == "multiplication" or e[i] == "addition":
            sign.append([b[i],d[i], a[i],c[i], e[i]])

        else:
            try:
                e[i] = int(e[i])
                position[int(e[i])].append([b[i], a[i], d[i], c[i]])
            except:
                pass


    return position, sign



def got_a_visual(position):
    """Got a visual of the last list"""

    for c, i in enumerate(position):
        print(i, c)
        print("")

    print("")



def constituate_mean(position):
    """We make a mean because some detection are
    to far of our 4/5 positions we want (numbers and signs)
    5*15 or 50*15 or 15*5 for example"""

    count = 0
    mean = 0
    for i in position:
        if i  != []:
            for j in i:
                mean += j[0]
                count += 1

    return mean, count

    
def clear_points_so_far_by_mean(mean, position, count):
    """We clear points to far a 1 detected
    on the top corner right
    is impossible so we delete this detection"""

    mean = int(mean / count)
    for i in position:
        if i  == []:
            pass
        else:
            for j in i:
                print(j[0], mean)
                if j[0] > mean + 25 or\
                   j[0] < mean - 25:
                    i.remove(j)
        
    return position
    


def del_doublon(position):
    """Our database is constituate
    of half one for example so we can
    have multiple detections"""

    for i in position:
        if len(i) > 1:
            for j in i:
                for k in i:
                    if abs(j[0] - k[0]) == 0:
                        pass
                    elif abs(j[0] - k[0]) < 15:
                        try:
                            i.remove(j)
                        except:
                            pass
    return position



def define_operand(sign, position):
    """We can got multipl sign so we choice one
    by his position gg data analysis"""

    stop = False
    for s in sign:
        for i in position:
            for j in i:
                if abs(s[0] - j[0]) < 10:
                    position[-1].append(s[-1])
                    stop = True
            if stop is True:
                break

    if stop is False:
        position[-1].append("soustraction")


    return position



def take_x_pos_for_define_the_4_pts(position):
    """We recup only the x of the last points
    detected"""

    x = []
    count = 0
    for i in position:
        if i == []:
            pass
        else:
            for j in i:
                print(j, count)
                try:
                    j[0] = int(j[0])
                    if j[0] == int(j[0]):
                        x.append(j[0])
                except ValueError:
                    pass

        count += 1

    return x



def top_bot_points(x):
    """We placing top and bot X points numbers"""

    top = []
    bot = []

    if len(x) == 4:
        for i in range(2):
            bot.append(max(x))
            x.remove(max(x))
        for i in x:
            top.append(i)


    maxi = 0
    count = 0
    if len(x) == 3:
        for i in x:
            if count == 0:
                maxi = i
            else:
                if i >= maxi:
                    maxi = i
       
            count += 1

        for i in x:
            if i < maxi - 15:
                top.append(i)
            else:
                bot.append(i)

    #print("top", top)
    #print("bot", bot)
    return top, bot



def top_bot_number(position, top, bot):
    """We recup all information about the last x
    x = 16 we recup all matrice where x = 16
    [x, y, w, h, prediction]"""

    final_top = []
    final_bot = []
    count = 0
    for i in position[:-1]:
        if i == []:
            pass
        else:
            for j in i:
                for k in top:
                    if j[0] == k:
                        final_bot.append([j, count])
                        break
                for l in bot:
                    if j[0] == l:
                        final_top.append([j, count])
                        break
        count += 1




    #print(final_bot) 
    #print(final_top)

    return final_bot, final_top





def final_position(final_bot, final_top, position):
    """We place the points to right or left"""

    left_top = ""
    right_top = ""

    left_bot = ""
    right_bot = ""


    if len(final_bot) == 2:
        if final_bot[0][0][1] < final_bot[1][0][1]:
            left_top = final_bot[0][1]
            right_top = final_bot[1][1]
        else:
            left_top = final_bot[1][1]
            right_top = final_bot[0][1]

    if len(final_bot) == 1:
        right_top = final_bot[0][1]


    if len(final_top) == 2:
        if final_top[0][0][1] < final_top[1][0][1]:
            left_bot = final_top[0][1]
            right_bot = final_top[1][1]
        else:
            left_bot = final_top[1][1]
            right_bot = final_top[0][1]

    if len(final_top) == 1:
        right_bot = final_bot[0][1]


    a = int(str(left_top)+ str(right_top))
    b = int(str(left_bot)+ str(right_bot))

    print(a, position[-1][0], b)

    out = 0
    if position[-1][0] == "soustraction":
        out = int(a) - int(b)
    elif position[-1][0] == "multiplication":
        out = int(a) * int(b)
    elif position[-1][0] == "addition":
        out = int(a) + int(b)

    print(out)
    return out


def detect_operande_cap(a, b, c, d , e):
    """Call all last function"""

    a, b, c, d, e = resize_list(a, b, c, d, e)
    position, sign = put_points_on_list(a, b, c, d, e)
    #got_a_visual(position)
    mean, count = constituate_mean(position)
    position = clear_points_so_far_by_mean(mean, position, count)
    position = del_doublon(position)
    position = define_operand(sign, position)
    x = take_x_pos_for_define_the_4_pts(position)
    top, bot = top_bot_points(x)
    final_bot, final_top = top_bot_number(position, top, bot)
    out = final_position(final_bot, final_top, position)

    return out


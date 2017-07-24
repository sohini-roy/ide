T = int(input())

for i in range(0,T):
    x11, y11, x12, y12 = input().split()
    x21, y21, x22, y22 = input().split()
    y = "no"
    #no 2nd snake
    if(((x11+x12+y11+y12) == 0) or ((x21+x22+y21+y22) == 0)):
        y = "yes"
    else:
        #any one of the co-ordinates overlap
        if((x11==x21 and y11==y21) or (x11==x22 and y11==y22) or (x12==x21 and y12==y21) or (x12==x22 and y12==y22)):
            y="yes"
        else :
            if(y11==y12):
                if(y21==y22) and (y21==y11):
                    #both snakes horizontal
                    if(x11 < x12):
                        if((x11 < x21 < x12) or (x11 < x22 < x12)):
                            y = "yes"
                        else:
                            y="no"
                    else:
                        if((x12 < x21 < x11) or (x12 < x22 < x11)):
                            y = "yes"
                        else:
                            y="no"
                else:
                    y="no"
            #1st snake vertical
            if(x11==x12):
                if(x22==x21 and x12==x22):
                    #both snakes vertical
                    if(y11 < y12):
                        if((y11 < y21 < y12) or (y11 < y22 < y12)):
                            y = "yes"
                        else:
                            y="no"
                    else:
                        if((y12 < y21 < y11) or (y12 < y22 < y11)):
                            y = "yes"
                        else:
                            y="no"
                else:
                    y="no"
    print(y)

T = int(input())

for i in range(0,T):
    x11, y11, x12, y12 = input().split()
    x21, y21, x22, y22 = input().split()
    y = ""
    x1 = 0
    x2 = 0

    if y11==y12==y21==y22:
        if x11>x12:
            x1=x11
        else:
            x1=x12

        if x21>x22:
            x2=x21
        else:
            x2=x22

        if int(x1)-int(x2)>0:
            y = "yes"
        else:
            y = "no"

    if x21==x22:
        if x21==x11 or x21==x12:
            y = "yes"
        else:
            y = "no"

    if x11==x12:
        if x11==x21 or x11==x22:
            y = "yes"
        else:
            y = "no"

    if y=="yes":
        print ("yes")
    else:
        print ("no")

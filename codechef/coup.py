t = int(input())

for test in range(t):
    n = int(input())
    matrix = []
    matrix.append(str(input()))
    matrix.append(str(input()))
    hori = 0
    verti = 0
    upnoise = False
    downnoise = False
    if matrix[0].count('*') > 0 and matrix[1].count('*') > 0:
        hori = 1
    for i in range(n):
        if matrix[0][i] == '*':

            if upnoise:
                verti += 1
                upnoise = False
                downnoise = False
            upnoise = True

        if matrix[1][i] == '*':
            if downnoise:
                verti += 1
                if not matrix[0][i] == '*':
                    upnoise = False
            downnoise = True
    print(verti+hori)
    # print('--------------------------------')
    # print(" Hori " + str(hori))
    # print(" Veri " + str(verti))

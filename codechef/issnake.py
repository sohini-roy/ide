T = int(input());

def ignore(i, k):
    if(k==1):
        if(row1[++i]=='.'):
            ignore(i, k);
        else:
            return i;
    else:
        if(row2[++i]=='.'):
            ignore(i, k);
        else:
            return i;


def nextpart(i, j, k):
    if(k==1):
        if(j==i and row2[j]=='#'):
            return 2;
        else:
            if(row1[++i]=='#'):
                return 1;
            else:
                return 0;
    else:
        if(i==j and row1[i]=='#'):
            return 1;
        else:
            if(row2[++j]=='#'):
                return 2;
            else:
                return 0;

for i in range(0,T):
    n = int(input());
    row1 = input();
    row2 = input();
    lastindexrow1 = row1.rfind('#')
    lastindexrow2 = row2.rfind('#')
    length = len(list(row1));
    i = j = 0;
    i = ignore(i, 1);
    j = ignore(j, 2);
    if(j < i):
        k=2;
        for(j; j<length;):
            nextstep = nextpart(i, j, k);
            if(nextstep == 1):
                j++;i++;
                k=1;
            else:
                if(nextstep == 2):
                    j++;
                else:
                    if(lastindexrow1 > i or lastindexrow2 > j):
                        print('no');
    else:
        if(i < j):
            k=1;
            for(i; i<length;):
                nextstep = nextpart(i, j, k);
                if(nextstep == 2):
                    j++;i++;
                    k=1;
                else:
                    if(nextstep == 1):
                        i++;
                    else:
                        if(lastindexrow1 > i or lastindexrow2 > j):
                            print('no');

s = input().strip();
l = len(s);

def reduce(s, l):
    flag = 0;
    for i in range(0, l):
        if s[i] == s[i+1]:
            flag = 1;
            j=i;i+=2;
            while(j<l):
                s[j].copy(s[i]);
                s[j+1].copy(s[i+1]);
                j+=2;
                l-=2;
                reduce(s, l);
        else:
            continue;
    if i==l and flag==0 :
        return s;

s = reduce(s, l);
if len(s):
    print(s);
else:
    print('empty string');

s = input().strip();

for i in range(0, len(s)):
    count=1;
    if ord(s[i]) > 65 and ord(s[i]) < 90:
        count +=1;
print(count);

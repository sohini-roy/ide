import re

def patternCount(s):
    # Complete this function
    matches = re.findall(r'(?=(10+1))', s)
    return len(matches)

q = int(input())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)

t = int(input());
result = [];

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

for i in range(0, t):
    n = int(input());
    a = list(map(int, input().strip().split(' ')));
    for i in range (o, n):
        x = a[i]
        if(is_prime(x)):
            if(!index(x)):
                result.appemd(a[i]);

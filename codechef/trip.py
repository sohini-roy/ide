mod = (10**9) + 7;

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

t = int(input());

for i in range (0,t):
     n = int(input());
     trip = factorial(n);
     ++trip;
     print(trip % mod);

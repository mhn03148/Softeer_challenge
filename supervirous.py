import sys
def power(a, n):
    if n == 0:
        return 1
    x = power(a, n//2)
    if n % 2 == 0:
        return x * x % 1000000007
    else:
        return x * x * a % 1000000007

k, p, n = map(int, input().split())
virous = (k*(power(p,10*n))) % 1000000007
print(virous)
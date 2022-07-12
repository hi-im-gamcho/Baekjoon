from math import gcd

a, b = map(int, input().split())

gcd = gcd(a, b)
print(gcd)
print(a*b//gcd)


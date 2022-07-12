def lcm(a,b):
    mul = a * b
    while b > 0:
        a,b = b, a%b
    return mul // a

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a,b))


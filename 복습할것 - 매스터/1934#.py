def lcm(a,b):
    mul = a * b
    while b > 0:
        a,b = b, a%b
    return mul // a

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lcm(a,b))

# 복습 시 함수를 한번 만들어볼것.
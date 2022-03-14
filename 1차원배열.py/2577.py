a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
list_mul = list(str(mul))

for i in range(0, 9+1):
    print(list_mul.count(str(i)))
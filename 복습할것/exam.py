a = input()         # 472
b = input()         # 385

list_a = list(a)
list_b = list(b)

for i in range (0, 2+1, 1):
    print(int(a) * int(list(b)[2-i]))
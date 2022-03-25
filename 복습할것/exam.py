N = n  = int(input())     # 26
count = 0

while True:
    ten = n//10                         # 2
    one = n%10                          # 6
    s = ten + one                       # 8
    count += 1
    new = int(str(one) + str(s%10))          # 68
    if new==N:
        break
print(count)
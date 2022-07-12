from math import factorial

N_factorial = factorial(int(input()))

cnt = 0
for i in str(N_factorial)[::-1]:
    if i != '0':
        break
    cnt += 1
print(cnt)

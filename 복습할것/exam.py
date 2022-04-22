n = int(input()) # 설탕   #18
# n = 5*a + 3*b

result = 0

while n >= 0:
    if n % 5 == 0:
        result += n // 5
        break
    else:
        n -= 3
        result += 1
else:
    print(-1)


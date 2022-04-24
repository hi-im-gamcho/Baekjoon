n = int(input())        # 설탕
# n = 5*a + 3*b

result = 0

while n >= 0:
    if n % 5 == 0:
        print(result)
        break
    else:
        result += 1
        n -= 3
else:
    print(-1)



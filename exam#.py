result = 1

for _ in range(3):
    result *= int(input())

result = list(str(result))

for i in range(0, 9+1):
    print(result.count(str(i)))

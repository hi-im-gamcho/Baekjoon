n = N = int(input())
count = 0

while True:
    ten = (n//10)
    one = (n%10)
    total = ten + one
    count += 1
    n = int(str(one) + str(total % 10))
    # total % 10 으로 해야 문제의 조건에 부합된다
    if N==n:
        break
print(count)

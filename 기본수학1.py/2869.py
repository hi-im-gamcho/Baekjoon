a,b,v = map(int, input().split())
# a = 올라가는 거리
# b = 내려가는 거리
# v = 막대 길이

day = 0
height = 0

while height < v:
    height += a
    day += 1

    if height >= v:
        break

    height -= b

print(day)

# 처음 이렇게 풀었는데 시간초과남.
# 2번째 풀이

a,b,v = map(int, input().split())
day = (v-a)/(a-b)+1

if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
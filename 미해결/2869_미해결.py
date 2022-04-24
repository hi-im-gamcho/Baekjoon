a, b, v = [int(x) for x in input().split()]
# a = 올라감
# b = 내려감
# v = 높이

day = 0

while True:
    if v > 0:
        v -= a
        day += 1
        if v <= 0:
            print(day)
            break
        v += b
    else:
        print(day)
        break
    
# 방법은 맞는데 v가 매우 클 경우 시간이 오래걸림 (100 99 1000000000)
# 이건 메모화로 해결해야 하는건가?




m, n = map(int, input().split())

for i in range(m, n+1):
    not_sosu = 0
    for x in range(2, i):
        if i % x == 0:
            not_sosu += 1
        if not_sosu != 0:
            break           # 조건을 만족하면 안쪽이 for 문을 빠져나감.
    if not_sosu == 0:
        print(i) 


# @@@@@@@@@@@@@@@@@@시간초과@@@@@@@@@@@@@@@@@@@@
# 다른사람들 보니까 import math 이용해서 math.sqrt()해서 제곱근 구해서 어찌저찌하던데
# 쓰읍...

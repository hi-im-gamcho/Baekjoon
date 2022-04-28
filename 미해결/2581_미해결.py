m = int(input())
n = int(input())    # m <= n

sosu = []

# M이상 N이하의 자연수 중 소수인 것을 모두 골라
# 이들 소수의 합과 최솟값을 찾는

for i in range(m, n+1):
    not_sosu = 0
    if i == 0:
        pass
    else:
        for x in range(2, i):   # 2 ~ i-1
            if i % x == 0:
                not_sosu += 1
        if not_sosu == 0:
            sosu.append(i)

if sosu == []:
    print("-1")
else:
    print(sum(sosu))
    print(min(sosu))

            

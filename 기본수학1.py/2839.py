n = int(input())    # kg

# n = (a * 5) + (b * 3) 가 되는 a,+의 최솟값을 구하라.

# 1. 분해되게하는 a와 b의 값을 구함
# 2. a+b의 최솟값을 구함.

result = 0              # 봉지 수
                            #17  14  11  8   5   
while n >= 0:
    if n % 5 == 0:
        result += n // 5 
        print(result)
        break
    else: 
        n -= 3
        result += 1         # 3kg 봉지 1개 추가.
else:
    print(-1)

        

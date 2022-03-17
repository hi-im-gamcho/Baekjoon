c = int(input())                    # 테스트 케이스

for i in range(1, c+1):
    n = list(map(int, input().split()))         # [5 50 50 70 80 100]
    sum_n = sum(n[1:])                          # 350
    avrg = sum_n / (len(n) - 1)                 # 70
    cnt = 0                 
    for score in n[1:]:
        if score > avrg:
            cnt +=1 
    result = cnt / n[0] * 100
    print(f"{result:.3f}%") 
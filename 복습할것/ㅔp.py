n = int(input())                    # 5

for i in range(1, n+1):             # (1, 5+1)
    t = input()                     # ooxxoxxooo
    T = list(t)                  # [o,o,x,x,o,x,x,o,o,o]    
    cnt = 0
    result = 0
    for x in range(0, len(T)):      # (0, 9+1)
        if T[x] == 'o':
            cnt += 1                # 1, 
            result += cnt           # 1, 
        else:
            cnt = 0
    print(result)            
# o가 나오면 cnt += 1
# x가 나오면 cnt = result += cnt / 0 으로 초기화 

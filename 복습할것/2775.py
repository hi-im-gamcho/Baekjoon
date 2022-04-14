t = int(input())                        # 테스트케이스


for i in range(t):
    k = int(input())                            # 층
    n = int(input())                            # 호

    floor = []                                  # 층의 개념
    list = []                                   # 호의 개념

    for i in range (1, n+1):
        list.append(i)                          # 0층의 i호에는 i명이 산다.
    
    floor.append(list)                          # 0층의 list가 완성되면 floor에 삽입.
    list = []

    for i in range(1, k+1):         # 1층부터 k층 까지
        for j in range(n):          # 1호부터 n호 까지.
            list.append(sum(floor[i-1][0:j+1]))
        floor.append(list)
        list = []

    print(floor[k][n-1])

# [
#     [],
#     [],
#     [],
# ]
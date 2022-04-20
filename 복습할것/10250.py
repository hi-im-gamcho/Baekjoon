# 초기에 모든 방이 비어있다고 가정하에
# N 번째로 도착한 손님에게 배정될 방 번호를 계산.

# 거리가 같으면 아래층 방을 더 선호.

t = int(input())

for i in range(t):
    h, w, n = [int(x) for x in input().split()] # 6, 12, 10
    # h = 층의 개수
    # w = 방의 개수
    # n = 손님 수
    rooms = []
    for w in range(1, w+1):
        for h in range(1, h+1):
            rooms.append(str(h) + str(w).zfill(2))
    print(rooms[n-1])

    
    



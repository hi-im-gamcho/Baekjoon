import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    # 출발점, 도착점
    x1, y1, x2, y2 = map(int, input().split())

    # 행성의 갯수
    n = int(input().rstrip())

    cnt = 0

    for _ in range(n):
        # 행성의 중심 / 반지름
        cx, cy ,r = map(int, input().split())
        start = (((x1 - cx)**2) + ((y1-cy)**2)) ** 0.5  # 행성중심 - 시작점 거리
        end = (((x2 - cx)**2) + ((y2-cy)**2)) ** 0.5    # 행성중심 - 도착점 거리

        if start < r and end < r :
            pass
        elif start < r:
            cnt += 1
        elif end < r: 
            cnt += 1
    
    print(cnt)





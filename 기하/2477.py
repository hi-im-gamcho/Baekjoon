import sys
input = sys.stdin.readline

K = int(input().rstrip())
farm = [list(map(int, input().split())) for _ in range(6)]  # 방향, 길이

w, w_idx = 0
h, h_idx = 0

# 가로, 세로의 최장값과 그 인덱스를 저장
for i in range(len(farm)):
    if farm[i][0] == 1 or farm[i][0] == 2:
        if w < farm[i][1]:
            w = farm[i][1]
            w_idx = i
    
    elif farm[i][0] == 3 or farm[i][0] == 4:
        if h < farm[i][1]:
            h = farm[i][1]
            h_idx = i


sub_w = abs(farm[(w_idx - 1) % 6][1] - farm[(w_idx + 1) % 6][1])
sub_h = abs(farm[(h_idx - 1) % 6][1] - farm[(h_idx + 1) % 6][1])

print(((w*h) - (sub_w*sub_h)) * K)

# https://itcrowd2016.tistory.com/84 근데 런타임에러남
# https://blog.naver.com/java_rang/222655215564
melon = int(input())

direction = []
distance = []

for _ in range(6):
    dir, dis = map(int, input().split())
    direction.append(dir)
    distance.append(dis)

direction += direction
distance += distance

idx = 0
for i in range(10):
    if direction[i] == direction[i+2] and direction[i+1] == direction[i+3]:
        idx = i
        break

area = (distance[idx+4] * distance[idx+5]) - (distance[idx+1] * distance[idx+2])
print(area*melon)
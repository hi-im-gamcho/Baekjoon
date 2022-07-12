import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
# W = width
# H = Height
# P = 선수의 수
players = 0
r = H // 2
for i in range(P):
    Px, Py = map(int, input().split())

    if X <= Px <= X + W and Y <= Py <= Y + H:   # 직사각형 내에 있을 경우
        players += 1
    elif (Px - (X + W))**2 + (Py - (Y + r))**2 <= r**2:
        players += 1
    elif (X - Px)**2 + ((Y + r) - Py)**2 <= r**2:
        players += 1

print(players)

x1, y1 = map(int, input().split())      # 1 < x, y =< 1000
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 축에 평행한 직사각형 만들기 위해 필요한 점 찾기.

if x1 == x2:
    x4 = x3
elif x2 == x3:
    x4 = x1
elif x3 == x1:
    x4 = x2

if y1 == y2:
    y4 = y3 
elif y2 == y3:
    y4 = y1
elif y3 == y1:
    y4 = y2

print(x4, y4)
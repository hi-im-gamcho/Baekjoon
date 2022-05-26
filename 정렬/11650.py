import sys
n = int(sys.stdin.readline())

coords = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
coords.sort()

for i in range(n):
    print("%d %d" %(coords[i][0], coords[i][1]))
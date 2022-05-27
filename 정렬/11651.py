import sys
n = int(sys.stdin.readline())

coords = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
coords.sort(key = lambda coords: (coords[1], coords[0]))


for i in range(len(coords)):
    sys.stdout.write(str(coords[i][0]) + " " + str(coords[i][1]) + "\n")

print(coords)
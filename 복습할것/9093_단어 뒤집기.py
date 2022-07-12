import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sen = input().split()
    for i in sen:
        print(i[::-1], end=' ')
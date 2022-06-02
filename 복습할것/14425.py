import sys

input = sys.stdin.readline

n, m = map(int, input().split())
S = {}
cnt = 0

for i in range(n):
    S[input()] = True

for x in range(m):
    if S.get(input()) == True:
        cnt += 1
    
print(cnt)

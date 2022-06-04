import sys
input = sys.stdin.readline

A, B = map(int, input().split())
list_A = set(map(int, input().split()))
cnt = 0

for i in set(map(int, input().split())):
    if i in list_A:
        cnt += 1
print(A + B - cnt*2)


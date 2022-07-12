import sys

input = sys.stdin.readline

N, M = map(int, input().split())
listen = []
result = []

for p in range(N):
    listen.append(input().rstrip())

for q in range(M):
    a = input().rstrip()
    if a in listen:
        result.append(a)

print(len(result))
print('\n'.join(sorted(result)))

# ------------내 코드 (시간초과)
# ------------아래건 다른사람코드. 근데 왜 밑에꺼가 더 삐른지 머르겠음.

# 듣보잡

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = []
arr2 = []

for i in range(n): #듣 못
    x = input()
    arr1.append(x)
    
for i in range(m): #보 못
    y = input()
    arr2.append(y)

answer = list(set(arr1) & set(arr2)) # 듣보잡 교집합
answer.sort()
print(len(answer))
print(''.join(answer), end = '') # 리스트

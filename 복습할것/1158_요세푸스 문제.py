import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

list_1 = deque([i for i in range(1,N+1)])
print("<", end='')
                            # [1,2,3,4,5,6,7]
for i in range(N-1):        # 0,1,2,3,4,5,6
    for _ in range(K-1):    # 0,1
        list_1.rotate(-1)
    print(list_1.popleft(), end=', ')
print(list_1.popleft(), end='>')

# (https://blog.naver.com/tmvmffpsej/222750258929) : 위 (이건 어떻게 생각한거냐...)
# (https://blog.naver.com/ej_0109/222750409304) : 아래

import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())

k = k-1

stack = []
q = deque([i for i in range(1,n+1)])

while q:
    q.rotate(-k)
    stack.append(q.popleft())

print("<", end = "")
print(*stack, sep=", ", end = "")
print(">", end = "")


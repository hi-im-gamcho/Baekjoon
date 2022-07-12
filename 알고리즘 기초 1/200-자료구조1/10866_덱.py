import sys
from collections import deque

input = sys.stdin.readline
D = deque()

for _ in range(int(input().rstrip())):
    order = input().split()
    
    if order[0] == "push_front":
        D.appendleft(order[1])
    elif order[0] == "push_back":
        D.append(order[1])
    elif order[0] == "pop_front":
        if len(D) == 0:
            print(-1)
        else:
            print(D[0])
            D.popleft()
    elif order[0] == "pop_back":
        if len(D) == 0:
           print(-1)
        else:
            print(D[-1])
            D.pop()
    elif order[0] == 'size':
        print(len(D))
    elif order[0] == 'empty':
        if len(D) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(D) == 0:
            print(-1)
        else: 
            print(D[0])
    elif order[0] == 'back':
        if len(D) == 0:
            print(-1)
        else: 
            print(D[-1])
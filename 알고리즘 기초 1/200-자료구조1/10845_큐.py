import sys

input = sys.stdin.readline
Q = []

for _ in range(int(input())):
    command = input().split()
    
    if command[0] == "push":
        Q.append(command[1])
    if command[0] == "pop":
        if len(Q) != 0:
            print(Q[0])
            Q.pop(0)
        else: 
            print(-1)
    if command[0] == "size":
        print(len(Q))
    if command[0] == "empty":
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    if command[0] == "front":
        if len(Q) != 0:
            print(Q[0])
        else:
            print(-1)
    if command[0] == "back":
        if len(Q) != 0:
            print(Q[-1])  
        else:
            print(-1)
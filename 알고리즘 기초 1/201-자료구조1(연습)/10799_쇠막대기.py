import sys

input = sys.stdin.readline

Q = input()
cnt = 0
result = 0

for i in range(len(Q)):
    if Q[i] == '(':
        cnt += 1
    else:
        if Q[i-1] == '(':
            cnt -= 1
            result += cnt
        else:
            cnt -= 1
            result += 1

print(result)


    

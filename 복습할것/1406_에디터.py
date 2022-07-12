import sys

input = sys.stdin.readline

stack1 = list(input().rstrip())     #   ['a','b','c','d' ]
stack2 = []

for _ in range(int(input().rstrip())):
    cmd = input().split()
    
    if cmd[0] == 'L':
        stack2.append(stack1.pop())
    elif cmd[0] == 'D':
        stack1.append(stack2.pop())
    elif cmd[0] == 'B':     
        stack1.pop()
    elif cmd[0] == 'P':
        stack1.append(cmd[1])

print(''.join(stack1 + stack2[::-1]))


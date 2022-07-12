import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])    # 맨 뒤의 값을 출력
            del stack[-1]       # 맨 뒤의 값 삭제
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack) == 0:
            print(stack[-1])
        else:
            print(stack[-1])

### 이게 내가한건데 왜 이건 런타임 에러 뜨고
### 아래껀 맞았다고하냐...
import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
        a = sys.stdin.readline().split()
        o = a[0]
    
        if o == "top":
            if len(l) == 0: 
                print(-1) 
            else: 
                print(l[-1]) 
        elif o == "pop": 
            if len(l) == 0: 
                print(-1) 
            else:
                print(l[-1])
                del l[-1] 
        elif o == "size": 
            print(len(l))
        elif o == "empty":
            if len(l) == 0: 
                print(1) 
            else:
                print(0) 
        elif o == "push":
            l.append(int(a[1])) 






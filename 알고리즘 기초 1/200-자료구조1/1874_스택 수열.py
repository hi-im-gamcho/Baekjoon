# 스택에 '넣었다가(전제조건)' '뽑아 늘어놓음으로써' 수열을 만들 수 있다.
# 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.
# 스택에 push하는 순서는 반드시 '오름차순'을 지키도록 한다고 하자.
import sys
n = int(input())

data = [i for i in range(n)]    # [1,2,3,4,5,6,7,8]   오름차순 수열

target = []                     # [4,3,6,8,7,5,2,1]   목표로 하는 수열
stack = []
result = []                     # 결과
temp = []
for _ in range(n):
    target.append(int(input()))

for i in target:
    if i in data:
        for j in range(data.index(i)+1):
            stack.append(data[j])
            result.append('+')
            temp.append(data[j])
        for j in temp:
            data.remove(j)
        temp.clear()

    if i in stack:
        if stack[-1] != i:
            print('NO')
            sys.exit()
        else:
            stack.pop()
            result.append('-')

for i in result:
    print(i)


# 출처 1 : https://blog.naver.com/dltldns852/222667031713
# 출처 2 : https://pacific-ocean.tistory.com/231




# 오큰수 = 오른쪽에 있으면서 /  Ai보다 큰 수 중에서 / 가장 왼쪽에 있는 수

N = int(input())                    # 4
A = list(map(int, input().split())) # 3/5/2/7

ans = [-1] * N  # [-1, -1, -1, -1] 이라는 리스트 선언
stack = [0]

for i in range(1, N):
#                   stack의 맨 마지막 요소를 index로 가지는 A의 값보다 / A[i]가 더 크다면 
    while stack and A[stack[-1]] < A[i]:
#   1차 : a[0] < a[1] 이라면    
        ans[stack.pop()] = A[i]
    stack.append(i) #[1,2]
print(*ans)


### Q : 궁금한건 11항의 조건 중 stack이 왜 필요한거지???
### A : 반복문을 빠져나가기 위한 종료조건임.
###     i=1 일 때 while stack이라는 조건이 없다면 A[stack[-1]] < A[1]이라는 조건을 항상 만족하기 때문에
###     반복문이 끝나지 않음.
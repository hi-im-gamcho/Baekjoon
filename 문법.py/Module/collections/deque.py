from collections import deque

q = deque([i for i in range(1, 7+1)])

# 1. q.append(item) : 오른쪽 끝에 삽입.
# 2. q.appendleft(item) : 왼쪽 끝에 삽입.

# 3. q.pop() : 가장 오른쪽의 요소 반환 및 삭제.
# 4. q.popleft() : 가장 왼쪽의 요소 반환 및 삭제.

# 5. q.extend(array) : 주어진 array 배열을 순환하며 q의 오른쪽에 추가.
# 6. q.extendleft(array) : 주어진 array 배열을 순환하며 q의 왼쪽에 추가.

# 7. q.remove(item) : 해당 '요소'를 q에서 찾아 삭제.

# 8. q.rotate(숫자) : 해당 숫자만큼 회전. (양수 : 시계방향, 음수 : 반시계 방향)
# 데크가 비어 있지 않으면, 
# 오른쪽으로 한 단계 회전하는 것은 d.appendleft(d.pop())과 동등하고, 
# 왼쪽으로 한 단계 회전하는 것은 d.append(d.popleft())와 동등하다.
print(q.rotate(1))  # deque([7, 1, 2, 3, 4, 5,6])
print(q.rotate(-1))  # deque([2, 3, 4, 5, 6, 7, 1])

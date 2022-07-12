# (https://honggom.tistory.com/68)

# ai의 오큰등수 = 오른쪽에 있으면서 / 등장한 횟수가 F(ai) 보다 큰 수 중에서 / 가장 왼쪽에 있는 수
# F(ai) = ai가 등장한 횟수 

from sys import stdin
from collections import Counter

N = int(stdin.readline())
nums = [int(i) for i in stdin.readline().split()]
nums_cnt = Counter(nums)
result = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and nums_cnt[nums[stack[-1]]] < nums_cnt[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)
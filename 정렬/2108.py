import sys
from collections import Counter

num_list = []
n = int(sys.stdin.readline())

for i in range(n):
    num_list.append(int(sys.stdin.readline()))


# 산술평균
print(round((sum(num_list)) / n))

# 중앙값
num_list.sort()
print(num_list[n//2])

# 최빈값
cnt = Counter(num_list).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]: # 빈도수가 같은게 2개 이상 있다면 
    print(cnt[1][0])
else:
    print(cnt)
    print([0][0])

# 범위
print(max(num_list) - min(num_list))
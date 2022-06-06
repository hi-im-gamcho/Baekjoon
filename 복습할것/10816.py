import sys

input = sys.stdin.readline
n = int(input().rstrip())
card_list = list(map(int, input().split()))
result = {}

for p in set(card_list):
    result[p] = card_list.count(p)

m = int(input().rstrip())
coords = list(map(int, input().split()))

for q in coords:
    print(result.get(q, 0), end=' ')

# -------위는 내가 작성한 코드 (시간 초과)----------
# -------아래는 다른 사람 코드 ---------------------

from collections import Counter
import sys

input = sys.stdin.readline

n = int(input().rstrip())
card_list = list(map(int, input().split()))
m = int(input().rstrip())
coords = list(map(int, input().split()))

card_list = Counter(card_list)

for i in coords:
    print(card_list[i], end=' ')

n, m = map(int, input().split())
# n = 카드의 개수
# m = 카드에 쓰여 있는 수
num = list(map(int, input().split()))
result = []

for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            if num[a] + num[b] + num[c] <= m:
                result.append(num[a] + num[b] + num[c])

print(max(result))

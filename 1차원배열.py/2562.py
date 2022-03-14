list_n = []

# 리스트에 요소를 추가하는 과정을 N 번 반복
for i in range(1, 9+1):
    list_n.append(int(input()))

M = max(list_n)

print(M)
print(list_n.index(M) + 1)
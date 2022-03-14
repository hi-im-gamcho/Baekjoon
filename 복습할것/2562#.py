list_n = []

for i in range(1, 9+1):
    list_n.append(int(input()))

M = max(list_n)

print(M)
print(list_n.index(M) + 1)
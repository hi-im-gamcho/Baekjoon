list_num = []
list_left = []
result = []
for i in range(1, 10+1, 1):
    list_num.append(int(input()))      # a = [1,2,3,4,5,6,7,8,9,10]
print(list_num)

for i in range(0, 9+1, 1):
    left = list_num[i] % 42
    list_left.append(left)

for x in list_left: 
    if x not in result:
        result.append(x)

print(len(result))

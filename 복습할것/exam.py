list_num = []
list_left = []


for i in range(0, 9+1):
    list_num.append(int(input()))          # [1,2,3,4,5,6,7,8,9,43]

for i in list_num:
    list_left.append(i%42)


print(len(list(set(list_left))))

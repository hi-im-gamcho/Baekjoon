list_num = []
list_left = []
result = []

for i in range(1, 10+1):
    # list_num = [1,2,3,4,5,6,7,8,9,10]
    list_num.append(int(input()))
    # list_num 의 요소를 42 로 나눈 나머지를 list_left에 저장   
    list_left.append(list_num[i-1] % 42)

# list_left의 요소들중에서 중복되지 않는것만 result에 넣어서 길이 계산
for x in list_left:
    if x not in result:
        result.append(x)
    
print(len(result))







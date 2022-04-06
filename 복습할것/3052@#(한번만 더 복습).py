list_num = []
list_left = []
result = []

for i in range(1, 10+1):
    # list_num = [1,2,3,4,5,6,7,8,9,10]
    list_num.append(int(input()))
    # list_num 의 요소를 42 로 나눈 나머지를 list_left에 저장   
    list_left.append(list_num[i-1] % 42)

# list_left의 요소들중에서 중복되지 않는것만 result에 넣어서 길이 계산 
# 13 - 15 항을 생각 못해서 못풀었는데
# 리스트의 요소 중, '조건에 만족하는것만 새로운 리스트에 넣음' 이라는 아이디어는
# 유용하게 사용할 수 있는 아이디어인듯.
for x in list_left:
    if x not in result:
        result.append(x)
    
print(len(result))







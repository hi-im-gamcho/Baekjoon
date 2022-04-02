a = input()                     # 어차피 인덱스로 숫자에 접근해야하니까
b = input()                     # 초장부터 int형으로 굳이 바꿀 필요 없음

print(int(a) * int(b[2]))
print(int(a) * int(b[1]))
print(int(a) * int(b[0]))
print(int(a) * int(b))

#--------------- 다른 풀이 -------------------

a = int(input())                # 472
b = int(input())                # 385

list_b = list(str(b))           # [3,8,5]

for i in range(2, 0-1, -1):
    print(a * int(list_b[i]))   # 472 * 
print(a*b)

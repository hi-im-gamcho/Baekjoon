a = int(input())
b = int(input())
c = int(input())

mul = a*b*c                         # a,b,c의 곱
list_mul = list(str(mul))           # 을 str로 바꿔서 리스트화
                                    
for i in range(0, 9+1):
    print(list_mul.count(str(i)))


# ---------- 내가 처음 했던 풀이--------------
a = int(input())            
b = int(input())
c = int(input())

result = str((a*b*c))            # a,b,c의 곱
count = result.count("0")
print(count)                    # 0이 몇번 쓰였는지 출력

for i in range(1, 9+1):
    count = result.count(str(i))
    print(count)

# 문제를 제대로 파악하지 않아서 생긴 문제.
# count 함수를 활용한다면 쉽게 풀 수 있음.
def selfnum(n):
    # 자기자신 + 자릿수로 나눈 리스트의 합
    n = n + sum(map(int, str(n)))
    # 새로운n = 생성자
    return n

a = [0]*10001
# selfnum을 반복
for i in range (1, 10000+1):
    a[i] =  selfnum(i)

for i in range(1, 10000+1):
    if(i not in a):
        print(i)



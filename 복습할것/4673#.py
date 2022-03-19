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


#--------------------------------------------------------------------
                 # x 에 dn 이 없으면 i(셀프넘버) 출력
                            # x 에 dn 저장

# 셀프넘버 = 생성자가 없는 숫자
# 2. dn을 x에 넣음
x = []
# 1. dn을 구함
for n in range(1, 10000+1):
    N = n                           # 123
    n = list(str(n))                # [1,2,3]
    num = 0                         
    for i in range(0, len(n)):      # (0,2+1)
        num += int(n[i])                 # 1+2+3
    num += N                        # 1+2+3+123
    x.append(num)                   # x = [123]    

for i in range(1, 10000+1):
    if i not in x:
        print(i)



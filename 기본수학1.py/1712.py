a,b,c, = map(int, input().split())

# a + bn <= cn  
# a <= n(c-b)
# a / c-b <= n 

if b >= c:      # 손익분기점 없음
    print(-1)
else:
    print(a//(c-b) + 1)     # 손익분기점은 정수이므로 정수연산자를 사용해야함
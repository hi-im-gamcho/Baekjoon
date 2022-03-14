a, b = [int(x) for x in input().split()] 
print(a+b)
print()

# 다른 풀이
# int 함수가 저렇게 사용됬음에 주목하자!!
c = list(map(int, input().split()))
print(c[0] + c[1])
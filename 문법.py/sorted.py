# 기존의 리스트는 그대로 둔 채 '새로운 리스트를 만들어서 정렬해야할 때' 사용
# '비파괴적 함수'
# 변수 이름 = sorted(정렬하고싶은 리스트)  와 같은 형태로 사용
# sorted(리스트명, value, key)

# 1. 숫자로 구성된 리스트 오름차순 정렬
a = [3,2,4,1,5]
b = sorted(a)
print(a)
print(b)

# 2. 숫자로 구성된 리스트 내림차순으로 정렬
c = [3,2,4,1,5]
d = sorted(c, reverse=True)
print(c)
print(d)

# 문자열도 sort()와 같으니까 생략

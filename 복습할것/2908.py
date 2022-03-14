a,b = input().split()
# 확장슬라이싱을 통해 뒤집기
reverse_a = int(a[::-1])
reverse_b = int(b[::-1])

if reverse_a > reverse_b:
    print(reverse_a)
if reverse_a < reverse_b:
    print(reverse_b)

# 1. reversed 함수 뿐만이 아니라 확장 슬라이싱을 통해서도 뒤집기가 가능하다.
# 2. 확장 슬라이싱은 리스트 뿐만이 아니라 문자열에도 가능하다. 단, int형에는 안됨!
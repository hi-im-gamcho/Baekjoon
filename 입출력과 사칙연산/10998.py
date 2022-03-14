# 두 정수 A와 B를 입력받은 다음, 
# A×B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 1번째 방법
a = list(map(int, input().split()))
print(a[0] * a[1])

# 2 번째 방법
b, c = [int(i) for i in input().split()]
print(b*c)
import sys

T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

# 배운점

# sys.stdin.readline()도 input()과 같이 입력값을 받는 함수다.
# 전자를 사용하려면 import sys를 첫 줄에 꼭 써줘야한다.
# 둘의 가장 큰 차이점으로 전자는 개행문자를 같이 입력받아서 
# 문자열을 입력받을 때는 .rstrip()으로 개행문자를 제거해주어야한다.
# 전자를 사용하는 이유는 시간초과를 피하기 위해서다! 즉, input()보다 입력이 빠르다!

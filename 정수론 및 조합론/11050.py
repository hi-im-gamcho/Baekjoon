import sys
input = sys.stdin.readline
N, K = map(int, input().split())

dict_fibo = {
    1: 1,
    2: 2
}

def factorial(i):
    if i in dict_fibo:
        return dict_fibo[i]
    else:
        output = i * factorial(i-1)
        dict_fibo[i] = output
        return output

def comb (n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

print(comb(N, K))

#--------------------위는 내가 처음 한 풀이 : 런타임 에러
#--------------------아래는 두번째 풀이
import sys
def factorial(num): # num!을 구해주는 함수
    number = 1
    for i in range(2,num+1):
        number *= i
    return number

n, k = map(int, sys.stdin.readline().split()) # n, k 입력

print(int(factorial(n)/(factorial(k)*factorial(n-k)))) # nCk를 프린트


